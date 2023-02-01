def xlsx_to_array(fname):
    import pathlib
    import pandas as pd
    df = pd.read_excel(fname)
    df = df.fillna('')
    array = df.values.tolist()
    return array

def csv_to_array(fname):
    import pathlib
    import csv
    array = []
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for _, line in enumerate(reader):
            array.append(line)
    f.close()
    return array

def txt_to_array(fname):
    import pathlib
    import csv
    array = []
    delim = det_delim(fname)
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter = delim)
        for i, line in enumerate(reader):
            array.append(line)
    f.close()
    return array

def det_delim(fname):
    colonamt = 0
    commaamt = 0
    semicamt = 0
    with open(fname, 'r') as f:
        l = f.readlines()
        semicamt = l.count(';')
        commaamt = l.count(',')
        colonamt = l.count(':')
    f.close()
    if (colonamt > commaamt) and (colonamt > semicamt):
        largest = ':'
    elif (commaamt > colonamt) and (commaamt > semicamt):
        largest = ','
    else:
        largest = ';'
    return largest

def compare_arrays(array1, array2):
    if len(array1) >= len(array2):
        x = len(array1)
    else:
        x = len(array2)
    if len(array1[0]) >= len(array2[0]):
        y = len(array1[0])
    else:
        y = len(array2[0])
    
    barray = [['' for x in range(y)] for x in range(x)]
    for i in range(len(array1)):
        for j in range(len(array1[i])):
            if (array1[i][j] == array2[i][j]):
                barray[i][j] = None
            else:
                barray[i][j] = f'old data: {array1[i][j]}, new data: {array2[i][j]}, located {chr(98 + i)}, {j + 1}'
    return barray

def det_type(fname):
    import pathlib
    import os
    name = os.path.splitext(fname)
    if (name[1] == '.txt'):
        return 1
    elif (name[1] == '.csv'):
        return 2
    elif (name[1] == '.xlsx'):
        return 3
    else:
        return name[1]

def compare_files(fname1, fname2):
    import pathlib
    lib = pathlib.Path
    try:
        fname1 = txt_to_array(fname1)
    except:
        try:
            fname1 = csv_to_array(fname1)
        except:
            try:
                fname1 = xlsx_to_array(fname1)
            except:
                print(fname2)
                print('line 91 compare_files')

    
    try:
        fname2 = txt_to_array(fname2)
    except:
        try:
            fname2 = csv_to_array(fname2)
        except:
            try:
                fname2 = xlsx_to_array(fname2)
            except:
                print(fname2)
                print('line 103 compare_files')
    
    try:
        return compare_arrays(fname1, fname2)
    except:
        print('line 108 compare_files')
        return 'ERROR'

def check_empty_array(array):
    import os
    try:
        os.path.exists(os.path.dirname(array))
        return 'path'
    except:
        for i in range(len(array)):
            try:
                for j in range(len(array[i])):
                    try:
                        if array[i][j] == '' or array[i][j] == ' ' or array[i][j] == None:
                            array[i].pop(j)
                    except:
                        pass
            except:
                pass
            if array[i] == '' or array[i] == ' ' or array[i] == None:
                array.pop(i)
        if len(array) == 0:
            if not array or array == None:
                return True
        else:
            return False

if __name__ == '__main__':
    print('import module')