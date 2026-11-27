title_to_contents: dict[str, list[str]] = {}
id_to_title: dict[int, str] = {}

last_used_title_id = -1


def set_last_used_title_id(last_used_id):
    global last_used_title_id
    last_used_title_id = last_used_id


def get_next_available_id():
    global last_used_title_id
    last_used_title_id = last_used_title_id + 1
    return last_used_title_id


def add(title, content):
    if not title:
        return "Title is empty"

    if not content:
        return "Content is empty"

    contents = title_to_contents.get(title)

    if contents is not None:  # title already exist
        contents.append(content)
        return None

    new_id = get_next_available_id()
    id_to_title[new_id] = title
    title_to_contents[title] = [content]
    return None


def get_all_ids_and_titles():
    return list(id_to_title.items())


