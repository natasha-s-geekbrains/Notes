def print_notes():
    print("Список всех заметок:\n")
    with open("notes_file.txt", encoding="utf-8") as file:
        for line in file:
            print(
                f'ID: {line.split(";")[0]}; '
                f'[{line.split(";")[1]}]; '
                f'Заметка: {line.split(";")[2]}; '
                f'Сохранена: {line.split(";")[3]}'
            )
