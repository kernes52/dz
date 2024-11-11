class FactorialCalculator:
    _cache = {0: 1, 1: 1}

    def factorial(a):
        if a in FactorialCalculator._cache:
            return FactorialCalculator._cache[a]
        result = a * FactorialCalculator.factorial(a - 1)
        FactorialCalculator._cache[a] = result
        return result

print(FactorialCalculator.factorial(6))
print(FactorialCalculator.factorial(3))