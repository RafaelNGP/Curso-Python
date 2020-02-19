import os
from os import path
import datetime
import time


def main():
    print(os.name)
    print(f"Item exists: {path.exists('texto.txt')}")
    print(f"Item is a file: {path.isfile('texto.txt')}")
    print(f"Item is a directory: {path.isdir('texto.txt')}")
    print(f"Item Path: {path.realpath('texto.txt')}")
    print(f"Item path and name: {path.split(path.realpath('texto.txt'))}")

    t = time.ctime(path.getmtime("texto.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime('texto.txt')))

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("texto.txt"))
    print(f"It has been {td} since the file was modified")
    print(f"Or, {str(td.total_seconds())} seconds ")


if __name__ == '__main__':
    main()
