from calculator import Calculator
from validOps import validOps 

def Calculate(a, b, op):
    calculator = Calculator()

    switcher = {
    "+": calculator.sum,
    "-": calculator.sub,
    "*": calculator.mul,
    "/": calculator.div,
    "^": calculator.exp
    }


    try:
        a = float(a)
    except (ValueError, TypeError):
        return None

    if op not in validOps:
        return None


    try:
        b = float(b)
    except (ValueError, TypeError):
        return None

    result = switcher.get(op, lambda: "unknown")(a, b)

    return result

if __name__ == "__main__":
    a = input("Insira o primeiro operando: ")

    op = input("Insira a operação (Escolha entre +, -, /, * e ^): ")

    b = input("Insira o segundo operando: ")



    result = Calculate(a, b, op)

    if result == None:
        print("Algo deu errado, o valor é None")
        exit()

    else:
        print("O resultado foi " + str(result))
        exit()