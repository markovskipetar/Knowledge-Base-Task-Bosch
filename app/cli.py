def main():
    while True:
        command = input("$ knowledge> ")

        if command.strip().lower() == "exit":
            return

        print(f"Typed: {command}")