from app.commands import execute_command

def main():
    while True:
        input_text = input("$ knowledge> ")
        execute_command(input_text)