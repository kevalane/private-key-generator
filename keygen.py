import time
import secrets
import random

class KeyGen:

	def __init__(self, poolLength = 512, bytes = 32):
		self.poolLength = poolLength
		self.bytes = bytes
		self.test = 0
		self.index = 0
		self.pool = [0]*self.poolLength
		self.curve = int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141', 16)
		self.generateSecretBits()

	def __str__(self):
		return str(self.pool)
	
	# Function to insert byte in pool
	def insertByte(self, num):
		# XOR applied
		self.pool[self.index] = num
		# Make sure we don't get out of index array error
		if self.index >= self.poolLength - 1:
			self.index = 0
		else:
			self.index = self.index + 1

	# Generate bits using secrets library
	def generateSecretBits(self):
		# Generate a number for every poolLength
		for i in range(0, self.poolLength):
			secretByte = secrets.randbits(8)
			self.insertByte(secretByte)
		
		# Let's get some time bits in there
		self.generateTimeBits()

	# Generate bits using time library
	def generateTimeBits(self):
		timeInteger = int(time.time())
		# We need to insert some and shift the bits a random length
		randInt = secrets.SystemRandom().randint(0, 50)
		for i in range(0, randInt):
			byte = timeInteger >> secrets.SystemRandom().randint(0,32)
			while (byte >= 256):
				byte /= 10
			byte = int(byte)
			self.insertByte(byte)

	# Get user input, to be called
	def takeInput(self, input):
		self.generateTimeBits()
		for char in input:
			charCode = ord(char)
			self.insertByte(charCode)

	# Generate an integer
	def generateInt(self):
		seed = int.from_bytes(self.pool, byteorder='big', signed=False)
		random.seed(seed)
		return random.getrandbits(self.bytes * 8)

	# Generate the final key
	def generateKey(self):
		bigInt = self.generateInt()
		bigInt = bigInt % (self.curve - 1)
		bigInt = bigInt + 1
		key = hex(bigInt)[2:]
		while(len(key) < 64):
			key = "0" + key
		return key
