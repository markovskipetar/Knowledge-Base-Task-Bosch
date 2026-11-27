## Setup

1. Download or clone the repository and open the main folder containing `pyproject.toml` in a terminal.

2. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

3. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   # You should see (.venv) at the beginning of the prompt.
   ```

4. Install the `knowledge` command:

   ```powershell
   python -m pip install -e '.[test]'
   ```

5. Start the app:

   ```powershell
   knowledge
   ```

Activate the virtual environment again whenever you open a new terminal. To leave it, run `deactivate` after exiting the app.

## Saving and loading data

When the app starts, it reads `knowledge.json` and loads its saved entries into memory. If the file does not exist or is empty, the app starts with an empty knowledge base.

When you enter `exit`, press Ctrl+C, or press Ctrl+Z followed by Enter, the app saves the entries and the last used ID to `knowledge.json` before closing. The next time you start the app, it loads that data again.

## Example

Type commands after the `$ knowledge>` prompt. Put titles or content containing spaces in quotes.

```text
$ knowledge> add Python "Hello this is Python"
$ knowledge> add Python "Another note"
$ knowledge> list
0 | Python
$ knowledge> show 0
Python:
 - Hello this is Python
 - Another note
$ knowledge> search this
Matches for "this":
  - Hello [this] is Python
$ knowledge> delete 0
$ knowledge> exit
```

| Command | What it does |
| --- | --- |
| `add "title" "content"` | Adds a title and note. Using an existing title adds another note to it. |
| `list` | Shows all IDs and titles. |
| `show 0` | Shows the title and notes for ID `0`. |
| `search "text"` | Searches titles and notes, ignoring letter case. |
| `delete 0` | Deletes ID `0` and all its notes. |
| `exit` | Saves and closes the app. Ctrl+C also saves and exits. |

## Run the tests

From the project folder, with the virtual environment activated and the project installed as shown above, run:

```powershell
python -m pytest -v
```
