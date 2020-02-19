import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    if path.exists("texto.txt"):
        src = path.realpath('texto.txt')
        dst = src + ".bak"

    # criar backup
    # shutil.copy(src, dst)
    # shutil.copystat(src, dst)

    # renomeando
    # os.rename("texto.txt", "novotexto.txt")

    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("texto.txt")
        newzip.write("texto.txt.bak")


if __name__ == '__main__':
    main()
