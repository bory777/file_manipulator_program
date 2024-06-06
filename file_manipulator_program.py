import os
import sys

inputpath = input('入力ファイル名を入力してください\n')
if not os.path.exists(inputpath):
    print(f'{inputpath}は存在しません')
    sys.exit(1)
outputpath = input('出力ファイルを入力してください\n')

n = int(input('入力ファイルを複製する回数を入力してください\n'))

needle = input('置換したい文字を入力してください\n')
newstring = input('置換後の新しい文字列を入力してください\n')

# 入力ファイルの読み込みを抽象化
def read_file(in_file):
    try:
        with open(in_file, 'r', encoding = 'utf-8') as input_file:
            return input_file.read()
    except IOError:
        print(f'{in_file}の読み込み中にエラーが発生しました')
        return None

    
# ファイルへの書き込みを抽象化
def write_file(file_path, contents):
    try:
        with open(file_path, 'w', encoding = 'utf-8') as file:
            file.write(contents)
    except IOError:
        print(f'{file_path}の書き込み中にエラーが発生しました')


# 入力ファイルの内容を逆にして出力ファイルを作成する
def reverse(inputpath, outputpath):
    contents = read_file(inputpath)
    if contents is not None:
        reversed_contents = contents[::-1]
        write_file(outputpath, reversed_contents)
        print(f'{inputpath}の内容を逆にし、{outputpath}に保存。')


# 入力ファイルの内容をコピーし、出力ファイルを作成する
def copy (inputpath, outputpath):
    contents = read_file(inputpath)
    if contents is not None:
        write_file(outputpath, contents)
        print(f'{inputpath}の内容をコピーし、{outputpath}に保存。')


# 入力ファイルの内容を複製しn回入力ファイルに複製する
def duplicate_contents (inputpath, n):
    contents = read_file(inputpath)
    if contents is not None:
        duplicate = contents * n
        write_file(inputpath, duplicate)
        print(f'{inputpath}の内容を{n}回コピーして複製しました')


# needleをnewstringに置き換えてファイルを保存する
def replace_string(inputpath, needle, newstring):
    contents =  read_file(inputpath)
    if contents is not None:
        new_contents = contents.replace(needle, newstring)
        write_file(inputpath, new_contents)
        print (f'{inputpath}の内容の{needle}を{newstring}に変えました')


reverse(inputpath, outputpath)
copy(inputpath, outputpath)
duplicate_contents(inputpath, n)
replace_string(inputpath, needle, newstring)
