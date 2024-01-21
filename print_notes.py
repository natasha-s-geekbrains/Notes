from check_file_exists import check_file_exists


def print_notes():
    file_path = check_file_exists()
    if file_path == None:
        print("\nСожалеем, но списка с заметками не существует!\n")
    else:
        with open("notes_file.txt", "r", encoding="utf-8") as file:
            lines_qty = len(file.readlines())
            if lines_qty == 0:
                print("\nСожалеем, но в списке нет заметок.\n")
            else:
                print("\nСписок всех заметок:\n")
                with open("notes_file.txt", "r", encoding="utf-8") as file:
                    for line in file:
                        print(
                            f'ID: {line.split(";")[0]}; '
                            f'Заголовок: {line.split(";")[1]}; '
                            f'Заметка: {line.split(";")[2]}; '
                            f'Сохранена: {line.split(";")[3]}'
                        )
