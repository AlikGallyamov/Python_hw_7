import os
from zipfile import ZipFile

CURRENT_PATH = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_PATH)


# def generated_list():
#     """
#     Генерируем список с фильтрацией по формату файла
#     """
#     return [file_name for file_name in os.listdir(CURRENT_DIR) if
#             file_name.endswith(".csv") or file_name.endswith(".pdf") or file_name.endswith(".xlsx")]
#
#
# def file_add_in_archive(archive_name: str):
#     """
#     archive_name: имя создаваемого архива.
#     Вызываем метод геренации списка имён текущей директории.
#     Вернувшийся список упаковываем в zip архив
#     """
#     list_with_file_name = generated_list()
#
#     for file_name in list_with_file_name:
#         with ZipFile(str(archive_name) + ".zip", "a") as zf:
#             zf.write(file_name)
#
#
# file_add_in_archive("archive")

def read_content():
    with ZipFile("archive.zip", "r") as zf:
        content = zf.read("hello5.txt")
        print(content)