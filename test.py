
def hi(name):
	print("hi "+name)

hi("daniel")

if 14>12:
	print ("答對了!!")
else:
	print ("錯誤了!!")

class Cat:
	def __init__(self, name):
		self.name=name

	def meow(self):
		print (self.name+" Mewo!!!~~~~")

	def __str__(self):
		return self.name+" Ha ha ha...."

cc = Cat('Daniel')
cc.meow()
print(cc)
