print("Inserisci un importo intero")
a=input("A:")
a=int(a)

if a==0:
	print("inserisci un numero diverso da 0")
	
else:
	print("importo (dollari):",a)
	
	v=a/20
	v=int(v)
	print("biglietti da $20:",v)
	
	
	d=v*20
	D=a-d
	dd=D/10
	dd=int(dd)
	print("biglietti da $10:",dd)
	
	C=D-10
	c=dd/5
	c=int(c)
	print("biglietti da $5:",c)
	
	u=C/1
	u=int(u)
	print("biglietti da $1:",u)
	
	
