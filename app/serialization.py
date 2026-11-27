import json
from pathlib import Path

from app import store

DATA_FILE = Path("knowledge.json")


def load(path=DATA_FILE):
    try:
        with Path(path).open(encoding="utf-8") as file:
            file_content_as_text = file.read()
    except FileNotFoundError:
        return

    if not file_content_as_text.strip():  # empty file
        return

    from_json = json.loads(file_content_as_text)

    if from_json == {}:  # file content is "{}"
        return

    from_json["id_to_title"] = {
        int(entry_id): title for entry_id, title in from_json["id_to_title"].items()
    }
    check_titles_exist(from_json)
    update_store(from_json)


def check_titles_exist(from_json):
    id_to_title = from_json["id_to_title"]
    title_to_contents = from_json["title_to_contents"]

    for entry_id, title in id_to_title.items():
        if title not in title_to_contents:
            raise ValueError(f"Title {title!r} for ID {entry_id} is missing from title_to_contents.")


def update_store(from_json):
    store.title_to_contents.clear()
    store.title_to_contents.update(from_json["title_to_contents"])
    store.id_to_title.clear()
    store.id_to_title.update(from_json["id_to_title"])
    store.set_last_used_title_id(from_json["last_used_id"])


def save(path=DATA_FILE):
    data = {
        "last_used_id": store.last_used_title_id,
        "id_to_title": store.id_to_title,
        "title_to_contents": store.title_to_contents,
    }
    with Path(path).open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
