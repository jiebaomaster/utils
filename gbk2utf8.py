#coding=utf-8
import io
import os


def get_file_path(root_path, file_list, dir_list):
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path, dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            if dir_file_path in ignore_list:
                continue

            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_file_path(dir_file_path, file_list, dir_list)
        else:
            if dir_file_path in ignore_list:
                continue

            file_list.append(dir_file_path)
            print(dir_file_path)
            try:  # 过滤所有类型的错误，执行能够转换的
              # 以 gbk 格式打开并写入到一个新的 utf-8 格式的文件中
              io.open(dir_file_path + '__tmp', "w",
                      encoding="utf-8").write(io.open(dir_file_path, encoding="gbk").read())
              # 文件重命名
              os.remove(dir_file_path)
              os.rename(dir_file_path + '__tmp', dir_file_path)
            except:
              print("error read file: " + dir_file_path + ' \n')


if __name__ == "__main__":
    # 递归遍历 root_path 目录下的所有 gbk 格式的文件，将其转码为 utf-8 格式
    # 遍历的根目录
    root_path = r""
    # 用来存放所有的文件路径
    file_list = []
    #用来存放所有的目录路径
    dir_list = []
    # 不想转码的文件，目录，如 .git 目录
    ignore_list = []
    get_file_path(root_path, file_list, dir_list)
    print(file_list)
    print(len(file_list))
