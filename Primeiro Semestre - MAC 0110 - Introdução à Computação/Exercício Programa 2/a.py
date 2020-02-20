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

#Função que imprime a amostra
def PrintAmostra(ga):
	print("Amostra:")
	maxga = len(str(max(ga)))
	maxgaint = int(maxga)
	#Impressão e formatação da amostra
	#Imprime apenas 5 colunas de números
	for i in range (len(ga)):
		difga = maxgaint - len(str(int(ga[i])))
		if i == 0 or i == 1:
			print (" "*difga,"%.3f" %ga[i], end="")
		elif ((i+1)%5) == 0:
			print (" "*difga,"%.3f" %ga[i])
		else:
			print (" "*difga,"%.3f" %ga[i], end="")

	print()

#Função principal
def main():
	#Pede que o usuáro insira o intervalo [a,b) na mesma linha
	#Separando os valores por um espaço em branco
	a, b = map(float, input("Entre com o intervalo, separando os números por um espaço em branco:").split())
	while a or b == ' ':
		a, b = map(float, input("Entre com o intervalo, separando os números por um espaço em branckko:").split())
	#Solicita a quantidade n de elementos na amostra
	n = int(input("Entre com a quantidade de elementos na amostra:"))
	#Consistência para n negativo e igual a zero
	while n <= 0: 
		n = int(input("A quantidade de elementos na amostra deve ser um número positivo diferente de zero. Tente novamente. \nEntre com a quantidade de elementos na amostra:"))
	#Consistência para valores inválidos, como a=b e a>b
	while (b-a)/n < 0.001:
		print("Os valores que você inseriu para o intervalo são inválidos. \nOs valores do intervalo devem ser diferentes e o segundo deve ser maior que o primeiro. \nTente novamente.")
		main()
	#Chama a função que gera a amostra e amarzena a lista que ela retorna na variável ga
	ga = GeraAmostra(a, b, n)
	#Chama a função que imprime a amostra
	PrintAmostra(ga)
	#Solicita o número de intervalos infinitamente
	while True:
		#Solicita o número de intervalos
		nintervalo = int(input("Entre com o número de intervalos:"))
		#Se o valor que o usuário digitou é menor ou igual a zero o programa começa novamente
		#Solicita outros valores para a, b e n
		if nintervalo <= 0:
			main()
		#Calcula o valor do intervalo a ser acrescido desde o a até o b
		#Exemplo: a = 0 e b = 10 nintervalo = 10. Aqui, o valor do intervalo será de 1, então teremos intervalos de 0 a 1, 1 a 2.....
		valorint = (b-a)/nintervalo
		#Valor inical do intervalo atribuído a variável inter2 e a atribuído a inter
		inter = a
		inter2 = 0.000
		cont = [0]*nintervalo
		#Comando for cria uma lista com a frequência de números da amostra nos intervalos
		for i in range (nintervalo):
			inter2 = inter #inter2 assume o valor inicial do intervalo
			inter += valorint #inter é acrescido com o valor do intervalo 
			for j in range (len(ga)):
				if ga[j] < inter and ga[j] >= inter2: #Verifica se há números no intervalo [inter2, inter)
					cont[i] += 1 #Se sim, adiciona 1 à lista. Cada index da lista serve como um contador para cada intervalo
		#Retorna os valores inicias a inter e inter 2
		inter = a
		inter2 = 0.000
		#Cria listas para armazenar os valores dos intervalos à direita e à esquerda em relação
		intervalosesq = [0] * (nintervalo)
		intervalosdir = [0] * (nintervalo)
		#Comando for armazena os intervalos à direita e à esquerda em suas respectivas listas
		for g in range (nintervalo):
			inter2 = inter 
			inter += valorint
			intervalosesq[g] = inter2
			intervalosdir[g] = inter
		#Calcula o valor máximo de cada lista
		maxinter2 = max(intervalosesq)
		maxinter = max(intervalosdir)
		#Calcula o valor máximo da lista cont que contém as frequências
		maxfreq = max(cont)
		#Comando for que realiza a impressão dos intervalos, frequências e gráfico
		for j in range (nintervalo): 
			#Calcula a diferença 
			#Entre o tamanho do maior número da lista de frequências e o tamanho da frequência a ser impressa para o respectivo intervalo
			diffreq = (len(str(int(maxfreq)))) - len(str(int(cont[j]))) 
			#A partir daqui ocorre o cálculo para a formatacção correta das colunas dos intervalos, da coluna de frequências e do gráfico
			#Para os intervalosesq[j] e intervalosdir[j] ocorre a verificação se eles estão entre -1 e 0
			#Porque eles foram convertidos para inteiros e, na hora de calcular o difdire e difesq, ocorre uma alteração na formatação
			#Pois, como int, se valem entre -1 e 0, seu valor de 0.xxx fica 0, o que afeta o cálculo
			#Por isso há o -1 após a subtração para corrigir o valor
			#difesq e difdire são variáveis que armazenam a diferença de tamanho de caracteres entre o maior número e o que vai ser impresso
			#Com o objetivo de imprimir colunas alinhadas
			if -1 <= intervalosesq[j] <= 0:
				difesq = (len(str(int(maxinter2))) - len(str(int(intervalosesq[j])))) - 1
			else:
				difesq = len(str(int(maxinter2))) - len(str(int(intervalosesq[j])))
			if -1 <= intervalosdir[j] <= 0:
				difdire = (len(str(int(maxinter))) - len(str(int(intervalosdir[j])))) - 1
			else:
				difdire = (len(str(int(maxinter))) - len(str(int(intervalosdir[j]))))
			#Se j == 0, é a primeira vez executando o comando for
			#Então é preciso imprimir o título das seções em seus devidos lugares
			if j == 0:
				#Utilizando como base os espaçamentos entre os números nos comandos abaixo
				#Tem-se o espaçamento aproximado onde o título das seções devem ficar
				print ("Intervalo"," "*(difesq+12+len(str(int(intervalosesq[j])))+difdire+len(str(int(intervalosdir[j])))),"Frequência","        ", "Gráfico")
			#Impressão das colunas dos intervalos com os espaçamentos adequados para que a coluna esteja alinhada
			#Não importando o tamanho do número
			print(" "*difesq,"%.3f" %intervalosesq[j],"A"," "*difdire ,"%.3f" %intervalosdir[j], end="")
			#Impressão da frequência com o espaçamento adequado
			print(" "*(diffreq+12), cont[j], end="")
			#Impressão do espaço entre a frequência e o gráfico do intervalo da linha
			print("               ", end ="")
			#Ajuste no gráfico caso a frequência tenha um valor maior do que 100
			#Para que o gráfico fique proporcional
			if maxfreq > 100:
				cont[j] = round(100 * cont[j] / maxfreq)
			#Impressão do gráfico que repete conforme a frequência
			for u in range (cont[j]):
				print("\u25a0", end="")
			#Pula uma linha para que o próximo for seja não seja impresso na mesma linha
			print()
main()
			