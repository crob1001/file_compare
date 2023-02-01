import pathlib
import os
import find_files
import write
import compare_files

w = write
c = compare_files
m = find_files
lib = pathlib.Path

fields = ['matches', 'Sdrive', 'FTP']

p = lib(__file__).parents[1]
dir1 = lib(str(p) + '/' + 'FTP')
dir2 = lib(str(p) + '/' + 'SDRIVE')

temp = []

a = 0

for i in c.csv_to_array("C:\\Users\\croberts\\Desktop\\compare\\out\\parity.csv"):
    if i[0] != ' ' and i[0] != '' and i[0] != None:
        temp.append(i[0])
temp.pop(0)


for i in temp:
    fname = i
    try :
        file_matches = m.matches(lib(str(dir1) +'/'+ fname + '/Crossrates'), lib(str(dir2) +'/'+ fname))
    except:
        file_matches = m.matches(lib(str(dir1) +'/'+ fname), lib(str(dir2) +'/'+ fname))
    for j in file_matches:
        for l in j:
            try:
                array = c.compare_files(lib(str(dir1) +'/'+ fname + '/Crossrates/' + l), lib(str(dir2) +'/'+ fname +'/'+ l))
            except:
                try:
                    array = c.compare_files(lib(str(dir1) +'/'+ fname +'/'+ l), lib(str(dir2) +'/'+ fname +'/'+ l))
                except:
                    continue
            name = os.path.splitext(l)
            input(name)
            empty = c.check_empty_array(array)
            if empty == None:
                continue
            else:
                try:
                    os.makedirs('C:/Users/croberts/Desktop/compare/out/test3/' + fname + '/')
                except:
                    pass
                w.write_colums(lib('C:/Users/croberts/Desktop/compare/out/test3/' + fname + '/' + name[0]), array)
            array = []
        print(a)
        a += 1 