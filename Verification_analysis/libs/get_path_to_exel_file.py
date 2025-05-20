import os


def get_number_of_files_in_directory_exel_file():
    directory_path = "exel_file"
    # Проверяем существование каталога
    if not os.path.exists(directory_path):
        print("Указанный каталог не существует")
        return

    # Получаем список всех файлов в каталоге
    files = os.listdir(directory_path)
    return len(files)


def get_path_to_exel_file(file):
    directory_path = "exel_file"
    # Проверяем существование каталога
    if not os.path.exists(directory_path):
        print("Указанный каталог не существует")
        return

    # Получаем список всех файлов в каталоге
    files = os.listdir(directory_path)

    # Фильтруем только Excel файлы
    excel_files = [f for f in files if f.lower().endswith('.xlsx')]

    if not excel_files:
        print("В каталоге нет .xlsx файлов")
        return

    # Выбираем первый найденный Excel файл
    excel_file = excel_files[file]
    file_path = os.path.join(directory_path, excel_file)
    return file_path


def get_device_type(number_of_file):
    directory_path = "exel_file"
    # Проверяем существование каталога
    if not os.path.exists(directory_path):
        print("Указанный каталог не существует")
        return

    # Получаем список всех файлов в каталоге
    files = os.listdir(directory_path)

    # Фильтруем только Excel файлы
    excel_files = [f for f in files if f.lower().endswith('.xlsx')]

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
        exit()
