import os
import shutil

import pytest
import download_file

CURRENT_PATH = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_PATH)


@pytest.fixture()
def download_pack_files():
    os.mkdir("files")
    os.mkdir("resource")
    download_file.download_csv()
    download_file.download_pdf()
    download_file.download_xlsx()
    download_file.create_zip_files()

    yield

    shutil.rmtree(os.path.join(CURRENT_DIR, "files"))
    shutil.rmtree(os.path.join(CURRENT_DIR, "resource"))
