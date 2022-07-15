import os

def get_files():
    startPath = "./changelogs/base/"

    fileArr = []

    fileList = os.walk(startPath)
    # collects ALL files in changelog/base and makes 1 list out of them
    for root, subdirs, files in fileList:
        for fileName in files:
            if fileName != []:
                endFile = os.path.join(root, fileName)
                fileArr.append(endFile)

    return fileArr

def generate_table(files, newFile):
    # main meat of the operation
    # opens both files, generates the table, and dumbs to newFile
    with open(files, 'r') as fileDescriptor,\
         open(newFile, "w") as newFileDescriptor:
        print(f"## changelog\n\n| Version | Date       | PR                                                               | Subject                                           |", file=newFileDescriptor)
        versionField = ""
        dateField = ""
        prField = ""
        commentField = ""
        print(f"|:-------:|:----------:|:----------------------------------------------------------------:| ------------------------------------------------- |", file=newFileDescriptor)
        # generating the individual lines for the table
        for line in fileDescriptor.readlines():
            line = str(line).replace('\n','').split(' ')
            if "##" in line:
                # getting the version and date info -- resetting the pr and comment fields as they now have garbage data in them
                versionField = line[3]
                dateField = line[5]
                prField = ""
                commentField = ""
            if "*" in line:
                # getting pr data and coment field
                prOffset = len(line)
                if "([PR" in line:
                    prOffset = line.index("([PR")
                    prField +=f"<li> {' '.join(line[prOffset:])}</li>"
                commentField += f"<li> {' '.join(line[1:prOffset])} </li>"

            if (line == ['']):
                # combining into a single row in the table
                # because of how I wrote this, it produces a leading empty table that has to be ignored
                outputLine = f"| {versionField} | {dateField} | <ul>{prField}</ul> | <ul>{commentField}</ul> |"
                if outputLine != "|  |  | <ul></ul> | <ul></ul> |":
                    print(outputLine, file=newFileDescriptor)
        # end of file posting the last changelog
        outputLine = f"| {versionField} | {dateField} | <ul>{prField}</ul> | <ul>{commentField}</ul> |"
        if outputLine != "|  |  | <ul></ul> | <ul></ul> |":
            print(outputLine, file=newFileDescriptor)

def main():
    endpath = "./changelogs/compiled/"

    fileList = get_files()

    # iterates through all the files and generates a table from it
    for files in fileList:
        newFile = os.path.join(endpath, files[18:])
        generate_table(files, newFile)



if __name__ == "__main__": main()
