#Função que lê a matriz dada pela comanda do EP
def LeiaMatriz (NomeArquivo):
	mat = []
	try:
		arq = open(NomeArquivo, "r")
	except:
		print("Erro na abertura do arquivo (open).")
		return None
	i = 0
	for linha in arq:
		try:
			lin = linha[:len(linha)-1]
			v = lin.split('\t')
			mat.append([])
			for j in range (8):
				if j == 1:
					mat[i].append(v[1])
				else:
					mat[i].append(int(v[j]))
			i += 1
		except:
			print ("Erro no split(), no int() ou no append().")
			return None
    #Consistência dos valores da matriz
    #Precisam estar entre 1 e 60, ou seja, [1,60]
	for l in range (len(mat)):
		for u in range (2,8):
			#Caso não estejam no intervalo [1,60], o nome do arquivo é solicitado novamente
			#Por meio da execução da função main()
			if mat[l][u] > 60 or mat[l][u] < 1:
				print("Os números apresentados no arquivo devem estar entre 1 e 60. Tente novamente com um arquivo válido.")
				main()



	arq.close()
	return mat


#Função que responde as perguntas 1 e 2 da comanda do EP
def pergunta1e2 (matriz):
	#Cria uma lista com 60 elementos
	#Todos eles iguais a 0
	p1 = [0]*60
	#Faz a contagem de quantas vezes os números de 1 a 60 foram sorteados
	#E armazena a contagem na lista p1
	for j in range(60):
		for i in range(2,8):
			for a in range (len(matriz)):
				#A partir da matriz parâmetro
				#Caso algum elemento dela seja igual a j (entre 1 e 60)
				if matriz[a][i] == (j+1):
					#Adiciona 1 a p1[j]
					#Que vai servir como contador a partir do index
					#Ou seja, o index 0 indica o número 1
					#O valor no index 0 indica quantas vezes o número 1 foi sorteado
					p1[j] = p1[j] + 1
	#Cria uma segunda lista p12 com 60 elementos, todos iguais a 0
	p12 = [0]*60
	#Armazena os dados de p1 em p12
	for k in range(60):
		p12[k] = p1[k]
	#Ordena p1
	p1.sort()
	#Coloca em ordem decrescente
	p1.reverse()
	#Imprime o cabeçalho
	print()
	print("Sorteios por número (ordem decrescente)")
	print()
	print(" Números     Sorteios")
	#Imprime os números sorteados
	#E o número de vezes que foram sorteados
	#Em ordem decrescente
	for g in range(60):
		print("%5d %12d" %((p12.index(p1[g])+1), (p1[g])))
		#Zera o número que já foi impresso para não acontecer repetições
		p12[p12.index(p1[g])] = 0


#Função que responde as perguntas 3 e 4 da comanda do EP
def pergunta3e4 (matriz):
	#Imprime ccabeçalho
	print()
	print("Data mais recente que cada número foi sorteado")
	print()
	print(" Números     Sorteios         Data")
	print()
	#Cria uma matriz do tamanho da matriz parâmetro
	#Com elementos iguais a zero
	p14 = [0]*len(matriz)
	#Armazena nela os números sorteados
	for y in range (len(matriz)):
		p14[y] = matriz[y][2:8]
	#Ordena os elementos das sublistas em p14
	#Ordena os números sorteados em cada sorteio em ordem crescente
	for t in range (len(p14)):
		p14[t].sort()
	#Imprime o número sorteado, o sorteio e a data em que foi sorteado
	for q in range (len(p14)):
		for u in range (6):
			if p14[q][u] != 0:
				apareceprim = p14[q][u]
				print ("%5d %12d" %(p14[q][u], matriz[q][0]), end="")
				print("        ", matriz[q][1])
				#Zera o número que foi impresso
				p14[q][u] = 0
				#Zera todos os outros iguais que vem depois dele
				#Assim não acontece repetições
				#E imprime apenas o que foi sorteado na data mais recente
				for t in range (len(p14)):
					for b in range (6):
						if p14[t][b] == apareceprim:
							p14[t][b] = 0



#Função principal do programa
def main():
	#Solicita o nome do arquivo
	nomearq = str(input("Entre com o nome do arquivo:"))
	#Chama a função LeiaMatriz e armazena a matriz mat na variável matt caso o arquivo passe pela consistência
	matt = LeiaMatriz(nomearq)
	#Chama a função pergunta1e2 usando a variável matt como parâmetro
	pergunta1e2(matt)
	#Chama a função pergunta3e4 usando a variável matt como parâmetro
	pergunta3e4(matt)
	#Força o término do programa
	#Sem o exit(), a mensagem de erro na consistência da função LeiaMatriz continuaria a aparecer 
	#Juntamente com a solicitação de um novo nome de arquivo
	exit()
main()

