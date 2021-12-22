import random
import secrets

# Generate private_key using secrets library
def usingSecrets():
    bits = secrets.randbits(256)
    bits_hex = hex(bits)
    private_key = bits_hex[2:]
    while(len(private_key) < 64):
        private_key = "0" + private_key
    return private_key

# Generate private_key using random library (using current time, not secure)
def usingRandom():
    bits = random.getrandbits(256)
    bits_hex = hex(bits)
    private_key = bits_hex[2:]
    while(len(private_key) < 64):
        private_key = "0" + private_key
    return private_key