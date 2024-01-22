import datetime
from get_file_lines import get_file_lines


def find_date():
    string_date = input("\nВведите дату в формате dd/MM/yyyy: \n")
    user_date = datetime.datetime.strptime(string_date, "%d/%m/%Y").date()

    with open(f"notes_file.txt", "r", encoding="utf-8") as file:
        sum=0
        for line in file:
            line = line.rstrip("\n")
            line_date = datetime.datetime.strptime(
                line.split(";")[3], "%d.%m.%Y %H:%M:%S"
            ).date()
            if line_date == user_date:
                print(line)
            else:
                sum += 1
        print(sum)
