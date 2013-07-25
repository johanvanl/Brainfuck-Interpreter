import sys

class Tape(object):

	def __init__(self):
		self.size = 5
		self.tape = [0] * self.size
		self.index = self.size / 2

	def resize(self):
		temp = [0] * (self.size/2)
		temp.extend(self.tape)
		self.tape = temp
		
		temp = [0] * (self.size/2)
		self.tape.extend(temp)
		
		self.index += (self.size/2)
		self.size = len(self.tape)
		
	def left(self):
		if self.index == 0:
			self.resize()
			
		self.index -= 1

	def right(self):
		if self.index == self.size - 1:
			self.resize()
			
		self.index += 1
		
	def inc(self):
		self.tape[self.index] += 1

	def dec(self):
		self.tape[self.index] -= 1
		
	def putChar(self):
		self.tape[self.index] = ord(sys.stdin.read(1))
		
	def getNum(self):
		return self.tape[self.index]
		
	def getChar(self):
		return chr(self.getNum())
		
	def __str__(self):
		return str(self.tape)
		
if __name__ == '__main__':
	t = Tape()	
	t.put()
		
	for i in range(5000):
		t.right()
		
	t.put()
	
	for i in range(5000):
		t.left()
	
	print t.getChar()			
	#print t
	
