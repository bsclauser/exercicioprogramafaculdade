from random import seed, randrange 
# Gera n números aleatórios no intervalo [a, b) 
def GeraAmostra(a, b, n): 
	# Use o seu NUSP como semente      
	NUSP = 11221230
	seed(NUSP)     
	amostra = n * [0] 
	for k in range(n):         
	 	amostra[k] = a + float(randrange(1000000)) * (b - a)/1000000.0 

	return amostra


def PrintAmostra(length, ga):
	print("Amostra:")
	maxga = len(str(max(ga)))
	maxgaint = int(maxga)
	for i in range (len(ga)):
		difga = maxgaint - len(str(int(ga[i])))
		if i == 0 or i == 1:
			print (" "*difga,"%.3f" %ga[i], end="")
		elif ((i+1)%5) == 0:
			print (" "*difga,"%.3f" %ga[i])
		else:
			print (" "*difga,"%.3f" %ga[i], end="")

	print()


def main():
	a, b = map(float, input("Entre com o intervalo:").split())
	n = int(input("Entre com a quantidade de elementos na amostra:"))
	while n <= 0: 
		n = int(input("A quantidade de elementos na amostra deve ser um número positivo diferente de zero. Tente novamente. \nEntre com a quantidade de elementos na amostra:"))
	while (b-a)/n < 0.001:
		print("Os valores que você inseriu para o intervalo são inválidos. \nOs valores do intervalo devem ser diferentes e o segundo deve ser maior que o primeiro. \nTente novamente.")
		main()
	ga = GeraAmostra(a, b, n)
	length = len(ga) + 1
	PrintAmostra(length, ga)
	while True:
		nintervalo = int(input("Entre com o número de intervalos:"))
		if nintervalo <= 0:
			main()
		valorint = (b-a)/nintervalo
		inter = a
		inter2 = 0.000
		cont = [0]*nintervalo
		for i in range (nintervalo):
			inter2 = inter 
			inter += valorint
			for j in range (len(ga)):
				if ga[j] < inter and ga[j] >= inter2:
					cont[i] += 1
		print ("          Intervalo     ", "         Frequência     ", "     Gráfico     ")
		inter = a
		inter2 = 0.000
		intervalosesq = [0] * (nintervalo)
		intervalosdir = [0] * (nintervalo)
		for g in range (nintervalo):
			inter2 = inter 
			inter += valorint
			intervalosesq[g] = inter2
			intervalosdir[g] = inter
		maxinter2 = max(intervalosesq)
		maxinter = max(intervalosdir)
		maxfreq = max(cont)
		for j in range (nintervalo):
			difesq = (len(str(int(maxinter2))) - len(str(int(intervalosesq[j]))))
			difdire = (len(str(int(maxinter))) - len(str(int(intervalosdir[j])))) 
			diffreq = (len(str(int(maxfreq)))) - len(str(int(cont[j]))) 
			print(" "*difesq,"%.3f" %intervalosesq[j],"A"," "*difdire ,"%.3f" %intervalosdir[j], end="")
			print(" "*(diffreq+12), cont[j], end="")
			print("               ", end ="")

			for u in range (cont[j]):
				print("\u25a0", end="")
			print()
main()
			