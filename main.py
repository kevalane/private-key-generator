import random

bits = random.getrandbits(256)
bits_hex = hex(bits)
private_key = bits_hex[2:]
print(private_key)
