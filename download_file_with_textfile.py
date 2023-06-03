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



path_file = "Path txt file"
download_by_file(path_file)
