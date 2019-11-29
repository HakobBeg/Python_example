def show_menu():
    print("Available actions: \na - Add or update an item\nf - Search for an item\ns - Register a sale\nx - Exit\n")


def prompt_command():
    return input("Please type a command: ")

def add_item():
    pass
def find_item():
    item_id = input("Type item ID: ")

def add_sale():
    pass

def invoke_command(cmd: str):
    command = ['a','f','s','x']
    if not cmd in command:
        print("Invalid command. rTry again!")
        invoke_command(prompt_command())
    print('\n\n')


while True:
    show_menu()
    cmd = prompt_command()  # Get a command from input and validates it

    invoke_command(cmd)  # Runs a command

# DON'T DO THIS


