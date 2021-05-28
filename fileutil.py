import os
import shutil


def get_fileList(dir):
    Filelist = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            # 文件名列表，包含完整路径
            if os.path.isfile(os.path.join(root, filename)):
                Filelist.append(os.path.join(root, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append(filename)
    return Filelist


# 递归替换项目中的资源
def search_drawable_in_project(sourcedir, targetdir):
    # print sourcedir
    if os.path.isdir(sourcedir):
        # 是文件夹，检索文件夹内文件递归
        listdir = os.listdir(sourcedir)
        for ld in listdir:
            path = sourcedir + "/" + ld
            search_drawable_in_project(path, targetdir)
    else:
        # 是文件,判断是否是要复制的文件
        print("正在对比文件")
        splitl = os.path.split(sourcedir)
        targetl = os.path.split(targetdir)
        # print "src: "+splitl[1]+" tar: "+targetl[1]
        if os.path.isfile(sourcedir) and targetl[1] == splitl[1]:
            print("正在替换")
            shutil.copy(targetdir, sourcedir)
        return
    pass


if __name__ == '__main__':
    for file in get_fileList("/Users/caoxing01/百度/ui/a"):
        print(file)
        search_drawable_in_project("/Users/caoxing01/百度/ui/b", file)
