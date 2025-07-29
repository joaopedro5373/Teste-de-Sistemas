from functions import soma
from functions import produto

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