def create_dir(fname):
    #external libs
    import pathlib

    #lib const
    lib = pathlib.Path
    p = lib(__file__).parents[1]

    #creates dir
    fname.mkdir(parents=True, exist_ok=True)

def write_csv(path, data):
    #external libs
    import pathlib
    import pandas
    import os

    #lib const
    lib = pathlib.Path
    p = lib(__file__).parents[1]
    
    #changes file extension
    path = path.with_suffix('.csv')

    os.makedirs(os.path.dirname(path), exist_ok=True)

    data.to_csv(path)

def write_txt(path, data):
    #external libs
    import pathlib
    import pandas
    import os

    #lib const
    lib = pathlib.Path
    p = lib(__file__).parents[1]
    
    #changes file extension
    path = path.with_suffix('.txt')

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'a') as f:
        for i in data:
            f.write(f'{i}\n')

def file_copy(src, dest):
    import pathlib
    import shutil
    import os

    #lib const
    lib = pathlib.Path
    p = lib(__file__).parents[1]
    
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copy(src, dest)