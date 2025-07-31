import datetime
import os
import shutil

import xlwings

from libs.all_data_object import PathToFile


def check_folder():
    # if not os.path.exists(output_folder):
    # PathToFile.output_folder = "Проверенные файлы" + "_" + str(datetime.datetime.now().strftime("%d.%m.%y_%H.%M"))
    # output_folder = PathToFile.output_folder
    # os.makedirs(output_folder)

    directory_path = PathToFile.output_folder
    # Проверяем существование каталога
    if not os.path.exists(directory_path):
        print("Указанный каталог не существует")
        return False

    # Получаем список всех файлов в каталоге
    files = os.listdir(directory_path)

    # Фильтруем только Excel файлы
    excel_files = [f for f in files if f.lower().endswith(('.xlsx', '.xls'))]

    if len(excel_files) == 0:
        return 1
    for i in excel_files:
        if all(substring not in i for substring in ["1ф", "3ф", "ТТ"]):
            return 2
    return 0


def convert_folder():
    output_folder = PathToFile.output_folder
    for file in os.listdir(output_folder):
        if file.lower().endswith('.xls'):
            input_path = os.path.join(output_folder, file)
            output_path = os.path.join(output_folder, file.replace('.xls', '.xlsx'))

            try:
                app = xlwings.App(visible=False)
                wb = app.books.open(input_path)
                wb.save(output_path)
                wb.close()
                app.quit()
                print(f"Конвертирован: {file}")
                os.remove(input_path)
            except Exception as e:
                print(f"Ошибка при конвертации {file}: {str(e)}")


def get_number_of_files_in_directory_exel_file():
    output_folder = PathToFile.output_folder
    directory_path = output_folder
    # Проверяем существование каталога
    if not os.path.exists(directory_path):
        print("Указанный каталог не существует")
        return 0

    # Получаем список всех файлов в каталоге
    files = os.listdir(directory_path)
    return len(files)


def get_path_to_exel_file(file):
    output_folder = PathToFile.output_folder
    directory_path = output_folder
    # Проверяем существование каталога
    if not os.path.exists(directory_path):
        print("Указанный каталог не существует")
        return False

    # Получаем список всех файлов в каталоге
    files = os.listdir(directory_path)

    # Фильтруем только Excel файлы
    excel_files = [f for f in files if f.lower().endswith(('.xlsx', '.xls'))]

    if len(excel_files) == 0:
        return 0
    for i in excel_files:
        if all(substring not in i for substring in ["1ф", "3ф", "ТТ"]):
            return 0

    # Выбираем первый найденный Excel файл
    excel_file = excel_files[file]
    file_path = os.path.join(directory_path, excel_file)
    return file_path


def get_device_type(number_of_file):
    output_folder = PathToFile.output_folder
    directory_path = output_folder
    # Проверяем существование каталога
    if not os.path.exists(directory_path):
        print("Указанный каталог не существует")
        return

    # Получаем список всех файлов в каталоге
    files = os.listdir(directory_path)

    # Фильтруем только Excel файлы
    excel_files = [f for f in files if f.lower().endswith(('.xlsx', '.xls'))]

    if not excel_files:
        print("В каталоге нет .xlsx файлов")
        return

    # Выбираем первый найденный Excel файл
    excel_file = excel_files[number_of_file]

    if "1ф" in excel_file:
        return "1PH"
    elif "3ф" in excel_file:
        return "3PH"
    elif "ТТ" in excel_file:
        return "TT"
    else:
        print("Нетипичное имя файла, файл должен содержать '1ф', '3ф' или 'ТТ' символами кириллицы")
        return
