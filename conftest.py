import os

import pytest
import packing_files
import download_file

CURRENT_PATH = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_PATH)


@pytest.fixture()
def download_pack_files():
    download_file.download_csv()
    download_file.download_pdf()
    download_file.download_xlsx()
    packing_files.create_zip_files()

    yield

    os.rmdir("files")
    os.rmdir("resource")
