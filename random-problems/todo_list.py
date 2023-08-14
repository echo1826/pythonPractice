def menuInput():
    menu_choice = input("Enter a command. Type 'h' for help:\n")
    return menu_choice

def main():
    menu_choice = menuInput()
    todo_list = []
    completed = []
    while True:
        if menu_choice == 'h':
            print("""
            TODO LIST HELP
            Type 'q' to quit
            To add a todo to the list, type it and hit enter
            To complete a todo enter its number""")
        elif menu_choice == 'q':
            print(f"You've completed {len(completed)} tasks today:")
            for i in range(len(completed)):
                print(f"* {completed[i]}")
            break
        elif menu_choice.isnumeric():
            if int(menu_choice) in range(len(todo_list) + 1):
                todo = todo_list.pop(int(menu_choice) - 1)
                completed.append(todo)
                for i in range(len(todo_list)):
                    print(f"{i+1}) {todo_list[i]}")
                
            else:
                print("Todo not found!")
            print("*" * 20)
        else:
            todo_list.append(menu_choice)
            for i in range(len(todo_list)):
                print(f"{i+1}) {todo_list[i]}")
            print("*" * 20)
        menu_choice = menuInput()

main()
