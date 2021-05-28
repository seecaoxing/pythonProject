import os
import shutil

# 修改所有资源图片
def replace_drawable(self):
    # 替换掉所有类型的mipmap包下的文件
    print
    "开始替换图片资源..."
    for pr in project_drawable:
        targetfile = self.search_drawable_in_local(project_drawable[pr])
        if targetfile is not None:
            # 递归查找
            # (filename,extension) = os.path.splitext(targetfile)
            targetdir = local_config[
                            "local_drawable_path"] + "/" + targetfile
            print
            "将替换的图片资源: %s " % (targetdir)
            self.search_drawable_in_project(
                local_config["drawable_path"], targetdir)
    print
    "图片资源替换完成."
    pass


# 递归替换项目中的资源
def search_drawable_in_project(self, sourcedir, targetdir):
    if sourcedir.find(".git") >= 0:
        return
    # print sourcedir
    if os.path.isdir(sourcedir):
        # 是文件夹，检索文件夹内文件递归
        listdir = os.listdir(sourcedir)
        for ld in listdir:
            if os.path.isdir(ld) and ld.find("mipmap") < 0:
                continue
            path = sourcedir + "/" + ld
            self.search_drawable_in_project(path, targetdir)
    else:
        # 是文件,判断是否是要复制的文件
        splitl = os.path.split(sourcedir)
        targetl = os.path.split(targetdir)
        # print "src: "+splitl[1]+" tar: "+targetl[1]
        if os.path.isfile(sourcedir) and targetl[1] == splitl[1]:
            shutil.copy(targetdir, sourcedir)
        return
    pass


# 查找本地资源文件(一级目录)
def search_drawable_in_local(self, source_id):
    (sourcename, srextension) = os.path.splitext(source_id)
    path = local_config["local_drawable_path"]
    if os.path.isdir(path):
        # 根据要替换的文件名找到新文件并返回
        listfile = os.listdir(path)
        for file in listfile:
            # ic_launcher.png
            (filename, extension) = os.path.splitext(file)
            if filename == sourcename:
                return file
    else:
        # 本地资源路径非文件夹
        return
    pass
