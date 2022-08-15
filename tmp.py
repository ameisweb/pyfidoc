import shutil, os


path_source = "C:/Users/work/Documents/test_files/"
dir_path = path_source + "documentations/"

def delete_make_dir(path_source):
    dir_path = path_source + "documentations/"
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        pass

    while True:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if os.path.exists(dir_path):
            break

delete_make_dir(path_source)