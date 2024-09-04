def operAritmetic(val1, val2, operator):
    try:
        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        elif operator == '*':
            return val1 * val2
        elif operator == 'sqrt':
            if val2 == 0:
                return 'Error: El índice de la raíz no puede ser cero'
            else:
                return val1 ** (1 / val2)
        elif operator == '/':
            if val2 == 0:
                raise ValueError("No puede dividir por cero")
            return val1 / val2
        else:
            raise ValueError("Operador no válido")
    except Exception as e:
        print(f"Error: {e}" )
        
def calcIva(cifra):
    return cifra * 19/100

# Generar un metodo que permita retornar la cadena de los N primeros numero de la serie 
# de fibonacci 

def fibonacciSeries(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return ', '.join(map(str, fib_series))

# Generar un metodo que permita retornar el factorial de cualquier numero
def factorial(num):
    if num < 0:
        raise ValueError("El factorial no está definido para números negativos")
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
   




