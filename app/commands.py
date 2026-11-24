import shlex

# command name mapped to the number of parameters required
command_specifications = {
    "Add": 2,
    "List": 0,
    "Show": 1,
    "Search": 1,
    "Delete": 1
}


def tokenize_input(input_text):
    return [token.strip() for token in shlex.split(input_text)]


def validate_command(tokens):
    if len(tokens) == 0:
        return "Missing command!"

    tokens[0].capitalize()
    command_name = tokens[0]
    required_parameters_count = command_specifications.get(command_name)

    if required_parameters_count is None:
        return f"{command_name} is not a valid command!"

    provided_parameters_count = len(tokens) - 1

    if required_parameters_count != provided_parameters_count:
        return f"{command_name} requires exactly {required_parameters_count}!"

    return None

def execute_command(input_text):
    tokens = tokenize_input(input_text)
    validation_error = validate_command(tokens)

    if validation_error is not None:
        print(validation_error)
        return


