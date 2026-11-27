import pytest

from app import store


@pytest.fixture(autouse=True)
def reset_store():
    store.title_to_contents.clear()
    store.id_to_title.clear()
    store.set_last_used_title_id(-1)
