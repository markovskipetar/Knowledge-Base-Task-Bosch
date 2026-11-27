import re
import shlex
from app import store

# command name mapped to the number of parameters required
command_specifications = {
    "Add": 2,
    "List": 0,
    "Show": 1,
    "Search": 1,
    "Delete": 1,
    "Exit": 0
}


def tokenize_input(input_text):
    return [token.strip() for token in shlex.split(input_text)]


def validate_command(tokens):
    if len(tokens) == 0:
        return "Missing command!"

    tokens[0] = tokens[0].capitalize()
    command_name = tokens[0]
    required_parameters_count = command_specifications.get(command_name)

    if required_parameters_count is None:
        return f"{command_name} is not a valid command!"

    provided_parameters_count = len(tokens) - 1

    if required_parameters_count != provided_parameters_count:
        return f"{command_name} requires exactly {required_parameters_count} parameters!"

    return None


def add(parameters):
    title = parameters[0]
    content = parameters[1]

    error = store.add(title, content)
    if error is not None:
        print(error)


# intentionally passing parameters so I can call all function the same way
def list_all(parameters):
    ids_and_titles = store.get_all_ids_and_titles()

    for title_id, title in ids_and_titles:
        print(f"{title_id} | {title}")


def parse_id(value):
    try:
        title_id = int(value)
    except ValueError:
        print("ID must be an integer.")
        return

    if title_id < 0:
        print("ID cannot be negative.")
        return

    return title_id


def show(parameters):
    title_id = parse_id(parameters[0])

    if title_id is None:
        return

    title_and_its_contents = store.get_title_and_its_contents(title_id)

    title = title_and_its_contents[0]
    contents = title_and_its_contents[1]

    if title is None:
        print(f"No entry found with ID {title_id}.")
        return

    print(f"{title}:")

    for content in contents:
        print(f" - {content}")


def print_highlighted_matches(matches, searched_word):
    pattern = re.compile(re.escape(searched_word), re.IGNORECASE)
    print(f'Matches for "{searched_word}":')

    for text in matches:
        highlighted_match = pattern.sub(lambda match: f"[{match.group()}]", text)
        print(f"  - {highlighted_match}")


def search(parameters):
    searched_word = parameters[0]

    if not searched_word:
        print("Search text cannot be empty.")
        return

    matches = store.search_in_all(searched_word)

    if not matches:
        print(f'No matches found for "{searched_word}".')
        return

    print_highlighted_matches(matches, searched_word)


def delete(parameters):
    id_to_delete = parse_id(parameters[0])

    if id_to_delete is None:
        return

    error = store.delete(id_to_delete)

    if error is not None:
        print(error)


def exit_command(parameters):
    return True


command_to_function = {
    "Add": add,
    "List": list_all,
    "Show": show,
    "Search": search,
    "Delete": delete,
    "Exit": exit_command
}


def execute_command(input_text):
    try:
        tokens = tokenize_input(input_text)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    validation_error = validate_command(tokens)

    if validation_error is not None:
        print(validation_error)
        return

    command_name = tokens[0]
    parameters = tokens[1:]

    function_for_command = command_to_function.get(command_name)
    return function_for_command(parameters)
