from check_file_exists import check_file_exists


def change_note():
    file_path = check_file_exists()
    if file_path == None:
        print("Сожалеем, но списка с заметками не существует!\n")
    else:
        print("Заметка успешно изменена и сохранена!")
        print()
