import os
import re

def get_files():
    startPath = "./changelogs/base/"

    fileArr = []

    fileList = os.walk(startPath)
    for root, subdirs, files in fileList:
        for fileName in files:
            if fileName != []:
                endFile = os.path.join(root, fileName)
                fileArr.append(endFile)

    return fileArr

def main():
    endpath = "./changelogs/compiled/"

    #fileList = get_files()
    fileList = ["changelogs/base/connectors/rust-connectors/sources/http/CHANGELOG.md"]
    for files in fileList:
        newFile = endpath + files[16:]
        with open(files, 'r') as fileDescriptor,\
             open(newFile, "w") as newFileDescriptor:
            print(f"## changelog\n\n| Version | Date       | PR                                                               | Subject                                           |", file=newFileDescriptor)
            print(f"|:-------:|:----------:|:----------------------------------------------------------------:| ------------------------------------------------- |", file=newFileDescriptor)
            for line in fileDescriptor.readlines():
                line = str(line)
                if re.search( "##" , line):
                    print(line)
                else:
                    print("not here!")


if __name__ == "__main__": main()
