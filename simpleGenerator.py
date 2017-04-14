# Simple example: Generators

def myGenerator():
	yield "These"
	yield "are"
	yield "words"
	yield "come"
	yield "one"
	yield "at"
	yield "a"
	yield "time"
	
	
myGenInstance = myGenerator()

for word in myGenInstance:
	print word
