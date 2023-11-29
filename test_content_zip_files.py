import time

from selene import browser, be, have
from pypdf import PdfReader
from download_file import CURRENT_DIR

import os
import zipfile


def test_create_archive(download_pack_files):
    resource_dir = os.path.join(CURRENT_DIR, "resource", "test.zip")
    file_size = os.path.getsize(resource_dir)
    assert file_size == 1175998
    with zipfile.ZipFile(resource_dir, "r") as myzip:
        assert len(myzip.infolist()) == 3
