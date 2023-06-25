import os
from typing import List
from zipfile import ZipFile


def check_extension(file_name: str) -> str:
    """
    Checks file extension and returns it.
    :param file_name: name of the file with extension
    :exception ValueError: if the file has an extension that the program does not work with, it raises ValueError.
    :return: extension name
    """

    if file_name.endswith('.zip'):
        return 'zip'
    elif file_name.endswith('.txt'):
        return 'txt'
    raise ValueError


def convert_folders_path_to_str(dirs_lst: List[str]) -> str:
    """
    Converts a path consisting of a list of folders to a string.
    :param dirs_lst: path of a list of folders
    :return: path of a string
    """

    dirs_str: str = os.path.abspath(os.path.join(os.path.sep))
    for i_dir in dirs_lst:
        folder_path: str = os.path.join(dirs_str, os.path.join(i_dir))
        dirs_str: str = folder_path

    return dirs_str


def find_file(curr_path: str, file_name: str) -> str:
    """
    Searches for the specified file by the path passed by the user.
    :param curr_path: path passed by the user
    :param file_name: file to search
    :exception FileNotFound: if the file is not found an exception is raises
    :return: path to file
    """

    for elem in os.listdir(curr_path):
        if file_name == elem:
            path: str = os.path.join(curr_path, elem)
            return path
    raise FileNotFoundError


def unzip_file(file_path: str) -> str:
    """
    Extracts the file in the format .txt from the archive and returns the name of .txt file.
    :param file_path: name of the zip file without the extension
    :return: the name of the extracted file with the extension .txt
    """

    with ZipFile(file_path, mode='r') as zip_file:
        for i_file in zip_file.filelist:
            if i_file.filename.endswith('.txt'):
                txt_file_name = i_file.filename
                zip_file.extractall(members=[i_file])
                break

        return txt_file_name


def read_file(txt_file: str) -> str:
    """
    Reads the file, saves it to a variable and returns the variable.
    :param txt_file: the name of the file to be read
    :return: a variable containing the contents of the file
    """

    with open(f'{txt_file}', 'r', encoding='windows-1251') as file:
        text_: str = file.read()

    return text_
