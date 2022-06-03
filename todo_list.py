def menuInput():
    menu_choice = input("Enter a command. Type 'h' for help:\n")
    return menu_choice

def main():
    menu_choice = menuInput()
    todo_list = []
    while True:
        if menu_choice == 'h':
            print("""
            TODO LIST HELP
            Type 'q' to quit
            To add a todo to the list, type it and hit enter
            To complete a todo enter its number""")
        elif menu_choice == 'q':
            break
        else:
            todo_list.append(menu_choice)
            for i in range(len(todo_list)):
                print(f"{i+1}) {todo_list[i]}")
        menu_choice = menuInput()

main()
