import os
import re
import sys


def change_name(name):
    name = re.sub(r"\s+", " ", name)
    name = re.sub(r"\.\s+", ".", name)
    name = re.sub(r"\s+\.", ".", name)
    name = name.strip()
    return name


def duplicate_name(name):
    c = 1
    name_ = name
    while True:

        file_path = os.path.join(dir_path, name_)
        if os.path.exists(file_path):
            name_ = f"{'_' * c}{name}"
            c += 1
        else:
            break

    return name_


def rename(file_name, new_name):
    file_name = os.path.join(dir_path, file_name)
    new_name = os.path.join(dir_path, new_name)

    os.rename(file_name, new_name)


def check_dir_path(dir_path):
    if not os.path.exists(dir_path):
        print("Invalid path: {dir_path} does not exist")
        return False
    if not os.path.isdir(dir_path):
        print("Invalid path: {dir_path} is not a directory")
        return False
    return True


dir_paths = []
if __name__ == "__main__":

    if len(sys.argv) == 1:

        dir_path = input("Enter the directory path: ")
        if check_dir_path(dir_path):
            dir_paths.append(dir_path)
    else:

        for i in sys.argv[1:]:
            if check_dir_path(i):
                dir_paths.append(i)
    for dir_path in dir_paths:

        for file_name in os.listdir(dir_path):
            if os.path.isdir(os.path.join(dir_path, file_name)):
                continue
            new_name = change_name(file_name)
            if new_name != file_name:
                new_name = duplicate_name(new_name)
                rename(file_name, new_name)
                print(f"{file_name} -> {new_name}")
        else:
            print(f"Done({dir_path})...")
