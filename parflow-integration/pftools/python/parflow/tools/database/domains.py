r'''
This module aims to gather all kind of value validation you would like to
enable inside Parflow run.
'''

import sys
import traceback
import os

from ..terminal import Colors as term
from ..terminal import Symbols as term_symbol

# -----------------------------------------------------------------------------
# Validation helper functions
# -----------------------------------------------------------------------------

def filter_errors_by_type(msg_type, errors):
    filter_list = []
    for error in errors:
        if error['type'] == msg_type:
            filter_list.append(error['message'])

    return filter_list

# -----------------------------------------------------------------------------

def error(message):
    return {
        'type': 'ERROR',
        'message': message
    }

# -----------------------------------------------------------------------------

def warning(message):
    return {
        'type': 'WARNING',
        'message': message
    }

# -----------------------------------------------------------------------------

def duplicate_search(history):
    if len(history) > 1:
        dup_count = len(history)
        return dup_count
    else:
        pass

# -----------------------------------------------------------------------------

def get_comparable_version(version):
    c_version = 0
    validVersionNumber = version[1:] if version[0] == 'v' else version
    version_tokens = validVersionNumber.split('.')
    for version_token in version_tokens:
        c_version *= 1000
        c_version += int(version_token)
    return c_version

# -----------------------------------------------------------------------------

def get_installed_parflow_module(module):
    module_file = f'{os.getenv("PARFLOW_DIR")}/config/Makefile.config'
    has_module_installed = False
    if os.path.exists(os.path.abspath(module_file)):
        with open(module_file, "rt") as f:
            for line in f.readlines():
                if f'PARFLOW_HAVE_{module}' in line and 'yes' in line:
                    has_module_installed = True
    else:
        print(
            f'Cannot find Makefile.config in {os.path.abspath(module_file)}.')
    return has_module_installed

# -----------------------------------------------------------------------------
# Validation classes
# -----------------------------------------------------------------------------


class ValidationException(Exception):
    '''
    Basic parflow exception used for domains to report error
    '''
    pass

# -----------------------------------------------------------------------------


class MandatoryValue:
    '''
    MandatoryValue makes sure that the key is set

    If the value is not defined in the script and has a default value,
    the default value will be written out in the validation message and database file.
    '''
    def validate(self, value, **kwargs):
        errors = []

        if value is None:
            errors.append(error('Needs to be set'))
            return errors

        return errors


class IntValue:
    '''
    IntRange domain constrains value to be an integer
    while also ensure optionally if its value needs to be
    above or below another one.

    The expected set of keyword arguments are:
      - min_value: If available the value must be strictly above it
      - max_value: If available the value must be strictly below it
    '''
    # NEED TO COME UP WITH A BETTER WAY TO HANDLE THE VARIABLE DZ CORNER CASE

    def validate(self, value, min_value=None, max_value=None, into_list=False, **kwargs):
        errors = []

        if value is None:
            return errors

        if not isinstance(value, int):
            errors.append(error('Needs to be an integer'))

        if into_list:
            return errors

        if min_value is not None and value < min_value:
            errors.append(error(f'Is smaller than min: {min_value}'))
        if max_value is not None and value > max_value:
            errors.append(error(f'Is greater than max: {max_value}'))

        return errors


class DoubleValue:
    '''
    DoubleValue domain constrains value to be a double (or int)
    while also ensure optionally if its value needs to be
    above or below another one.

    The expected set of keyword arguments are:
      - min_value: If available the value must be strictly above it
      - max_value: If available the value must be strictly below it
    '''

    def validate(self, value, min_value=None, max_value=None, **kwargs):
        errors = []

        if value is None:
            return errors

        if not (isinstance(value, float) or isinstance(value, int)):
            errors.append(error('Needs to be a double'))

        if min_value is not None and value < min_value:
            errors.append(error(f'Is smaller than min: {min_value}'))
        if max_value is not None and value > max_value:
            errors.append(error(f'Is greater than max: {max_value}'))

        return errors

# -----------------------------------------------------------------------------


class EnumDomain:
    '''
    EnumDomain domain constrains value to be a particular string
    that is part of a list defined in the enum_list.

    The expected keyword argument is a list of the accepted values.
    '''

    def validate(self, value, enum_list=[], pf_version=None, **kwargs):
        errors = []

        if value is None:
            return errors

        if isinstance(value, list) and len(value) == 1:
            value = value[0]

        lookupList = []
        if isinstance(enum_list, list):
          lookupList = enum_list

        if isinstance(enum_list, dict):
          # We need to find the matching version
          sortedVersions = [(get_comparable_version(v), v) for v in enum_list.keys()]
          sortedVersions.sort(key=lambda t: t[0])
          versionToUse = sortedVersions[0]
          currentVersion = get_comparable_version(pf_version)
          for version in sortedVersions:
            if currentVersion >= version[0]:
              versionToUse = version

          lookupList = enum_list[versionToUse[1]]

        if value not in lookupList:
            str_list = ', '.join(lookupList)
            errors.append(error(f'{value} must be one of [{str_list}]'))

        return errors

# -----------------------------------------------------------------------------


class AnyString:
    '''
    AnyString domain constrains the value to be a string or list of strings.
    '''
    def validate(self, value, **kwargs):
        errors = []

        if value is None:
            return errors

        if isinstance(value, list) or isinstance(value, str):
            return errors

        errors.append(error(f'{value} ({type(value)} must be a string'))
        return errors

# -----------------------------------------------------------------------------


class BoolDomain:
    '''
    BoolDomain domain constrains the value to be a boolean.
    '''
    def validate(self, value, **kwargs):
        errors = []

        if value is None:
            return errors

        if isinstance(value, bool):
            return errors

        errors.append(error(f'{value} ({type(value)} must be True/False)'))
        return errors

# -----------------------------------------------------------------------------


class ValidFile:
    '''
    ValidFile domain checks the working directory to find the specified file.
    '''
    def validate(self, value, working_directory=None, **kwargs):
        errors = []

        if value is None:
            return errors

        if working_directory is None:
            errors.append(error('Working directory is not defined'))
            return errors

        if os.path.exists(os.path.join(working_directory, value)):
            return errors

        errors.append(error(
            f'Could not locate file {os.path.abspath(os.path.join(working_directory, value))}'))
        return errors


# -----------------------------------------------------------------------------


class AddedInVersion:
    '''
    AddedInVersion domain deals with keys that were added to the ParFlow code in
    recent versions. It will check your version of ParFlow with the added version
    and print an error if your ParFlow version does not have the given key.
    '''
    def validate(self, value, arg, pf_version=None, **kwargs):
        errors = []

        if value is None:
            return errors

        version = get_comparable_version(arg)
        current_version = get_comparable_version(pf_version)

        if version <= current_version:
            errors.append(error(f'Removed in v{arg}'))

        if version > current_version:
            errors.append(warning(f'Will be removed in v{arg}'))

        return errors



# -----------------------------------------------------------------------------


class DeprecatedInVersion:
    '''
    DeprecatedInVersion domain deals with keys that have been or will be deprecated. It
    will check your version of ParFlow with the deprecated version and print
    an error or warning depending on whether the key has been deprecated.
    '''
    def validate(self, value, arg, pf_version=None, **kwargs):
        errors = []

        if value is None:
            return errors

        version = get_comparable_version(arg)
        current_version = get_comparable_version(pf_version)

        if version <= current_version:
            errors.append(error(f'Deprecated in v{arg}'))

        if version > current_version:
            errors.append(warning(f'Will be deprecated in v{arg}'))

        return errors

# -----------------------------------------------------------------------------


class RemovedInVersion:
    '''
    RemovedInVersion domain deals with keys that have been or will be removed from the
    ParFlow code. It will check your version of ParFlow with the removed version
    and print an error or warning depending on whether the key has been or will
    be removed.
    '''
    def validate(self, value, arg, pf_version=None, **kwargs):
        errors = []

        if value is None:
            return errors

        version = get_comparable_version(arg)
        current_version = get_comparable_version(pf_version)

        if version <= current_version:
            errors.append(error(f'Removed in v{arg}'))

        if version > current_version:
            errors.append(warning(f'Will be removed in v{arg}'))

        return errors

# -----------------------------------------------------------------------------


class RequiresModule:
    '''
    RequiresModule domain deals with keys that require specific modules associated
    with ParFlow (e.g. CLM, SILO, NetCDF, etc.). It will check to see whether the
    required modules are installed with ParFlow and will print an error message
    if the required module is missing.
    '''
    def validate(self, value, arg, **kwargs):
        errors = []

        if value is None:
            return errors

        arg_list = arg.split() if isinstance(arg, str) else arg

        for module in arg_list:
            if not get_installed_parflow_module(module):
                errors.append(error(f'Need to install {module} module'))

        return errors

# -----------------------------------------------------------------------------
# Helper map with an instance of each domain type
# -----------------------------------------------------------------------------


AVAILABLE_DOMAINS = {}


def get_domain(class_name):
    if class_name in AVAILABLE_DOMAINS:
        return AVAILABLE_DOMAINS[class_name]

    if hasattr(sys.modules[__name__], class_name):
        klass = getattr(sys.modules[__name__], class_name)
        instance = klass()
        AVAILABLE_DOMAINS[class_name] = instance
        return instance

    print(f'{term.FAIL}{term_symbol.ko}{term.ENDC} Could not find domain: "{class_name}"')

    return None

# -----------------------------------------------------------------------------
# API meant to be used outside of this module
# -----------------------------------------------------------------------------


def validate_value_with_errors(value, domain_definitions=None, domain_add_on_kwargs=None):
    '''
    domain_definitions = {
      IntRangeDomain: {
        min_value: 1
      },
      NoNoneValueDomain:
    }
    This method validates the value set to a key using the domains provided in the key
    definition files.
    '''
    errors = []
    if not domain_definitions:
        return errors

    for domain_classname in domain_definitions:
        domain = get_domain(domain_classname)
        if domain:
            domain_kwargs = {}
            if domain_add_on_kwargs:
                domain_kwargs.update(domain_add_on_kwargs)

            if domain_definitions[domain_classname]:
                if isinstance(domain_definitions[domain_classname], str):
                    domain_kwargs['arg'] = domain_definitions[domain_classname]
                elif isinstance(domain_definitions[domain_classname], list):
                    domain_kwargs['arg'] = domain_definitions[domain_classname]
                else:
                    domain_kwargs.update(domain_definitions[domain_classname])

            errors.extend(domain.validate(value, **domain_kwargs))

    return errors

# -----------------------------------------------------------------------------


def validate_value_with_exception(value, domain_definition=None, domain_add_on_kwargs=None, exit_on_error=False):
    all_messages = validate_value_with_errors(
        value, domain_definition, domain_add_on_kwargs)
    errors = filter_errors_by_type('ERROR', all_messages)

    if len(errors):
        print()
        try:
            raise ValidationException()
        except ValidationException:
            exp, val, tb = sys.exc_info()
            listing = traceback.format_stack(tb.tb_frame)
            for item in listing:
                if 'parflow/database' in item:
                    continue
                print(item)

        print(f'    The value {value} is invalid')
        for error in errors:
            print(f'    - {error}')
        print()

        if exit_on_error:
            sys.exit(1)

# -----------------------------------------------------------------------------

def validate_value_to_string(name, value, domain_definition=None, domain_add_on_kwargs=None, history=None, indent=1):
    indent_str = '  ' * (indent - 1)
    all_messages = validate_value_with_errors(
        value, domain_definition, domain_add_on_kwargs)
    errors = filter_errors_by_type('ERROR', all_messages)
    warnings = filter_errors_by_type('WARNING', all_messages)
    validation_string = []

    if len(errors):
        validation_string.append(
            f'{value} {term.FAIL}{term_symbol.ko}{term.ENDC}')
        for error in errors:
            validation_string.append(
                f'{indent_str}    {term.WARNING}{term_symbol.errorItem}{term.ENDC} {error}')
    elif value is not None:
        # checking for duplicates and changing print statement
        if history is not None:
            dup_count = duplicate_search(history)
            if dup_count is not None and dup_count >= 1:
                # offset = 1 if 'default' in name else 1
                dup_str = '('
                for val in range(dup_count-1):
                    dup_str += str(history[val]) + ' => '
                dup_str += str(history[dup_count-1]) + ')'
                validation_string.append(
                    f'{term.MAGENTA}{term_symbol.warning}{term.ENDC} {value}  {term.MAGENTA}{dup_str}{term.ENDC}')
            # elif 'default' in name
            else:
                validation_string.append(
                    f'{value} {term.OKGREEN}{term_symbol.ok}{term.ENDC}')
        else:
            validation_string.append(
                f'{value} {term.OKGREEN}{term_symbol.ok}{term.ENDC}')

    if len(warnings):
        for warning in warnings:
            validation_string.append(
                f'{indent_str}    {term.CYAN}{term_symbol.warning}{term.ENDC} {warning}')

    return len(all_messages), '\n'.join(validation_string)
