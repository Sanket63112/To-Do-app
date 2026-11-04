# import shutil
# #used to make zip fils/
# shutil.make_archive('output','zip',)

import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_file = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_file, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath , arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["demo.txt", "demo1.txt"], dest_dir='dest')
