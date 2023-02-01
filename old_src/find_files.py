#checks if dirs are the same

def matches(dir1, dir2):
    import pathlib

    lib = pathlib.Path
    dir1l = []
    dir2l = []
    m = []
    u1 = []
    u2 = []


    if ((dir1).exists()):
        for p in lib(dir1).iterdir():
            file_name = p.name
            dir1l.append(file_name)
    else:
        raise Exception (f'{dir1} isn\'t real')

    if (dir2.exists()):
            for p in lib(dir2).iterdir():
                file_name = p.name
                dir2l.append(file_name)
    else:
        raise Exception (f'{dir2} isn\'t real')
        
    for i in dir1l:
        if (i in dir2l):
            if (i not in m):
                m.append(i)
        else:
            u1.append(i)

    for i in dir2l:
        if (i in dir1l):
            if (i not in m):
                m.append(i)
        else:
            u2.append(i)

    return [m,u1,u2]

# if __name__ == '__main__':
#     print('import module')