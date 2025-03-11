import math

a = 182841384165841685416854134135
b = 135481653441354138548413384135

modular_div= a % b
print(f"Modular Division: {modular_div}")


division_int = a // b
gcd_ab = math.gcd(a, b)
print(f"integer Division: {division_int}")

modinverse = 0
try:
    modinverse = pow(a, -1, b)
except ValueError:
    print("NO MOD INVERSE FOUND FOR THIS")

print(f"Modulo inverse Division: {modinverse}")