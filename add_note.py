import datetime


def add_note():
    note_title = input("Введите заголовок заметки и нажмите клавишу Enter: ")
    note_text = input("Введите текст заметки и нажмите клавишу Enter: ")
    storage_date_time = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    with open("notes_file.txt", "a", encoding="utf-8") as file:
        file.write(f"{note_title};{note_text};{storage_date_time}\n")

    print("Заметка успешно сохранена!")
    print()
