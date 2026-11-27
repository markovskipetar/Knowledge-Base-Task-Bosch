from app.commands import execute_command
from app import serialization

def load_knowledge_base():
    try:
        serialization.load()
    except (OSError, ValueError) as error:
        print(f"Could not load knowledge base: {error}")
        return False

    return True


def save_knowledge_base():
    try:
        serialization.save()
    except OSError as error:
        print(f"Could not save knowledge base: {error}")
        return False

    return True


def main():
    if not load_knowledge_base():
        return 1

    while True:
        try:
            input_text = input("$ knowledge> ")
            if execute_command(input_text):
                break
        except (EOFError, KeyboardInterrupt):
            print()
            break

    if not save_knowledge_base():
        return 1

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
