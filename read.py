#collects all file names in a dir
def get_file_names(fname):
    #finds all files in a dir
    import pathlib
    import pandas as pd

    lib = pathlib.Path

    temp = []
    
    if ((fname).exists()):
        for i in lib(fname).iterdir():
            file = i.name
            temp.append(file)
    else:
        raise Exception (f'{fname} isn\'t real')
    
    return pd.DataFrame(temp)

#determins the file extension
def det_filetype(fname):
    fname = str(fname)
    if fname.endswith('.txt'):
        return 0
    elif fname.endswith('.csv'):
        return 1
    elif fname.endswith('.xlsx'):
        return 2
    else:
        return 3

#determine the deliminator in a file
def det_delim(fname):
    import pathlib

    colonamt = 0
    commaamt = 0
    semicamt = 0
    with open(fname) as f:
        l = f.readline()
        semicamt = l.count(';')
        commaamt = l.count(',')
        colonamt = l.count(':')
    f.close()
    if (colonamt > commaamt) and (colonamt > semicamt):
        return ':'
    elif (semicamt > colonamt) and (semicamt > commaamt):
        return ';'
    else:
        return ','

#read a xlsx to df
def read_xlsx(fname):
    import pandas as pd
    import pathlib
    
    try:
        df =  pd.read_excel(fname)
        return df
    except:
        df =  pd.read_excel(fname, engine='openpyxl')
        return df

#reads a txt into a df
def read_txt(fname):
    import pandas as pd
    import pathlib

    try:
        df = pd.read_table(fname, sep = det_delim(fname))
        return df
    except:

        #defines final list
        outarray = []

        #opens file and pulls all lines into list
        with open(fname) as f:
            flist = f.readlines()
            f.close()

        #cleans up list by removing all spaces and newlines at begining and end
        # then splits items at delim and apends them to outarray
        for i in range(len(flist)):
            outarray.append(flist[i].strip().strip('\n').split(det_delim(fname)))
        
        return pd.DataFrame(outarray)

#reads a csv to a data frame
def read_csv(fname):
    import pandas as pd
    import pathlib
    import csv
    
    try:
        fname = pd.read_csv(fname)
    except:
        array = []
        with open(fname, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for _, line in enumerate(reader):
                array.append(line)
        f.close()
        fname = pd.DataFrame(array)
    return fname

#compares df by turning them into lists
def compare_array(df1, df2):
    import pandas as pd

    #handle non df
    if type(df1) == 'dict':
        df1 = pd.DataFrame.from_dict(df1)
    
    if type(df2) == 'dict':
        df2 = pd.DataFrame.from_dict(df2)

    df1.replace(to_replace=['None'], value = None, inplace=True)
    df2.replace(to_replace=['None'], value = None, inplace=True)

    df1.replace(to_replace=[None], value = pd.NA, inplace=True)
    df2.replace(to_replace=[None], value = pd.NA, inplace=True)

    df1 = df1.fillna(value = pd.NA).values.tolist()
    df2 = df2.fillna(value = pd.NA).values.tolist()

    #gets the greater length
    maxl = max(len(df1), len(df2))
    maxlj = max(len(df1[0]), len(df2[0]))

    #creates a 2d list the same size as the lists
    outarray = [None] * maxl
    for i in range(maxl):
        outarray[i] = [None] * maxlj
    
    #compares each item in the lists, appends nothing if equal
    for i in range(maxl):
        if i < len(df2) and i < len(df1):
            for j in range(maxlj):
                if j < len(df2[i]) and j < len(df1[i]):
                    if pd.isna(df1[i][j]) and pd.isna(df2[i][j]) or pd.isnull(df1[i][j]) and pd.isnull(df2[i][j]):
                            outarray[i][j] = pd.NA

                    else:
                        if pd.isna(df1[i][j]) or pd.isna(df2[i][j]) or pd.isnull(df1[i][j]) or pd.isnull(df2[i][j]):
                             outarray[i][j] = f'old: {df1[i][j]}, new: {df2[i][j]}'
                        else:
                            if df1[i][j] == df2[i][j]:
                                outarray[i][j] = pd.NA
                            else:
                                outarray[i][j] = f'old: {df1[i][j]}, new: {df2[i][j]}'
                
                else:
                    if len(df2[i]) == maxlj:
                        outarray[i][j] = f'old: None, new: {df2 [i][j]}'

                    elif len(df1[i]) == maxlj:
                        outarray[i][j] = f'old: {df1[i][j]}, new: None' 

                    else:
                        print('How?2')
                        input()

        else:
            if i > len(df2) and i > len(df1):
                pass
            else:
                if i > len(df1):
                    for t in range(maxlj):
                        if t < len(df2[i]):
                            if {df2[i][t]} == pd.NA:
                                outarray[i][j] = pd.NA
                            else:
                                outarray[i][t] = f'old: None, new: {df2[i][t]}' 

                if i > len(df2):
                    for t in range(maxlj):
                        if t <= len(df1[i]):
                            if {df1[i][t]} == pd.NA:
                                outarray[i][j] = pd.NA
                            else:
                                outarray[i][t] = f'old: None, new: {df1[i][t]}' 

    return pd.DataFrame(outarray)

#compares the contents of two files
def compare_file(fname1, fname2):
    import pandas as pd
    import pathlib

    print(fname1)
    print(fname2)

    match det_filetype(fname1):
        case 0:
            df1 = read_txt(fname1)
        case 1:
            df1 = read_csv(fname1)
        case 2:
            df1 = read_xlsx(fname1)
        case 3:
            print('read.py, line 94')

    match det_filetype(fname2):
        case 0:
            df2 = read_txt(fname2)
        case 1:
            df2 = read_csv(fname2)
        case 2:
            df2 = read_xlsx(fname2)
        case 3:
            print('read.py, line 104')

    try:
        return compare_array(df1, df2)
    except:
        print(fname1)
        print(fname2)
        input()