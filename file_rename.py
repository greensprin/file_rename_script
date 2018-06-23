# coding=utf-8

import os
import sys

argvs = sys.argv

def search_path(path, fname, frename):
    flists = os.listdir(path)
    # ファイルかディレクトリを判断
    for flist in flists:
        print(flist)
        filename, ext = os.path.splitext(flist)
        if ext == ".txt" :
            print("this is file")
            file_rename(path, flist, fname, frename)
        else:
            print("this is dir")
            cul_dir = path
            path = path + "\\" + flist
            search_path(path, fname, frename)
            path = cul_dir


def file_rename(path, flist, fname, frename):
    frnlist = flist.replace(fname, frename)
    f_base_name = path + "\\" + flist
    f_replace_name = path + "\\" + frnlist
    os.rename(f_base_name, f_replace_name)

if __name__ == '__main__':
    path = argvs[1]
    fname = argvs[2]
    frename = argvs[3]
    search_path(path, fname, frename)
