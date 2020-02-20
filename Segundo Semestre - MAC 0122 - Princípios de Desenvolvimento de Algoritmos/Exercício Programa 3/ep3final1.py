#mporta o time para calcular o tempo de cada algoritmo
import time

#Função principal
def main():
    while True:
        #Recebe o nome do arquivo de origem
        #Os testes que estão no diretório
        narqo = str(input("Entre com o nome do arquivo origem: "))
        #recebe o nome do arquivo de destino a ser criado
        narqd = str(input("Entre com o nome do arquivo destino: "))
        #O programa termina quando o usuário digita sair
        if (narqd == "sair" or narqo == "sair") or (narqd == "Sair" or narqo == "Sair") or (narqd == "SAIR" or narqo == "SAIR"):
            return
        #Quantos registros o usuário quer classificar
        registrosclass = int(input("Quantidade de registros a classificar: "))
        #Gera uma tabela com cada linha do arquivo como um elemento string de uma lista
        TAB = CriaTAB(narqo)
        #Gera uma lista com sublistas, sendo cada uma delas as linhas do arquivo.txt
        #Essas sublistas tem como como elementos -> [....['nome', dia, mes, ano, ident]....]
        TAB = CriaTAB3(TAB, registrosclass)
        #Começa a contar o tempo do Quick Sort recursivo
        tempo1 = time.perf_counter()
        #Faz a classificação com o Quick Sort recursivo
        finalqsr = ClassQuickRecursivo(TAB)
        #Termina de contar do tempo do Quick Sort recursivo
        tempo2 = time.perf_counter()
        #Chama a função que verifica se a classificação está correta
        VerifClass(finalqsr)
        #Coemeça a contar o tempo do sort()
        tempo3 = time.perf_counter()
        #Faz a classificação com o sort()
        finals = classMetodoSort(TAB)
        #Termina de contar o tempo do sort()
        tempo4 = time.perf_counter()
        #Verifica se a classificação está correta
        VerifClass(finals)
        #Começa a contar o tempo do Quick Sort iterativo (não recursivo)
        tempo5 = time.perf_counter()
        #Faz a classificação com o Quick Sort não recursivo
        finalqsnr = ClassQuickRecursivo(TAB)
        #Termina de contar o tempo
        tempo6 = time.perf_counter()
        #Verifica se a classificação está correta
        VerifClass(finalqsnr)
        #Cria o novo arquivo para escrever as informações classificadas
        #Usei a lista final do Quick Sort recursivo para escrever
        #Já que todas teoricamente dão a mesma coisa, não vejo necessidadade de escrever as informações das três
        CriaArqDest(narqd, finalqsr)
        #Imprime o tempo que cada método demorou para classificar a tabela
        print("Tempo para classificar a tabela:")
        print("Método Quick Recursivo:", tempo2-tempo1, "segundos")
        print("Método Quick Não Recursivo:", tempo6-tempo5, "segundos")
        print("Método sort() do Python:", tempo4-tempo3, "segundos")

#Função que cria o arquivo de destino com o nome dado e passa todas as informações
def CriaArqDest (nomedoarquivo, lista):
    arqdest = open(nomedoarquivo, "w")
    linhas = ""
    for a in range(len(lista)):
        for b in range(5):
            linha = lista[a][b]
            linha2 = str(linha)
            if b == 2:
                linhas = linhas + "/" + linha2
            elif b == 3:
                linhas = linhas + "/" + linha2 + ","
            elif b == 1:
                linhas = linhas + linha2
            elif b == 4:
                linhas = linhas + linha2
            else:
                linhas = linhas + linha2 + ","
        arqdest.write(linhas+"\n")
        linhas = ""
    
                 

#Função que cria a tabela TAB com cada linha do arquivo como um elemento da lista
def CriaTAB (narqo):
    arq = open(narqo, "r")
    TAB = [line.rstrip('\n') for line in arq]
    return TAB

#Gera uma lista com sublistas, sendo cada uma delas as linhas do arquivo.txt
#Essas sublistas tem como como elementos -> [....['nome', dia, mes, ano, ident]....]
def CriaTAB3 (TAB, registrosclassificar):
    TAB2 = []
    for k in range (registrosclassificar):
        a = TAB[k].split(",")
        TAB2.append(a)
    nomes = [TAB2[i][0] for i in range (len(TAB2))]
    datas = [TAB2[j][1] for j in range (len(TAB2))]
    idd = [int(TAB2[l][2]) for l in range (len(TAB2))]
    ab = []
    for a in range(len(datas)):
        ab.append(datas[a].split("/"))
    for c in range (len(ab)):
        for d in range(3):
            ab[c][d] = int(ab[c][d])
    TAB3 = [[0,0,0,0,0] for i in range(len(TAB2))]
    for h in range (len(TAB2)):
        TAB3[h][0] = nomes[h]
        TAB3[h][1] = ab[h][0]
        TAB3[h][2] = ab[h][1]
        TAB3[h][3] = ab[h][2]
        TAB3[h][4] = idd[h]
    return TAB3

#Função que classifica a tabela usando o Quick Recursivo
def ClassQuickRecursivo (TAB):
    #Classifica os nomes
    classn = QuickSort_IndexRecursivo(TAB, 0)
    a = 0
    #A partir daqui se verifica as prioridades (datanasc e ident) caso os nomes são iguais
    while a+1 < len(classn):
        ind = 0
        if classn[a][0] == classn[a+1][0]:
            k = a+1
            while k < len(classn)and classn[a][0] == classn[k][0]:
                ind = k
                k += 1
            for g in range (1,ind+1):
                if a+g < len(classn):
                    if classn[a][0] == classn[a+g][0] and classn[a][3] != classn[a+g][3]:
                        classndataano = QuickSort_IndexRecursivo([classn[a], classn[a+g]], 3)
                        classn[a], classn[a+g] = classndataano[0], classndataano [1]
                    elif classn[a][0] == classn[a+g][0] and classn[a][2] != classn[a+g][2]:
                        classdatames = QuickSort_IndexRecursivo([classn[a], classn[a+g]], 2)
                        classn[a], classn[a+g] = classdatames[0], classdatames [1]
                    elif classn[a][0] == classn[a+g][0] and classn[a][1] != classn[a+g][1]:
                        classdatadia = QuickSort_IndexRecursivo([classn[a], classn[a+g]], 1)
                        classn[a], classn[a+g] = classdatadia[0], classdatadia [1]
                    elif classn[a][0] == classn[a+g][0] and classn[a][4] != classn[a+g][4]:
                        classid = QuickSort_IndexRecursivo([classn[a], classn[a+g]], 4)
                        classn[a], classn[a+g] = classid[0], classid[1]
        a += 1
    return classn

#Função que classifica a tabela usando o sort()
def classMetodoSort(TAB):
    #Classifica pelo nome
    classn2 = Sort(TAB, 0)
    a = 0
    #A partir daqui se verifica as prioridades (datanasc e ident) caso os nomes são iguais
    while a+1 < len(classn2):
        ind = 0
        if classn2[a][0] == classn2[a+1][0]:
            k = a+1
            while k < len(classn2) and classn2[a][0] == classn2[k][0]:
                ind = k
                k += 1
            for g in range (1,ind+1):
                if a+g < len(classn2):
                    if classn2[a][0] == classn2[a+g][0] and classn2[a][3] != classn2[a+g][3]:
                        classndataano = Sort([classn2[a], classn2[a+g]], 3)
                        classn2[a], classn2[a+g] = classndataano[0], classndataano [1]
                    elif classn2[a][0] == classn2[a+g][0] and classn2[a][2] != classn2[a+g][2]:
                        classdatames = Sort([classn2[a], classn2[a+g]], 2)
                        classn2[a], classn2[a+g] = classdatames[0], classdatames [1]
                    elif classn2[a][0] == classn2[a+g][0] and classn2[a][1] != classn2[a+g][1]:
                        classdatadia = Sort([classn2[a], classn2[a+g]], 1)
                        classn2[a], classn2[a+g] = classdatadia[0], classdatadia [1]
                    elif classn2[a][0] == classn2[a+g][0] and classn2[a][4] != classn2[a+g][4]:
                        classid = Sort([classn2[a], classn2[a+g]], 4)
                        classn2[a], classn2[a+g] = classid[0], classid[1]
        a += 1
    return classn2

#Função que classifica a tabela usando o Quick Sort não recursivo
#Não consegui adaptar o Quick Sort não recursivo para listas dentro de listas
#Então, só classifica o nome
def ClassQuickNaoRecursivo (TAB):
    QuickSortNonRecursive(TAB)
    return TAB

#Função do Quick Sort recursivo adaptada para sublistas (usa o index que quer priorizar)
def QuickSort_IndexRecursivo(lst, index):
    if len(lst) == 0:
        return []
    else:
        pivot = lst[0]
        lesser = QuickSort_IndexRecursivo([x for x in lst[1:] if x[index] < pivot[index]], index)
        greater =  QuickSort_IndexRecursivo([x for x in lst[1:] if x[index] >= pivot[index]], index)
        return lesser + [pivot] + greater

#Função do sort() adaptado para sublistas, usando o index que quer priorizar para classificar
def Sort(sub_li, index): 
    sub_li.sort(key = lambda x: x[index]) 
    return sub_li

#Função do Quick Sort não recursivo que não consegui adaptar para sublistas e indexes específicos
def QuickSortNonRecursive (TAB):
    pilhaa = PilhaLista()
    pilhaa.push((0, len(TAB) - 1)) 
    while not pilhaa.is_empty(): 
        inicio, fim = pilhaa.pop() 
        if fim - inicio > 0: 
            k = particiona(TAB, inicio, fim)                         
            pilhaa.push((inicio, k - 1))             
            pilhaa.push((k + 1, fim))
#Função particiona do Quick Sort não recursivo
def particiona(lista, inicio, fim):
    i, j = inicio, fim 
    pivo = lista[fim] 
    while True:         
        while i < j and lista[i] <= pivo: i = i + 1         
        if i < j:             
            lista[i], lista[j] = pivo, lista[i] 
        else: break                 
        while i < j and lista[j] >= pivo: 
            j = j - 1         
        if i < j: lista[i], lista[j] = lista[j], pivo        
        else: break    
    return i 
  
     
#Função que verifica se as classificações estão corretas
def VerifClass(TAB):
    for a in range(len(TAB)):
        #Testando os nomes
        if a+1 < len(TAB) and TAB[a][0]<TAB[a+1][0]:
            continue
        if a+1 < len(TAB) and TAB[a][0]>TAB[a+1][0]:
            print ("Há nomes na ordem incorreta.")
            return
        #Se os nomes são iguais
        #Testa para a datanasc e o ident
        #Mesmo estilo do Quick Sort recursivo e do sort()
        ind = 0
        if a+1 < len(TAB) and TAB[a][0] == TAB[a+1][0]:
            k = a+1
            while k < len(TAB) and TAB[a][0] == TAB[k][0]:
                ind = k
                k += 1
            for g in range (1,ind+1):
                if a+g < len(TAB):
                    if TAB[a][0] == TAB[a+g][0] and TAB[a][3] != TAB[a+g][3]:
                        if TAB[a+g][3]>TAB[a][3]:
                           pass
                        else: 
                            print("Há erro(s) na classificação -", nome)
                            return
                    elif TAB[a][0] == TAB[a+g][0] and TAB[a][2] != TAB[a+g][2]:
                        if TAB[a+g][2]>TAB[a][2]:
                            pass
                        else:
                            print("Há erro(s) na classificação -", nome)
                            return
                    elif TAB[a][0] == TAB[a+g][0] and TAB[a][1] != TAB[a+g][1]:
                        if TAB[a+g][1]>TAB[a][1]:
                            pass
                        else:
                            print("Há erro(s) na classificação -", nome)
                            return
                    elif TAB[a][0] == TAB[a+g][0] and TAB[a][4] != TAB[a+g][4]:
                        if TAB[a+g][4]>TAB[a][4]:
                            pass
                        else:
                            print("Há erro(s) na classificação -", nome)
                            return
                    elif TAB[a][0] == TAB[a+g][0] and TAB[a][3] == TAB[a+g][3] and TAB[a][2] == TAB[a+g][2] and TAB[a][1] == TAB[a+g][1] and TAB[a][4] == TAB[a+g][4]:
                        pass
                    elif TAB[a][0] == TAB[a+g][0]:
                        print("Há erro(s) na classificação -", nome)
                        return

#Pilha usada no Quick Sort não recursivo
class PilhaLista:
    def __init__(self):         
         self._pilha = []
    def __len__ (self):         
        return len(self._pilha)
    def push(self, e):
        self._pilha.append(e) 
    def is_empty(self):         
        return len(self._pilha) == 0 
    def top(self):         
        if self.is_empty( ):             
            raise Empty("Pilha vazia")        
        self._pilha[-1] 
    def pop(self):         
        if self.is_empty( ):             
            raise Empty("Pilha vazia")         
        return self._pilha.pop( ) 

#Executa o programa
main()
