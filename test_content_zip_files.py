import time
from selene import browser, be, have
from pypdf import PdfReader
from download_file import CURRENT_DIR

import os
import zipfile

resource_dir = os.path.join(CURRENT_DIR, "resource", "test.zip")


def test_create_archive_1(download_pack_files):
    file_size = os.path.getsize(resource_dir)
    assert file_size == 1175998
    with zipfile.ZipFile(resource_dir, "r") as myzip:
        assert len(myzip.infolist()) == 3


def test_package_pdf_2(download_pack_files):
    with zipfile.ZipFile(resource_dir, "r") as myzip:
        with myzip.open('files/examplePdf.pdf') as myfile:
            reader = PdfReader(myfile)
            assert "рисунки" in reader.pages[1].extract_text()
            assert len(reader.pages) == 59
