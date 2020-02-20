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

	for l in range (len(mat)):
		for u in range (2,8):
			if mat[l][u] > 60 or mat[l][u] < 1:
				print("Os números apresentados no arquivo devem estar entre 1 e 60. Tente novamente com um arquivo válido.")
				main()



	arq.close()
	return mat

def pergunta1e2 (matriz):
	p1 = [0]*60
	for j in range(60):
		for i in range(2,8):
			for a in range (len(matriz)):
				if matriz[a][i] == (j+1):
					p1[j] = p1[j] + 1
	p12 = [0]*60
	for k in range(60):
		p12[k] = p1[k]
	p1.sort()
	p1.reverse()
	print()
	print("Sorteios por número (ordem decrescente)")
	print()
	print(" Números     Sorteios")
	for g in range(60):
		print("%5d %12d" %((p12.index(p1[g])+1), (p1[g])))
		p12[p12.index(p1[g])] = 0

def pergunta3e4 (matriz):
	print()
	print("Data mais recente que cada número foi sorteado")
	print()
	print(" Números     Sorteios         Data")
	print()
	p14 = [0]*len(matriz)
	for y in range (len(matriz)):
		p14[y] = matriz[y][2:8]
	for t in range (len(p14)):
		p14[t].sort()
	for q in range (len(p14)):
		for u in range (6):
			if p14[q][u] != 0:
				apareceprim = p14[q][u]
				print ("%5d %12d" %(p14[q][u], matriz[q][0]), end="")
				print("        ", matriz[q][1])
				p14[q][u] = 0
				for t in range (len(p14)):
					for b in range (6):
						if p14[t][b] == apareceprim:
							p14[t][b] = 0

	
def main():
	nomearq = str(input("Entre com o nome do arquivo:"))
	matt = LeiaMatriz(nomearq)
	pergunta1e2(matt)
	pergunta3e4(matt)
	exit()
main()

