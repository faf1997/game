import time
import ctypes
from ctypes import c_double

mi_lib = ctypes.CDLL('./addition_functions.so')
mi_lib.suma_double.argtypes = [ctypes.c_float, ctypes.c_float]
mi_lib.suma_double.restype = ctypes.c_float

mi_lib.subtraction_double.argtypes = [ctypes.c_double, ctypes.c_double]
mi_lib.subtraction_double.restype = ctypes.c_double
mi_lib.div_double.argtypes = [ctypes.c_double, ctypes.c_double]
mi_lib.div_double.restype = ctypes.c_double
mi_lib.multiply_double.argtypes = [ctypes.c_double, ctypes.c_double]
mi_lib.multiply_double.restype = ctypes.c_double



def medir_tiempo(func):
    def wrapper():
        inicio = time.time()
        func()
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        #print(f"Tiempo de ejecución de {func.__name__}: {tiempo_transcurrido} segundos")


def add(a:float, b:float,opeation_type:str="+")->float:

    result:float = mi_lib.suma_double(a,b)
    return result

def subtract(a:float, b:float,opeation_type:str="+")->float:

    result:float = mi_lib.subtraction_double(a,b)
    return result

def divide(a:float, b:float,opeation_type:str="+")->float:

    result:float = mi_lib.div_double(a,b)
    return result

def multiply(a:float, b:float,opeation_type:str="+")->float:

    result:float = mi_lib.multiply_double(a,b)
    return result


def prueba():
    inicio = time.time()
    for _ in range(10000000):
        add(0.2,0.1)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print(tiempo_transcurrido)


def sumar(a,b):
    return a + b

def prueba2():
    inicio = time.time()
    for _ in range(10000000):
        sumar(0.2,0.1)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print(tiempo_transcurrido)




if __name__ == "__main__":
    prueba()
    # print(op_arithmetic(0.3,5.1))
    # print(op_arithmetic(0.3,5.1,"-"))
    # print(op_arithmetic(0.3,5.1,"/"))
    # print(op_arithmetic(0.3,5.1,"*"))



