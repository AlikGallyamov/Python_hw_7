import zipfile, os

CURRENT_PATH = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_PATH)

source_dir = os.path.join(CURRENT_DIR, "files")
resource_dir = os.path.join(CURRENT_DIR, "resources")
files_name = os.listdir(source_dir)


def create_zip_files():
    """

    """
    with zipfile.ZipFile(resource_dir + '/test.zip', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in files_name:
            add_file = os.path.join("files", file)
            zf.write(add_file)
