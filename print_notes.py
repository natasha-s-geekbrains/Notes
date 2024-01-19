def print_notes():
    print("Список всех заметок:")
    with open("notes_file.txt") as file:
        for line in file:
            print(line)
    print()

