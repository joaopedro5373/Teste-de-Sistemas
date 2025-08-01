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

import math
import os

def calculate_average(numbers:int)->float:
    return sum(numbers) / len(numbers)

def is_prime(n:int)->bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def read_file_content(path:str)->str:
    with open(path, "r") as f:
        return f.read()

def count_word_occurrences(text:str, word:str)->int:
    return text.lower().split().count(word.lower())

def factorial(n:int)->int:
    if n == 0:
        return 1    
    return n * factorial(n - 1)

def reverse_string(s:str)->str:
    return s[::-1]

def get_environment_variable(var_name:str)->str:
    return os.environ[var_name]

def divide(a:float, b:float)->float:
    return a / b

def flatten_list(nested_list:list)->list:
    return [item for sublist in nested_list for item in sublist]

def authenticate_user(username:str, password:str)->bool:
    return username == "admin" and password == "1234"
