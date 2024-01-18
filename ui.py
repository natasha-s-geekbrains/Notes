def start_menu():
    command = None
    while command !=6:
        command = int(input("Здравствуйте! Вы находитесь в приложении по управлению заметками!\n"
                            "Выберите, что вы хотите сделать:\n"
                            "1. Создать заметку\n"
                            "2. Вывести все заметки\n"
                            "3. Редактировать заметку\n"
                            "4. Выйти из приложения\n"
                            "Введите номер выбранной команды: "))
        comand=check_command_num(command)

    return n

def check_command_num(n):
    return n
