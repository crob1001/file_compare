def write_colums(filenm, data): 
    import csv
    import pathlib
    lib = pathlib.Path

    temp = []
    longl = []

    try:
        for i in data:
            if len(i) > len(longl):
                longl = i
    except:
        pass

    f = open(lib(str(filenm) + '.csv'), 'w', newline='')
    write = csv.writer(f)
    n = 0
    while n != len(longl):
        try:
            temp.append(data[0][n])
        except:
            temp.append(None)
        try:
            temp.append(data[1][n])
        except:
            temp.append(None)
        try:
            temp.append(data[2][n])
        except:
            temp.append(None)
        n+=1
        write.writerow(temp)
        temp = []
    f.close()

def write_rows(filenm, data):
    import csv
    import pathlib
    lib = pathlib.Path

    f = open(lib(str(filenm) + '.csv'), 'w', newline='')
    print(filenm)
    write = csv.writer(f)
    write.writerows(data)
    f.close()

if __name__ == '__main__':
    print('import module')