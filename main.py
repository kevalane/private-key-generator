import random
import secrets
import keygen as kg
import time

# Generate private_key using secrets library
def usingSecrets():
    bits = secrets.randbits(256)
    bits_hex = hex(bits)
    private_key = bits_hex[2:]
    return private_key

# Generate private_key using random library (using current time, not secure)
def usingRandom():
    bits = random.getrandbits(256)
    bits_hex = hex(bits)
    private_key = bits_hex[2:]
    return private_key

key = kg.KeyGen(256, 32)
key.takeInput('AEHUFoeaBNgjSRBNgjio;SRbnjhirs brhsil gbnrsahilvnvn ;asvbhialrsbvliasrb vslaih')
print(key)