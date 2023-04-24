import os
import sys
import translators as ts
# pip install translators==5.7.0


def read_file(file_path: str) -> list:
    if os.path.exists(file_path):
        string_list = []
        with open(file_path, 'r', encoding="UTF-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    string_list.append(line)

        print("read file ...")
        return string_list
    else:
        print("File not found")
        return None


def translator(string_list: list) -> list:
    new_string_list = []
    for l in string_list:
        wyw_text = ts.translate_text(
            translator="google", query_text=l, from_language="en", to_language="fa")
        new_string_list.append(wyw_text)
    return new_string_list


def save_file(string_list: str, base_path: str, file_name: str = "new_file.txt") -> None:
    new_file_path = os.path.join(base_path, file_name)
    with open(new_file_path, 'w', encoding="UTF-8") as f:
        for l in string_list:
            f.writelines(l)
            f.writelines("\n")
    print("File saved")


def main():
    if len(sys.argv) == 2:
        file_name_save = "new_file.txt"
    elif len(sys.argv) == 3:
        file_name_save = sys.argv[2]
    else:
        print("python text_file_translator.py file_name [new_file_name]")
        return None

    file_path = sys.argv[1]
    base_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    string_list = read_file(file_path)

    if string_list:
        string_list = translator(string_list)
        save_file(string_list, base_path, file_name_save)


if __name__ == "__main__":
    main()
