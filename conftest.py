import os
import pytest
import download_file

CURRENT_PATH = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_PATH)


@pytest.fixture()
def download_pack_files():
    print("Запускаю загрузку")
    download_file.download_csv()
    print("Загружен файл 1")
    download_file.download_pdf()
    print("Загружен файл 2")
    download_file.download_xlsx()
    print("Загружен файл 3")
    download_file.create_zip_files()

    yield

    os.rmdir("files")
    os.rmdir("resource")
