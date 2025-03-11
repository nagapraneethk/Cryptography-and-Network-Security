import random

p = 29
g = 2
private_a = random.randint(2, p - 1)
private_b = random.randint(2, p - 1)

pub_a = pow(g, private_a, p)
pub_b = pow(g, private_b, p)

shared_a = pow(pub_b, private_a, p)
shared_b = pow(pub_a, private_b, p)

print(f"Public key of A: {pub_a}")
print(f"Public key of B: {pub_b}")
print(f"Shared secret of A: {shared_a}")
print(f"Shared secret of B: {shared_b}")
