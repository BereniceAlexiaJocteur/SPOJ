import decimal

decimal.getcontext().prec = 9030

res = decimal.Decimal(2)
fact = decimal.Decimal(1)

for i in range(2, 2971):
    fact *= i
    res += 1/fact

print(res)
