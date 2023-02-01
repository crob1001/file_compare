#external libs
import pandas as pd
import pathlib
from datetime import date


#internal libs
import write as w
import read as r 

#lib const
lib = pathlib.Path
p = lib(__file__).parents[1]

#other const
COMPARISON_FILE = lib(str(p) + '/src/parity_working.csv')
COPY_CHECKED = False

#find and use comparison file
def get_comparison(fname):
    fname = r.read_csv(fname)
    fname = fname.values.tolist()
    return pd.DataFrame(fname).dropna()

#main fuction, start point
def main():
    outpath = lib(f'{str(p)}/out/{str(date.today())}')
    diff = lib(f'{outpath}/D')

    print('starting')

    w.create_dir(outpath)

    #creates a df that contains the name of the company and the win paths to each of their dirs
    df =  get_comparison(COMPARISON_FILE)

    for i in range(len(df)):
        mfiles = []
        gfiles = []
        bfiles = []

        print(i)

        #creates dirs
        #creates a list of 2 df one for each set of files in the dirs derived from the comparison file
        allfilenms = [r.get_file_names(lib(df.iloc[i,0])).values.tolist(), r.get_file_names(lib(df.iloc[i,1])).values.tolist()]

        #makes an array that contains all the files names that match
        for j in range(len(allfilenms[0])):
            print(j)
            if (allfilenms[0][j] in allfilenms[1]):
                if (allfilenms[0][j] not in gfiles):
                    gfiles.append(allfilenms[0][j])
            else:
                if (allfilenms[0][j] not in bfiles):
                    bfiles.append(allfilenms[0][j])
        
        #double checks the array of files from the other location
        for j in range(len(allfilenms[1])):
            print(j)
            if (allfilenms[1][j] in allfilenms[0]):
                if (allfilenms[1][j] not in gfiles):
                    gfiles.append(allfilenms[1][j])
            else:
                if (allfilenms[1][j] not in bfiles):
                    bfiles.append(allfilenms[1][j])

        for l in range(len(bfiles)):
            if bfiles[l] in gfiles:
                bfiles.pop(l)

        for j in range(len(bfiles)):
            print(j)
            try:
                w.file_copy(lib(f'{df.iloc[i,0]}/{bfiles[j][0]}'), lib(f'{diff}/FTP/{df.iloc[i,2]}/{bfiles[j][0]}'))
            except:
                w.file_copy(lib(f'{df.iloc[i,1]}/{bfiles[j][0]}'), lib(f'{diff}/SDRIVE/{df.iloc[i,2]}/{bfiles[j][0]}'))
        
        #loops through gfiles and checks if the two files are equal returning differences
        #writes to output file
        for j in range(len(gfiles)):
            print(j)
            temp = r.compare_file(lib(f'{df.iloc[i,0]}/{gfiles[j][0]}'), lib(f'{df.iloc[i,1]}/{gfiles[j][0]}'))#.values.tolist()

            #if it's empty 
            if not temp.isnull().all().all():
                w.write_csv(lib(f'{diff}/{df.iloc[i,2]}/{gfiles[j][0]}'), temp)
            else:
                mfiles.append(gfiles[j][0])
        
        w.write_txt(lib(f'{outpath}/M/{df.iloc[i,2]}'), mfiles)

        w.write_txt(lib(f'{outpath}/A/{df.iloc[i,2]}'), allfilenms)

main()