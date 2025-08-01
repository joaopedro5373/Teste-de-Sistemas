from functions import *

def test_soma_int():
    a = 10
    b = 15
    resultadoEsperado = 25
    resultado = soma(a, b)
    assert resultado == resultadoEsperado

def test_soma_float():
    a = 0.55
    b = 0.25
    resultadoEsperado = 1
    resultado = soma(a, b)
    assert resultado == resultadoEsperado

def test_soma_float_floatString():
    a = "1.5"
    b = "1.5"
    resultadoEsperado = 4
    resultado = soma(a, b)
    assert resultado == resultadoEsperado

def test_soma_emptyString():
    a="eqd"
    b="qedwe    dwe"
    resultadoEsperado = 0
    resultado = soma(a, b)
    assert resultado == resultadoEsperado

def test_produto_int():
    a = 2.51
    b = 2
    resultadoEsperado = 6
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_string():
    a = "2"
    b = "7"
    resultadoEsperado = 14
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_formatarNome():
    nome = "João"
    sobrenome = "Pedro"
    resultadoEsperado = "João Pedro"
    resultado = formatar_nome(nome, sobrenome)
    assert resultado == resultadoEsperado

def test_verificarSenha():
    senha = "pAo12w#@swq121"
    resultadoEsperado = True
    resultado = verificar_senha(senha)
    assert resultado == resultadoEsperado

def test_read_file_content():
    path = "texto.txt"
    resultado = read_file_content(path)
    resultadoEsperado = "batata"
    assert resultado == resultadoEsperado

def test_fatorial():
    numero = 3
    resultado = factorial(numero)
    resultadoEsperado = 6
    assert resultado == resultadoEsperado

def test_divide():
    a = 2
    b = 2
    resultado = divide(a, b)
    resultadoEsperado = 1
    assert resultado == resultadoEsperado

def test_authenticate_user():
    username = "admin"
    password = "1234"
    resultado = authenticate_user(username, password)
    resultadoEsperado = True
    assert resultado == resultadoEsperado

def test_reverse_string():
    s = "banana"
    resultado = reverse_string(s)
    resultadoEsperado = "ananab"
    assert resultado == resultadoEsperado

def test_count_word_occurrences():
    word = "batata"
    text = "batata é gostosa de todo jeito, batata frita, batata cozida, batata rústica, batata palha, " \
    "batata em salgadinho, batata no purê, enfim, batata é vida."
    resultadoEsperado = 8
    resultado = count_word_occurrences(text, word)
    assert resultado == resultadoEsperado

def test_calculate_avarage():
    numbers = [2, 4, 6, 8]
    resultado = calculate_average(numbers)
    resultadoEsperado = 5
    assert resultado == resultadoEsperado

def test_is_prime():
    n = 3
    resultado = is_prime(n)
    resultadoEsperado = True
    assert resultado == resultadoEsperado

def test_environment_variable():
    os.environ["comida"] = "batata"
    resultadoEsperado = "batata"
    resultado = get_environment_variable("comida")
    assert resultado == resultadoEsperado

def test_flatten_list():
    objetos = ["mesa", "cama"]
    frutas = ["banana", "morango"]
    nested_list = [frutas, objetos]
    resultado = flatten_list(nested_list)
    resultadoEsperado = ["banana", "morango", "mesa", "cama"]
    assert resultado == resultadoEsperado
