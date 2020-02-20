#Importar a classe que está no arquivo pilha.py dentro da pasta classe do diretório
from classe.pilha import PilhaNot

#Função que traduz a expressão da forma infixa para a pós-fixa
def TraduzPosFixa(expn):
    #Declaração das variáves globais utilizadas
    global num
    global letras
    #Criação de dicionário com a prioridade de cada operação
    #Quanto maior o valor, maior a prioridade
    prior = {}
    prior["#"] = 5
    prior["_"] = 5
    prior["**"] = 4
    prior["*"] = 3
    prior["/"] = 3
    prior["+"] = 2
    prior["-"] = 2
    prior["("] = 1
    prior[")"] = 1
    prior["="] = 0
    #Lista que vai receber a expressão em notação pós-fixa
    novalista = []
    #Uso da classe
    pilha = PilhaNot()
    #Para cada token/elemento na lista com as expressão infixa
    for token in expn:
        #Se o tamanho dele for maior que um, porém diferente de "**", temos uma número ou variável com mais de um dígito (Ex: 45, ab) ou um número com um operador unário (Ex: -2)
        if len(token)>1 and token != "**":
            #Começamos um contador para sabermos com qual dos casos estamos lidando
            cont = 0
            #Fazemos um for que percorre cada dígito do token
            for a in range (len(token)):
                #Se for um número ou uma variável com mais de um dígito
                if token[a] in letras or token[a] in num:
                    #Adiciona um ao contador
                    #Neste caso, no final do for, esperamos que o valor do contador seja igual ao tamanho
                    cont += 1
                #Se um dígito da variável ou do número é um dos operadores binários (+ ou -)
                elif "-" in token[a] or "+" in token[a]:
                    #Adiciona o número à lista que terá que a notação pós-fixa
                    novalista.append(token[1])
                    #Se o operador unário for "-"
                    if token[0] == "-":
                        #Trocamos por "_" para sabermos que é um sinal de menos unário
                        pilha.push("_")
                    #Se o operador unário for "+"
                    elif token [0] == "+":
                        #Trocamos por "#" para sabermos que é um sinal de mais unário
                        pilha.push("#")
            #Conferimos se o valor do contador é igual ao tamanho
            if cont == len(token):
                #Se sim, adicionamos a variável/número à lista que terá a notação pós-fixa
                novalista.append(token)
        #Se o token tiver um tamanho igual a 1 e ele for uma variável ou um número
        elif token in letras or token in num:
            #Adicionamos a variável/número à lista que terá a notação pós-fixa
            novalista.append(token)
        #Caso seja uma abertura de parênteses
        elif token == "(":
            #Adicionamos normalmente à lista final
            pilha.push(token)
        #Caso seja o fechamento de parênteses
        elif token == ")":
            #Retira ele
            toptoken = pilha.pop()
            #Retiramos todos os elementos até chegar na abertura de parênteses
            #Ou seja, retiramos todos os elementos que estavam dentro do parenteses
            while toptoken != "(":
                novalista.append(toptoken)
                toptoken = pilha.pop()
        #Se não for nenhum dos casos acimas, temos operadores
        else:
            #Verificamos se a lista não está vazia e a prioridade dos operadores
            #Adicionamos eles à lista de acordo com a prioridade
            while (not pilha.is_empty()) and (prior[str(pilha.top())] >= prior[str(token)]):
                novalista.append(pilha.pop())
            pilha.push(token)
    #Enquanto a pilha não estiver vazia
    #Adicionamos à lista o que sobrou
    while not pilha.is_empty():
        novalista.append(pilha.pop())
    #Retorna uma lista com um único elemento, sendo ele a ecpressão pós-fixa
    return " ".join(novalista)

#Variáveis globais
#Lista com as variáveis
tabvar = []
#Lista com o valor das variáveis
tabval = []
#Lista com as expressões que o usuário entrou
listexp =[]

#Função principal do programa
def main():
    #Declara todas as variáveis globais que vamos usar
    global notnum
    global num
    global letras
    global tabvar
    global tabval
    global listexp
    #Repete indefinidamente
    while True:
        #Imprime os ">>>"
        prompts()
        #Recebe o input do usuário
        exp = input()
        #Verifica se o que o usuário digitou não é a variável correspondente a uma expressão
        #Varre a lista com as expressões
        for u in range (len(listexp)):
            if exp == listexp [u][0]:
                #Se estiver nela, realizamos a tradução para a notação pós-fixa
                expposfix = TraduzPosFixa(listexp[u])
                #Calculamos o resultado
                resultado = CalcPosFixa(expposfix)
                #Imprimimos o resultado
                print(resultado)
                #Começamos tudo de novo
                main()
        #Se o que o usuário digitou não corresponde a nenhuma expressão da lista de expressões
        #Varremos o input
        for b in range (len(exp)):
            #Verificamos se não há nenhum caracter inválido
            if (exp[b] not in notnum) and (exp[b] not in num) and (exp[b] not in letras) and (exp[b] != " "):
                #Se houver, imprimimos uma mensagem e começamos o programa de novo
                print("Há caracteres inválidos na expressão. Tente novamente.")
                main()
        #Chamamos a função que cria uma lista do input do usuário na notação infixa
        expre = ListaInfixa(exp)
        #Agora vamos ver se é uma atribuição (Ex: a = 5) ou uma expressão
        #Contador de variáveis
        contvar = 0
        #Contador de números
        contnum = 0
        #Índice da variável
        indvar = 0
        #Índice do número/valor
        indval = 0
        #Varremos a lista da expressão em notação infixa
        for a in range (len(expre)):
            #Se o elemento tiver apenas um dígito
            if len(expre[a]) == 1:
                #E ele for um número
                if expre[a] in num:
                    #Adicionamos 1 ao contador de números
                    contnum += 1
                    #Armazenamos o índice do número na lista
                    indval = a
                #Se for uma variável
                elif expre[a] in letras:
                    #Adicionamos 1 ao contador de variáveis
                    contvar += 1
                    #Armazenamos o índice da variável na lista
                    indvar = a
            #Se o elemento tiver mais de um dígito
            elif len(expre[a])>1:
                #Contador de letras
                contl = 0
                #Contador de números
                contn = 0
                #Varremos os dígitos do elemento
                for c in range (len(expre[a])):
                    #Se for letra
                    if expre[a][c] in letras:
                        #Adiciona 1 ao contador de letra
                        contl += 1
                    #Se for número
                    elif expre[a][c] in num:
                        #Adiciona 1 ao contador de número
                        contn += 1
                #Se o contador de números tiver o mesmo tamanho do elemento (esperado) - Se ele for um número
                if contn == len(expre[a]):
                    #Adicona 1 ao contador de números principal
                    contnum += 1
                    #Armazena o índice do número
                    indval = a
                #Se o contador de letras tiver o mesmo tamanho do elemento (esperado) - Se ele for uma variável
                elif contl == len(expre[a]):
                    #Adiciona 1 ao contador de variáveis principal
                    contvar += 1
                    #Armazena o índice da variável
                    indvar = a
        #Se tivermos apenas uma variável, pelo menos um número e um sinal de igual
        if contvar == 1 and contnum >0 and "=" in expre:
            #Temos uma atribuição
            #Se ela tiver um operador unário (-)
            if expre[indval-1] == "_" or expre[indval-1] == "-":
                #Armazenamos o sinal e o elemento na variável val
                val = "-"+expre[indval]
            #Se ela tiver um operador unário (+)
            elif expre[indval-1] == "#":
                #Armazenamos o sinal e o elemento na variável val
                val = "+"+expre[indval]
            #Se não houver operadores unários
            else:
                #A variável val recebe a localização do valor atribuído
                val = expre[indval]
            #Adicionamos o valor atribuído à lista de valores
            tabval.append(val)
            #Adicionamos a variável correspondente a esse valor
            tabvar.append(expre[indvar])
        #Se não tivermos uma atribuição, temos uma expressão
        else: 
            #Se a lista de valor e a lista de variáveis não estiverem vazias
            #Ou seja, valores de variáveis já foram atribuídos
            if tabval != [] and tabvar != []:
                #Percorremos a expressão
                for e in range (len(expre)):
                    #Percorremos a lista de variáveis
                    for f in range (len(tabvar)):
                        #Se acharmos variáveis iguais
                        if expre[e] == tabvar[f]:
                            #Atribuímos o valor dela
                            expre[e] = tabval[f]
                #Adcionamos a expressão à lista de expressões
                listexp.append(expre)
            else:
                #Se as listas de atribuições estiverem vazias
                #Imprimimos uma mensagem
                print("Você precisa atribuir valores de variáveis antes de calcular expressões. Tente novamente.")
                #Começamos o programa de novo
                main()



#Variáveis globais
#Não-números
notnum = ["**", "*", "/", "+", "-", "=", "(", ")", "_", "#"]
#Números
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#Letras
letras = ["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]

#Função que transforma o input do usuário em uma lista com notação infixa
def ListaInfixa(exp):
    #Declara as variáveis globais
    global notnum
    global num
    global letras
    #Lista que vai receber a notação infixa 
    listafinal = []
    #Varre o input do usuário
    for i in range (len(exp)):
        #Se o elemento for uma letra
        if exp[i] in letras:
            #Se não estivermos no primeiro elemento e o anterior for uma letra não fazemos nada (caso de variável com mais de um dígito)
            if i != 0 and exp[i-1] in letras:
                pass
            #Senão
            else:
                #Pegamos todas as letras que formam o nome da variável
                mesmotipo = []
                while i < (len(exp)) and exp[i] in letras:
                    mesmotipo.append(exp[i])
                    i += 1
                mesmotipo2 = "".join(mesmotipo)
                #Adicionamos a variável à lista final
                listafinal.append(mesmotipo2)
        #Se o elemento for um número
        elif exp[i] in num:
            #Se não estivermos no primeiro elemento e o anterior for um número não fazemos nada (caso de número com mais de um dígito)
            if i != 0 and exp[i-1] in num:
                pass
            #Senão
            else:
                #Pegamos todos os dígitos que formam o número
                mesmotipo3 = []
                while i < (len(exp)) and exp[i] in num:
                    mesmotipo3.append(exp[i])
                    i += 1
                mesmotipo4 = "".join(mesmotipo3)
                #Adicionamos o número à lista final
                listafinal.append(mesmotipo4)
        #Se o elemento não for um número ou letra
        elif exp[i] in notnum:
            #Se houver outro notnum antes dele
            if exp[i-1] in notnum:
                #Temos um operador unário
                #Mas se for um parênteses antes, não temos um operador unário
                if exp[i-1] == ")" and exp[i] == "+":
                    listafinal.append("+")
                elif exp[i-1] == ")" and exp[i] == "-":
                    listafinal.append("-")
                #Trocamos pela representação unária
                elif exp[i] == "-": 
                    listafinal.append("_")
                elif exp[i] == "+": 
                    listafinal.append("#")
                #Se houver dois asteriscos - power, adicionamos à lista normalmente
                elif exp[i] == "*" and exp[i-1] == "*":
                    listafinal.append("**")
                #Se for parênteses, adicionamos à lista normalmente
                elif exp[i] == "(" or exp[i] == ")":
                    listafinal.append(exp[i])
                #Se for divisão, também adicionamos normalmente
                elif exp[i] == "/":
                    listafinal.append(exp[i])
            #Se o item anterior for um número ou uma letra e temos um "*" em seguida, agimos normalmente
            elif ((exp[i-1] in num) or (exp[i-1] in letras)) and exp[i] != "*":
                listafinal.append(exp[i])
            #Se o item da frente não for um notnum, adicionamos normalmente
            elif exp[i+1] not in notnum:
                listafinal.append(exp[i])
            #Se for um "=", adicionamos normalmente
            elif exp[i] == "=":
                listafinal.append(exp[i])
            #Se for um "/", adicionamos normalmente
            elif exp[i] == "/":
                listafinal.append(exp[i])
        #Teremos a lista final
        #Chamamos a função que checa se os sinais unários estão corretos
        listafinal = ChecarLista(listafinal)
    #Retornamos a lista com a expressão em notação infixa
    return listafinal

#Funçãp que checa se os sinais unários estão certos           
def ChecarLista(lista):
    #Declara variável global
    global notnum
    #Se o primeiro elemento for notnum
    #Temos um operador unário
    if lista[0] in notnum:
        #Trocamos para a representação adequada
        if lista[0] == "-": lista[0] = "_"
        elif lista[0] == "+": lista[0] = "#"
    #Varremos a lista
    for a in range (1, len(lista)):
        #Se tivermos um elemento notnum
        if lista[a] in notnum:
            #Verificar se o anterior também é notnum e não é parênteses que fecha
            if lista[a-1] in notnum and lista[a-1] != ")":
                #Verifica se são operadores que podem ser unários (+ ou -)
                #Se forem, troca de representação
                if lista[a] == "-": lista [a] = "_"
                elif lista [a] == "+": lista [a] = "#"
    #Retorna a lista com os operadores unários corretos
    return lista


#Função que imprime os prompts ">>>"
def prompts():
    print(">>> ", end=" ")

#Função que calcula o resultado de uma expressão pós-fixa
def CalcPosFixa(listaexp):
    #Vamos usar pilhas novamente
    pilha2 = PilhaNot()
    #Varremos a lista com notação pós-fixa
    for t in range(len(listaexp)):
        #Se o elemento for um "+"
        if listaexp[t] == "+":
            #Somamos os dois elementos anteriores
            pilha2.push(pilha2.pop() + pilha2.pop())
        #Se o elemento for um "-"
        elif listaexp[t] == "-":
            #Subtraímos os dois elementos anteriores
            oper = pilha2.pop()
            pilha2.push(pilha2.pop() - oper)
        #Se o elemento for um "*"
        elif listaexp[t] == "*":
            #Verificamos se tem outro "*" -> "**"
            #Se for "**", fazemos o pow dos dois elementos anteriores
            if t+1 < (len(listaexp)-1) and listaexp[t+1] == "*":
                oper3 = pilha2.pop()
                oper4 = pilha2.pop()
                pilha2.push(pow(oper4, oper3))
            #Se for "*", fazemos a multiplicação dos dois elementos anteriores
            if (t+1 < (len(listaexp)-1) and listaexp[t+1] != "*" and listaexp[t-1] != "*") or t == (len(listaexp)-1):
                pilha2.push(pilha2.pop() * pilha2.pop())
        #Se o elemento for um "/"
        elif listaexp[t] == '/':
            #Fazemos a divisão dos dois elementos anteriores
            oper2 = pilha2.pop()
            if oper2 != 0:
                pilha2.push(pilha2.pop() / oper2)
            else:
                #Se o denominador for zero, temos um erro
                raise ValueError("Divisão por zero!")
        #Se o elemento não for nenhum dos acima, temos um número
        #Usamos a função de classe is_number
        elif (pilha2.is_number(listaexp[t])):
            #Se for um número, adicionamos à pilha
            pilha2.push(float(listaexp[t]))
        #Se não for um número, deve ser um dos operados unários
        #Se for o "_"
        elif listaexp[t] == "_":
            #Multiplicamos o elemento anterior da pilha por (-1)
            pilha2.push((-1)*pilha2.pop())
        #Se for o "#"
        elif listaexp[t] == "#":
            #Multiplicamos o elemento anterior da pilha por (+1)
            pilha2.push((+1)*pilha2.pop())
    #Retornamos a base da pilha, ou seja, o resultado
    return pilha2.pop()


#Execução do programa/função principal
main()
