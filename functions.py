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

def formatar_nome(nome:str, sobrenome:str)->str:
    if(type(nome) == str and type(sobrenome) == str):
        if(len(nome) == 0 or nome.isspace() or len(sobrenome) == 0 or sobrenome.isspace()):
            raise ValueError("Os campos nome e sobrenome não podem estar vazios.")
    else: raise TypeError("Nome e sobrenome devem ser do tipo string.")
    nomeCompleto = f"{nome} {sobrenome}"
    return nomeCompleto

# | =============================== |
# | Verificador de senhas funcional |
# | =============================== |
def verificar_senha(senha:str)->bool:
    if(type(senha) is not str):
        raise TypeError("A senha precisa ser uma string.")
    elif(len(senha) == 0 or senha.isspace()):
        raise ValueError("A senha não pode ser vazia.")
    if(len(senha) < 8):
        return False
    temMaiuscula = any(c.isupper() for c in senha)
    temMinuscula = any(c.islower() for c in senha)
    temNumero = any(c.isdigit() for c in senha)
    tem_especial = any(not c.isalnum() for c in senha)
    if(temMaiuscula and temMinuscula and temNumero and tem_especial):
        return True
    else: return False
