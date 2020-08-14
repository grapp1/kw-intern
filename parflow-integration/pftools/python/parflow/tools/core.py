import os

from .database.generated import BaseRun, PFDBObj
from .utils import extract_keys_from_object, write_dict
from .terminal import Symbols as termSymbol


class Run(BaseRun):
    def __init__(self, name, basescript=None):
        super().__init__(None)
        self._name = name
        if basescript:
            PFDBObj.set_working_directory(os.path.dirname(basescript))

    def get_current_parflow_version(self):
        version_file = f'{os.getenv("PARFLOW_DIR")}/config/pf-cmake-env.sh'
        if os.path.exists(os.path.abspath(version_file)):
            with open(version_file, "rt") as f:
                for line in f.readlines():
                    if 'PARFLOW_VERSION=' in line:
                        version = line[17:22]
                if not version:
                    print(f'Cannot find version in {version_file}')
        else:
            print(
                f'Cannot find environment file in {os.path.abspath(version_file)}.')
        return version

    def get_key_dict(self):
        key_dict = {}
        extract_keys_from_object(key_dict, self)
        return key_dict

    # TODO: add feature to read external files
    # def readExternalFile(self, file_name=None, fileFormat='yaml'):
    #     inputDict = externalFileToDict(file_name, fileFormat)
    #     for key, value in inputDict.items():
    #         if not value == 'NA':
    #             # extKeyList =
    #             extKey = '.'.join(self, key)
    #             # print(extKey)

    def write(self, file_name=None, file_format='pfidb'):
        f_name = os.path.join(PFDBObj.working_directory,
                              f'{self._name}.{file_format}')
        if file_name:
            f_name = os.path.join(PFDBObj.working_directory,
                                  f'{file_name}.{file_format}')
        full_file_path = os.path.abspath(f_name)
        write_dict(self.get_key_dict(), full_file_path)
        return full_file_path, full_file_path[:-(len(file_format)+1)]

    def check_parflow_execution(self, run_name):
        print(f'# {"="*78}')
        out_file = f'{run_name}.out.txt'
        if os.path.exists(out_file):
            with open(out_file, "rt") as f:
                contents = f.read()
                if 'Problem solved' in contents:
                    print(f'# ParFlow ran successfully {termSymbol.splash*3}')
                else:
                    print(
                        f'# ParFlow run failed. {termSymbol.x} {termSymbol.x} {termSymbol.x} Contents of error output file:')
                    print("-"*80)
                    print(contents)
                    print("-"*80)
        else:
            print(f'# Cannot find {out_file} in {os.getcwd()}')
        print(f'# {"=" * 78}')

    def run(self, working_directory=None, skip_validation=False):
        if working_directory:
            PFDBObj.set_working_directory(working_directory)

        file_name, run_file = self.write()

        PFDBObj.set_parflow_version(self.get_current_parflow_version())

        print()
        print(f'# {"="*78}')
        print(f'# ParFlow directory')
        print(f'#  - {os.getenv("PARFLOW_DIR")}')
        print(f'# ParFlow version')
        print(f'#  - {PFDBObj.pf_version}')
        print(f'# Working directory')
        print(f'#  - {os.path.dirname(file_name)}')
        print(f'# ParFlow database')
        print(f'#  - {os.path.basename(file_name)}')
        print(f'# {"="*78}')
        print()

        if not skip_validation:
            self.validate()
            print()

        p = self.Process.Topology.P
        q = self.Process.Topology.Q
        r = self.Process.Topology.R
        num_procs = p * q * r

        os.chdir(PFDBObj.working_directory)
        os.system('sh $PARFLOW_DIR/bin/run ' + run_file + ' ' + str(num_procs))

        self.check_parflow_execution(run_file)
        print()
