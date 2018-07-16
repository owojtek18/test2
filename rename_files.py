import glob, os
# dvod,vodskovod,vodsov

def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        print(pathAndFilename)
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        # os.rename(pathAndFilename, os.path.join(dir, titlePattern % title + ext))
        os.rename(pathAndFilename, os.path.join(dir, titlePattern % title + ext))

rename(r'C:\Users\wojci\Desktop\txt', r'new*.txt', r'new(%s)')

