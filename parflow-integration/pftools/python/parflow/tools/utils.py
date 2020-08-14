import json

from .database.generated import PFDBObj

# -----------------------------------------------------------------------------


def convert_value_for_string_dict(value):
    if isinstance(value, str):
        return value

    if hasattr(value, '__iter__'):
        return ' '.join([str(v) for v in value])

    return value

# -----------------------------------------------------------------------------


def extract_keys_from_object(dict_to_fill, instance, parent_namespace=''):
    for key in instance.get_key_names(skip_default=True):

        value = instance.__dict__[key]
        if value is None:
            continue

        full_qualified_key = instance.get_parflow_key(parent_namespace, key)
        if isinstance(value, PFDBObj):
            if hasattr(value, '_value'):
                dict_to_fill[full_qualified_key] = convert_value_for_string_dict(
                    value._value)
            extract_keys_from_object(dict_to_fill, value, full_qualified_key)
        else:
            dict_to_fill[full_qualified_key] = convert_value_for_string_dict(value)

# -----------------------------------------------------------------------------

# TODO: add feature to read external files
# def external_file_to_dict(file_name, fileFormat):
#     externalFileDict = {}
#     externalFileDict['GeomInput.Names.domain_input.InputType'] = 'Box'
#     print(externalFileDict)
#     return externalFileDict

# -----------------------------------------------------------------------------


def write_dict_as_pfidb(dict_obj, file_name):
    with open(file_name, 'w') as out:
        out.write(f'{len(dict_obj)}\n')
        for key in dict_obj:
            out.write(f'{len(key)}\n')
            out.write(f'{key}\n')
            value = dict_obj[key]
            out.write(f'{len(str(value))}\n')
            out.write(f'{str(value)}\n')

# -----------------------------------------------------------------------------


def write_dict_as_yaml(dict_obj, file_name):
    with open(file_name, 'w') as out:
        for key in dict_obj:
            value = dict_obj[key]
            out.write(f'{key}: {value}\n')

# -----------------------------------------------------------------------------


def write_dict_as_json(dict_obj, file_name):
    with open(file_name, 'w') as out:
        out.write(json.dumps(dict_obj, indent=2))

# -----------------------------------------------------------------------------


def write_dict(dict_obj, file_name):
    ext = file_name.split('.').pop().lower()
    if ext in ['yaml', 'yml']:
        write_dict_as_yaml(dict_obj, file_name)
    elif ext == 'pfidb':
        write_dict_as_pfidb(dict_obj, file_name)
    elif ext == 'json':
        write_dict_as_json(dict_obj, file_name)
    else:
        print(f'Could not find writer for {file_name}')

# -----------------------------------------------------------------------------


def load_pfidb(file_path):
    result_dict = {}
    action = 'nb_lines'  # nbLines, size, string
    size = 0
    key = ''
    value = ''
    string_type_count = 0

    with open(file_path, 'r') as input_file:
        for line in input_file:
            if action == 'string':
                if string_type_count % 2 == 0:
                    key = line[:size]
                else:
                    value = line[:size]
                    result_dict[key] = value
                string_type_count += 1
                action = 'size'

            elif action == 'size':
                size = int(line)
                action = 'string'

            elif action == 'nb_lines':
                action = 'size'

    return result_dict

# -----------------------------------------------------------------------------


def sort_dict(input):
    output = {}
    keys = list(input.keys())
    keys.sort()
    for key in keys:
        output[key] = input[key]

    return output