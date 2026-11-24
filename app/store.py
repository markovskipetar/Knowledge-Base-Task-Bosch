title_to_contents: dict[str, list[str]] = {}
id_to_title: dict[int, str] = {}

title_id = -1  # this id must be reloaded when reading the json data from storage


def set_last_used_id(last_used_id):
    global title_id
    title_id = last_used_id


def get_next_available_id():
    global title_id
    title_id = title_id + 1
    return title_id


def add(title, content):
    if len(title) == 0:
        return "Title is empty"

    if len(content) == 0:
        return "Content is empty"

    contents = title_to_contents.get(title)

    if contents is not None:  # title already exist
        contents.append(content)
        return None

    new_id = get_next_available_id()
    id_to_title[new_id] = title
    title_to_contents[title].insert(content)
    return None
