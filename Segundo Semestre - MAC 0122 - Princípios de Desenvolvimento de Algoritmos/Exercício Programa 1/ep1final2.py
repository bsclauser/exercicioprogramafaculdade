#Importa o módulo de tempo
#Para calcular o tempo decorrido das soluções
import time

#Função que recebe o arquivo de texto e devolve uma lista 9x9 ou uma lista vazia
def LeiaMatrizLocal(NomeArquivo):
	#Retorna a matriz lida se ok ou uma lista vazia senão 
	#Abrir o arquivo para leitura
	try:
		arq = open(NomeArquivo, "r") 
	except:
		 return [] #Retorna lista vazia se deu erro 
	#Inicia matriz SudoKu a ser lida 
	mat = [9 * [0] for k in range(9)] 
	#Ler cada uma das linhas do arquivo 
	i = 0 
	for linha in arq:
		 v = linha.split() 
		 #Verifica se tem 9 elementos e se são todos entre '1' e '9' 
		 valorinvalido = 0
         #Verificar se há alguma excessão
		 try:
			 for a in range(len(v)):
				 if int(v[a])>9 or int(v[a])<0:
                     #Se valorinvalido for > 0
                     #Elementos não zero fora do intervalo [1,...,9]
					 valorinvalido += 1
		 except: 
             #Se houver valores que não sejam inteiros
             #Imprime a seguinte mensagem ao usuário
			 print("Matriz inválida. Valor(es) não inteiro(s) na matriz. Tente novamente com uma matriz válida.")
			 return None
        #Mensagem personalizada para quando a lista não tem 9 elementos por linha
        #Valores não zeros não estão entre 1 e 9
		 if len(v) != 9 and valorinvalido != 0:
			 print("Matriz inválida. Matriz não possui 9 elementos por linha e seus valores não se encontram entre 1 e 9. Tente novamente com uma matriz válida.")
			 arq.close()
			 return None
        #Mensagem personalizada para quando a lista não tem 9 elementos por linha
		 elif len(v) != 9:
			 print("Matriz inválida. Não há nove elementos por linha da matriz. Tente novamente com uma matriz válida.")
			 arq.close()
			 return None
        #Mensagem personalizada para quando a lista possui valores não zeros que não estão entre 1 e 9
		 elif valorinvalido != 0:
			 print("Matriz inválida. Há valores que não se encontram entre 1 e 9 nas linhas da matriz. Tente novamente com uma matriz válida.")
			 arq.close()
			 return None
		 #Transforma de texto para int 
		 for j in range(len(v)): 
			  mat[i][j] = int(v[j]) 
		 #Faz as consistências iniciais da matriz dada 
         #Chama a função TestaMatrizLida
		 resultado = TestaMatrizLida(mat)
         #TestaMatrizLida retorna True caso seja consistente 
         #False caso contrário
		 if resultado == False:
             #Se não for consistente
             #Imprime mensagem de invalidez ao usuário
			 print("Matriz inváldia. Há valores repetidos nos quadrados interiores da matriz. Tente novamente com uma matriz válida.")
			 return None
		 i = i + 1
    
	#Fechar arquivo e retorna a matriz lida e consistida 
	arq.close()
    #Retorna a matriz 9x9 se deu tudo certo
	return mat

#Função que verifica todas as condições inciais de um Sudoku
def TestaMatrizLida(mat):
    #Verifica se não tem elementos repetidos nas linhas
	#Consistência das linhas
	linhas = [0]*9
	for a in range(9):
		for b in range(9):
			linhas[b] = mat[a][b]
		for c in range(1,10):
			cont1 = linhas.count(c)
			if cont1 > 1:
				return False
    #Verifica se não tem elementos repetidos nas colunas
	#Consistência das colunas
	colunas = [0]*9
	for d in range(9):
		for e in range(9):
			colunas[e] = mat[e][d]
		for f in range(1,10):
			cont2 = colunas.count(f)
			if cont2 > 1:
				return False
    #Verifica se não tem elementos repetidos nos quadrados internos 3x3
	#Consistência dos quadradrados
    #Chama a função Quadrados que retorna todas as matrizes 3x3 da matriz 9x9 em uma lista
	quadradosn = Quadrados(mat)
	soma = 0
	for h in range(9):
		for g in range(1,10):
			j = 0
			soma = quadradosn[h][j].count(g) + quadradosn[h][j+1].count(g) + quadradosn[h][j+2].count(g)
			if soma > 1:
				return False
    #Retorna True se a matriz é consistente
	return True

#Função que devolve todas as matrizes 3x3 da matriz 9x9 
def Quadrados(mat):
    #Inicializa as listas 3x3
    #Os quadrados foram numerados da esquerda para direita, linha por linha
	quadrado1, quadrado2, quadrado3, quadrado4, quadrado5, quadrado6, quadrado7, quadrado8, quadrado9 =  [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)]
	#Varre a matriz 9x9
    #Dependendo dos índices, armazena os valores da matriz 9x9 em seu quadrado correspondente
	for h in range (9):
		for y in range (9):
			if h >= 0 and h <=2:
			    if y >= 0 and y <= 2:
				    quadrado1[h][y] = mat[h][y]
			    if y >= 3 and y <= 5:
				    quadrado2[h][y-3] = mat[h][y]
			    if y >= 6 and y <= 8:
				    quadrado3[h][y-6] = mat[h][y]
			elif h >= 3 and h <= 5:
				if y >= 0 and y <= 2 :
					quadrado4[h-3][y] = mat[h][y]
				if y >= 3 and y <= 5:
					quadrado5[h-3][y-3] = mat[h][y]
				if y >= 6 and y <= 8:
					quadrado6[h-3][y-6] = mat[h][y]
			elif h >= 6 and h <= 8:
				if y >= 0 and y <= 2 :
					quadrado7[h-6][y] = mat[h][y]
				if y >= 3 and y <= 5:
					quadrado8[h-6][y-3] = mat[h][y]
				if y >= 6 and y <= 8:
					quadrado9[h-6][y-6] = mat[h][y]
    #Retorna todos os quadrados 3x3
	return quadrado1, quadrado2, quadrado3, quadrado4, quadrado5, quadrado6, quadrado7, quadrado8, quadrado9

#Função que verifica se um número d está na linha L
def ProcuraElementoLinha (Mat, L, d):
	for s in range(9):
		if Mat[L][s] == d:
            #Se estiver, retorna sua coluna
			return s
    #Senão, retorna -1
	return -1

#Função que verifica se um número d está na coluna C
def ProcuraElementoColuna (Mat, C, d):
	for p in range(9):
		if Mat[p][C] == d:
            #Se estiver, retorna sua linha
			return p
    #Senão, retorna -1
	return -1

#Função que verifica se um número p está em um determinado quadrado 3x3
#Dependendo da sua posição
def ProcuraElementoQuadrado (Mat, L, C, p):
	ln = (L//3)*3
	cn = (C//3)*3
	for i in range(ln,ln+3):
		for j in range(cn,cn+3):
			if Mat[i][j]== p:
				return (i,j)
	return -1

#Função que faz a consistência da matriz preenchida
def TestaMatrizPreenchida(Matriz): 
    #Chama a função TestaMatrizLida que faz todas as consistências
	a = TestaMatrizLida(Matriz)
	if a:
        #Se for consistente, retorna True
		return True
    #Senão, retorna False
	return False

#Função que verifica qual a próxima posição vazia da matriz
def TemZero(matriz):
	elementoszero = 0
    #Varre a matriz 9x9
	for a in range(9):
		for b in range(9):
            #Se achar uma posição vazia
			if matriz[a][b] == 0:
                #Altera valor de elementoszero
				elementoszero = 1
                #Retorna os índices da posição vazia
                #Retorna elementoszero = 1 apenas representando que há uma posição vazia
				return [a,b,elementoszero]
    #Se não houver mais nenhuma posição vazia
    #Retorna [-1,-1]
	return [-1,-1]

#Função que testa se é possível adicionar um número val em uma certa posição
#Satisfazendo as consistências da matriz
def TestaValor(Mat, linha, coluna, val):
    #Verifica se val já está na coluna
	col = ProcuraElementoColuna(Mat, coluna, val)
    #Verifica se val já está na linha
	lin = ProcuraElementoLinha(Mat, linha, val)
    #Verifica se val já está no quadrado 3x3
	qua = ProcuraElementoQuadrado(Mat, linha, coluna, val)
    #Se todas as funções acima retornarem -1
	if col == -1 and lin == -1 and qua == -1:
        #Podemos colocar val em [linha,coluna]
		return True
    #Senão, False
	return False

#Função que verifica se a solução para o Sudoku foi encontrada
def AchouSolucao(mat):
    #Verifica se não existem mais posições vazias
    #Verifica se a matriz é consistente
	if TemZero(mat) == [-1,-1] and TestaMatrizPreenchida(mat) == True:
        #Se for, true
		return True
    #Se não, False
	return False

#Variável global que conta quantas soluções encontramos para o Sudoku do input
contadorsol = 0

#Função que resolve o Sudoku
def Sudoku(Mat):
    #Declara que vamos utilizar a variável global contadorsol
	global contadorsol
    #Verifica se achamos a solução
	if AchouSolucao(Mat):
        #Se sim, True
		return True
    #Senão, vamos tentar encontrar a solução
	else:
        #a recebe o valor retornado pela função TemZero
		a = TemZero(Mat)
        #Por estarmos no else, sabemos que TemZero não retorna [-1,-1]
        #Então, armazenamos a linha e coluna da próxima posição vazia em Lin e Col
		Lin = a[0]
		Col = a[1]
        #Fazemos um for que assume o valor de todos os candidatos possíveis para a posição vazia
		for p in range(1,10):
            #Chamamos a função TestaValor para sabermos se podemos colocar p na posição vazia
			if TestaValor(Mat, Lin, Col, p):
                #Se ela retornar True, podemos
                #Então, a posição vazia recebe o número p
				Mat[Lin][Col] = p
                #Backtracking
                #Faz uma chamada recursiva
                #Verifica se encontramos a solução para o Sudoku
				if Sudoku(Mat):
                    #Se sim, adicionamos um ao contadorsol global
					contadorsol += 1
                    #Realizamoa a impressão do Sudoku preenchido
					print()
					print("*** Matriz Completa ***")
					ImprimaMatriz(Mat)
					print()
					print("*** Matriz Completa e Consistente ***")
                #Backtracking
                #Apaga o número colocado na posição vazia e tenta novamente
				Mat[Lin][Col] = 0
        #Se ela chegar aqui, significa que não retornou True em nenhuma situação
        #Ou seja, não foi econtrada uma solução
		return False

#Função que imprime uma matriz de maneira organizada e sem os colchetes
def ImprimaMatriz (Mat):
	print()
	for a in range(9):
		for b in range(9):
            #Quanto chega ao nono elemento de cada linha
            #Pulamos linha
			if b == 8:
				print (Mat[a][b])
            #O resto escrevemos na mesma linha
			else:
				print (Mat[a][b], " ", end = " ")

sair = 0
#Função principal 
def main():
    global sair
    #Enquanto sair é 0, o programa continua rodando e pedindo novos arquivos
    while sair == 0:
        #Declara que vamos utilizar a variável global contadorsol
        global contadorsol
        #Solicita o input do usuário
        #Nome do arquivo de texto
        arqentrada = str(input("Entre com o nome do arquivo:"))
        #Opção para terminar o programa
        #Se usuário digitar SAIR o programa acaba
        if arqentrada == "SAIR":
            #Altera o valor de sair
            sair = 1
            #Sai do While, o qual não vai mais ser True
            break
        #Chama a função LeiaMatrizLocal
        #A variável matrizsudoku recebe o valor retornado por LeiaMatrizLocal
        matrizsudoku = LeiaMatrizLocal(arqentrada)  
        #Se matrizsudoku recebeu None
        #Temos uma matriz inválida                                                                                                                                                                                                                                                                                                                                                            
        if matrizsudoku == None:
            #Começa o programa novamente
            #Solicita um novo input
            print("Caso queira sair do programa, digite SAIR.")
            main()
        #Se matrizsudoku recebeu []
        #Nome do arquivo de texto inválido
        elif matrizsudoku == []:
            #Imprime mensagem dando a usuário a opção de terminar o programa
            print("Nome do arquivo de texto inválido. Tente novamente com um arquivo de texto válido.")
            print("Caso queira sair do programa, digite SAIR.")
            #Começa o programa novamente
            #Solicita novo input
            main()
        #Se chegou aqui, quer dizer matrizsudoku recebeu uma matriz 9x9 válida
        else:
            #Realizamos a impressão da matriz inicial
            print("*** Matriz Inicial ***")
            #Chama função ImprimaMatriz
            ImprimaMatriz(matrizsudoku)
            #Começa a contar o tempo decorrido antes do início da solução
            #Na comanda o EP, o professor utilizou time.clock()
            #Mas como este comando será descontinuado, preferi usar um mais atualizado
            tempo1 = time.perf_counter()
            #Chama a função Sudoku que resolve as matrizes
            sol = Sudoku(matrizsudoku)
            #Termina a contagem do tempo decorrido depois de ter encontrado todas ou nenhuma solução
            tempo2 = time.perf_counter()
            #Calcula o tempo decorrido
            tempodecorrido = tempo2 - tempo1
            #Se sol receber o valor False e contadorsol > 1, a função Sudoku imprimiu todas as soluções possíveis
            if sol == False and contadorsol > 0:
                print()
                #Imprimimos o tempo decorrido
                print("Tempo decorrido:",tempodecorrido,"segundos")
                #Verifica se contadorsol é igual ou diferente de um
                #Apenas para saber se imprime "solução" ou "soluções"
                if contadorsol == 1:
                    print("Esta matriz possui",contadorsol,"solução.")
                    print()
                else: 
                    print("Esta matriz possui",contadorsol,"soluções.")
                    print()
            #Se contadorsol é igual a 0, então não encontramos nenhuma solução, e, obviamente, sol recebeu False
            elif contadorsol == 0:
                print()
                #Informa o usuário que não tem solução
                print("A matriz informada não possui solução.")
                #Imprime tempo decorrido
                print("Tempo decorrido:",tempodecorrido,"segundos.")
                print()
            contadorsol = 0


#Executa a função main(), e, consequentemente, todo o programa
main()