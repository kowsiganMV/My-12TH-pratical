class sample:
			def __init__(self):
					self.a=str(input("enter a string:"))
					self.uppercase=0
					self.lowercase=0
					self.vowels=0
					self.constant=0
					self.space=0
					self.string=0
					self.b='a','e','i','o','u','A','E','I','O','U'
					self.c='!','@','#','$','%','^','&','*','(',')','-','_','+','=','[','{','}',']',';',':','"','/',',','>','<','\'','?'
			def upper(self):
					for i in self.a:
						if i.isupper():
							self.uppercase+=1
			def lower(self):
					for i in self.a:
						if i.islower():
							self.lowercase+=1
			def vowel(self):
					for i in self.a:
						if i in self.b:
							self.vowels+=1
			def constan(self):
					for i in self.a:
						if i not in self.b and self.c:
							self.constant+=1
						
			def spaces(self):
					for i in self.a:
						if i==" ":
							self.space+=1
			def strings(self):
					for i in self.a:
						if i in self.c:
							self.string+=1
			def output(self):
					print("captail letters=",self.uppercase)
					print("smaill letters=",self.lowercase)
					print("vowel letters=",self.vowels)
					print("constant letters=",self.constant)
					print("spaces=",self.space)
					print("spacial careacters=",self.string)
s=sample()
s.upper()
s.lower()
s.vowel()
s.constan()
s.spaces()
s.strings()
s.output()