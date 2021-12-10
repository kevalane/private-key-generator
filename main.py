import keygen as kg
import unsecure as us

# Using secrets library
skey = us.usingSecrets()
print(skey)
print(len(skey))

# Using random
rkey = us.usingRandom()
print(rkey)
print(len(rkey))

# Using keygen
key = kg.KeyGen(256, 32)
key.takeInput('AEHUFoeaBNgjSRBNgjio;SRbnjhirs brhsil gbnrsahilvnvn ;asvbhialrsbvliasrb vslaih')
kkey = key.generateKey()
print(kkey)
print(len(kkey))