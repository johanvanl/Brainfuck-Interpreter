import sys
from tape import Tape

def checkBrackets(source):
	count = 0
	for char in source:
		if char == '[':
			count += 1
		if char == ']':
			count -= 1
			
	if count != 0:
		raise Exception('The brackets aren\'t balanced.')	

def readFile(fn):
	sourceFile = open(fn, 'r')
	source = []
	while True:
		char = sourceFile.read(1)
		if not char:
			break
		if char in ['>', '<', '+', '-', '.', ',', '[', ']']:
			source.append(char)
			
	sourceFile.close()
	return source

def getBrackets(source):
	di = {}
	
	stack = []
	ind = 0
	while ind < len(source):
		char = source[ind]
		
		if char == '[':
			stack.append(ind)
			
		if char == ']':
			di[stack.pop()] = ind
		
		ind += 1
	
	return di

def interpret(source):
	brackets = getBrackets(source)
	inv_brackets = {v:k for k, v in brackets.items()}
	
	t = Tape()
	
	ind = 0	
	while ind < len(source):
		if source[ind] == '>':
			t.right()
			ind += 1			
		elif source[ind] == '<':
			t.left()
			ind += 1
		elif source[ind] == '+':
			t.inc()
			ind += 1
		elif source[ind] == '-':
			t.dec()
			ind += 1
		elif source[ind] == '.':
			sys.stdout.write(t.getChar())
			ind += 1
		elif source[ind] == ',':
			t.putChar()
			ind += 1
		elif source[ind] == '[':
			if t.getNum() == 0:
				ind = brackets[ind]
			ind += 1
		elif source[ind] == ']':
			ind = inv_brackets[ind]
			
def main(fn):
	source = readFile(fn)
	checkBrackets(source)
	interpret(source)
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		raise Exception('The file to be interpreted should be specified as an argument.')
		
	fn = sys.argv[1]
	main(fn)
	
