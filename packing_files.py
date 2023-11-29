import zipfile, os
import download_file


def create_zip_files():
    """

    """
    with zipfile.ZipFile(download_file.resource_dir + '/test.zip', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in download_file.files_name:
            add_file = os.path.join("files", file)
            print(add_file)
            zf.write(add_file)



