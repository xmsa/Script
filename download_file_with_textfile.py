import requests
import os
import urllib.parse
import zipfile


def read_file(path_file):
    list_of_url = list()
    with open(path_file, "r") as f:
        list_of_url = f.readlines()
        list_of_url = list(map(str.strip, list_of_url))

    return list(set(list_of_url))


def download_by_url(url, dir_name):
    parsed = urllib.parse.urlparse(url)
    name = os.path.basename(parsed.path)
    response = requests.get(url)
    path_file = os.path.join(dir_name, name)
    if response.status_code == 200:
        with open(path_file, "wb") as f:
            f.write(response.content)
        return path_file
    else:
        print(f"Error: {url}")
        return None


def download_by_file(path_file, compressing_files=True, zipname="archive.zip"):
    list_of_url = read_file(path_file)
    dir_name = os.path.dirname(path_file)
    file_download = []
    for url in list_of_url:
        path_file = download_by_url(url, dir_name)

        if path_file:
            file_download.append(path_file)

    print(file_download)
    zip_files(file_download, zipname)


def zip_files(file_list, zipname):
    zipf = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    for file in file_list:
        zipf.write(file)
    zipf.close()


def print_diss():
    print("python download_file_with_textfile.py [-s] input")

    print("       input: file_name.txt or url")
    print("       -s: if input == file_name.txt then compress all file download in zip file")


def main():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".txt"):
        if sys.argv[1].endswith(".txt"):

            path_file = sys.argv[1]
            download_by_file(path_file, compressing_files=False)
            
        else:
            url = sys.argv[1]
            download_by_url(url, os.path.dirname(__file__))
            
        return None
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-s" and sys.argv[2].endswith(".txt"):
            download_by_file(path_file, compressing_files=True)
            return None
    print_diss()


if __name__ == "__main__":
    main()
