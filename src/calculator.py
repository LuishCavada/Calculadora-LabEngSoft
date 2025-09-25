class Calculator:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return None if b == 0 else a / b

    @staticmethod
    def exp(a, b):
        if a == 0 and b == 0:
            return None  # Indeterminação 0^0
        return a ** b
