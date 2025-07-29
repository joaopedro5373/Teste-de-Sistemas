def soma(a:int,b:int)->int: 
    if (type(a) == str):
        try:
            if(len(a) == 0 or a.isspace()): a = 0
            elif("." in a): a = float(a)
            else: a = int(a)
        except: a = 0
    if (type(b) == str): 
        try:
            if(len(b) == 0 or b.isspace()): b = 0
            elif("." in b): b = float(b)
            else: b = int(b)
        except: b = 0
    a = round(a)
    b = round(b)
    return a + b

def produto(a:int, b:int)->int: 
    if (type(a) == str):
        try:
            if(len(a) == 0 or a.isspace()):
                a = 0
            elif("." in a): a = float(a)
            else: a = int(a)
        except: a = 0
    if(type(b) == str):
        try:
            if (len(b) == 0 or b.isspace()): b = 0
            elif("." in b): float(b)
            else: b = int(b)
        except: b = 0
    a = round(a)
    b = round(b)
    return a*b