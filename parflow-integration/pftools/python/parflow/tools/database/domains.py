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
    version_tokens = version.split('.')
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
    def validate(self, value, **kwargs):
        errors = []

        if value is None:
            errors.append(error('Needs to be set'))
            return errors

        return errors


class IntValue:
    '''
    IntRange domain allow to constrain value to be an integer
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
    DoubleValue domain allow to constrain value to be a double
    while also ensure optionally if its value needs to be
    above or below another one.

    The expected set of keyword arguments are:
      - min_value: If available the value must be strictly above it
      - max_value: If available the value must be strictly below it
    '''

    def validate(self, value, min_value=None, max_value=None, neg_int=None, **kwargs):
        errors = []

        if value is None:
            return errors

        # added for verification of DumpInterval (double if positive, int if negative)
        if neg_int and isinstance(value, int) and value < 0:
            return errors

        elif not isinstance(value, float):
            errors.append(error('Needs to be a double'))

        if min_value is not None and value < min_value:
            errors.append(error(f'Is smaller than min: {min_value}'))
        if max_value is not None and value > max_value:
            errors.append(error(f'Is greater than max: {max_value}'))

        return errors

# -----------------------------------------------------------------------------


class EnumDomain:
    def validate(self, value, enum_list=[], **kwargs):
        errors = []

        if value is None:
            return errors

        if isinstance(value, list) and len(value) == 1:
            value = value[0]

        if value not in enum_list:
            str_list = ', '.join(enum_list)
            errors.append(error(f'{value} must be one of [{str_list}]'))

        return errors

# -----------------------------------------------------------------------------


class AnyString:
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


class Deprecated:
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


class Removed:
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

def validate_value_with_print(name, value, domain_definition=None, domain_add_on_kwargs=None, history=None, indent=1):
    indent_str = '  ' * (indent - 1)
    all_messages = validate_value_with_errors(
        value, domain_definition, domain_add_on_kwargs)
    errors = filter_errors_by_type('ERROR', all_messages)
    warnings = filter_errors_by_type('WARNING', all_messages)

    if len(errors):
        print(f'{indent_str}  {term.FAIL}{term_symbol.ko}{term.ENDC} {name}: {value}')
        for error in errors:
            print(
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
                print(
                    f'{indent_str}  {term.MAGENTA}{term_symbol.warning}{term.ENDC} {name}: {value}  {term.MAGENTA}{dup_str}{term.ENDC}')
            # elif 'default' in name
            else:
                print(
                    f'{indent_str} {name}: {value} {term.OKGREEN}{term_symbol.ok}{term.ENDC}')
        else:
            print(
                f'{indent_str}  {name}: {value} {term.OKGREEN}{term_symbol.ok}{term.ENDC}')

    if len(warnings):
        for warning in warnings:
            print(
                f'{indent_str}    {term.CYAN}{term_symbol.warning}{term.ENDC} {warning}')

    return len(errors)


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