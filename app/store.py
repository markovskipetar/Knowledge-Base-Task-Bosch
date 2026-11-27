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


def delete(id_to_delete):
    title = id_to_title.get(id_to_delete)

    if title is None:
        return f"No entry found with ID {id_to_delete}."

    del id_to_title[id_to_delete]
    del title_to_contents[title]

    return None


def search_in_all(searched_word):
    if not searched_word:
        return []

    searched_word = searched_word.lower()
    matches = []
    
    for title, contents in title_to_contents.items():
        if searched_word in title.lower():
            matches.append(title)

        matches.extend(content for content in contents if searched_word in content.lower())

    return matches


def get_title_and_its_contents(title_id):
    title = id_to_title.get(title_id)

    if title is None:
        return None, None

    contents = title_to_contents.get(title)
    return title, contents
