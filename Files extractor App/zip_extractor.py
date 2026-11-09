import zipfile


def archive(archive_filepath, dest_dir):
    with zipfile.ZipFile(archive_filepath,'r') as arhive:
        arhive.extractall(dest_dir)

if __name__=="__main__":
    archive('compressed.zip','E:\EXL - online training\python mega course - udemy\Files extractor App')