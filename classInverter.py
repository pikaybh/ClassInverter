import glob, os

foo = input('[INFO] Index of class: ')

os.chdir("./")

for txt in glob.glob("*.txt"):
    f = open(txt, 'r')
    line = f.read()
    letters = line.split()
    letters[0]=str(foo)
    letters = " ".join(letters)
    f = open(txt, 'w')
    f.write(letters)
    f.close()

print('[INFO] Done!')