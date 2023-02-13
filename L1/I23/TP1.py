#Question 1

expression="!(p + q) * (!p + r) + (p * q)"
def ListerVariables(expression):
	a=sorted(expression)
	i=0
	b=[]
	print("a= ",a)
	while i < len(a):
		if a[i].isalpha():
			b=b+[a[i]]
		i= i+1
	print("avant del, b= ",b)
	i=0
	c=len(b)
	while i < (len(b)-1):
		print("b = ",b)
		if b[i]==b[i+1]:
			del b[i+1]
			c=c+1
			i=0
		else :
			i=i+1
	print("b final = ", b)
	return(b)


#Question 2

liste=["a","b","c","y","d","f","q","g","h","i","k","l","z","m","e","n","o","p","r","s","t","u","v","j","x"]
dico={}
def DicoVariables(liste):
	liste=sorted(liste)
	i=0
	while i < len(liste):
		dico[liste[i]]=i+1
		i=i+1
	return dico
print(DicoVariables(liste))


#Question 3

def Int2Bin(entier,n):
	binaire=bin(entier)
	binaire=binaire[2:]
	if len(binaire) < entier:
		bits=entier-len(binaire)
		print(bits)
		binaire = "0"*bits + str(binaire) 
	return(binaire)


#Question 4

def Bin2Bool(bits):
	t=()
	for 1 in bits:
		t = t + (bool(int(i)),)
	return t


#Question 5

def Math2Python(ex,vec,dic)
	i=0
	ch=''
	while i < len(ex):
		if ex[i] == "!":
			ch+="not"
		elif ex[i] == "*":
			ch+="and"
		elif ex[i] == "+":
			ch+="or"
		elif ex[i].isalpha():
			ch+=str(vec[dic[ex[i]]])
		else :
			ch+=ex[i]
		i = i+1
	return ch


#Question 6

def TabledeVerite(ex,dicovar):
	L=[]
	i=0
	while i < 2**len(dicovar):
		L+= [eval(Math2Python(ex,Bin2Bool(Int2Bin(i,len(dicovar))),dicovar))]
	return L












