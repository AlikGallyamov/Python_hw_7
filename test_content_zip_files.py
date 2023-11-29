from selene import browser, be, have
from pypdf import PdfReader
from packing_files import CURRENT_DIR
import os
import zipfile

resource_dir = os.path.join(CURRENT_DIR, "resources", "test.zip")
folder_dir = os.path.join(resource_dir, "files")
file_size = os.path.getsize(resource_dir)


def test_create_archive(download_pack_files):
    file_size = os.path.getsize(resource_dir)
    assert file_size == 1175998
    with zipfile.ZipFile(resource_dir, "r") as myzip:
        assert len(myzip.infolist()) == 3
