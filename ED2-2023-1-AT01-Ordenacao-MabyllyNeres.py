########################################################################################################
# Estrutura de dados 2 - Trabalho 01
# Estudantes: Mariana Pedroso Naves (2320720) e Mabylly Kauany Neres da Silva(2368013)
# Data: 12/04/2023
########################################################################################################

import random
import timeit
import sys
import os

##Implementando Insertion Sort
def insertionSort(vetor): 
    comparacaoInsertion = 0
    n = len(vetor)                                            
    for i in range(1, n):                                     
        auxiliar = vetor[i]
        j = i - 1
        while (j >= 0) and auxiliar < vetor[j]: 
          vetor[j+1] = vetor[j]
          j = j-1
          comparacaoInsertion +=1
        vetor[j+1] = auxiliar
    return comparacaoInsertion

##Implementando Selection Sort
def SelectionSort(vetor):
    n = len(vetor)
    comparacaoSelection = 0
    for i in range(n):
          menor = i
          for j in range(i+1, n):
            comparacaoSelection += 1
            if(vetor[j] < vetor[menor]):
              menor = j
          vetor[menor],vetor[i] = vetor[i], vetor[menor]
    return comparacaoSelection

## Implementando Bubble Sort
def bubbleSort(vetor):
    compareBubble = 0
    n = len(vetor)
    change = True
    while change == True:
        change = False
        for i in range(n - 1):
            compareBubble += 1
            if vetor[i] > vetor[i + 1]:
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                change = True    
        n -= 1                 
    return compareBubble

##Implementando Merge Sort
def mergeSort(vetor):
    comparacoesMerge = 0
    if len(vetor) > 1:
        meio = len(vetor)//2
        esquerda = vetor[:meio]
        direita = vetor[meio:]

        comparacoesMerge += mergeSort(esquerda)
        comparacoesMerge += mergeSort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            comparacoesMerge += 1
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1

    return comparacoesMerge


##Implementando Quick Sort
def quick_sort(vetor, comparacoesQuick):
    if len(vetor) > 1:
        pivot = vetor[0]
        esquerda = []
        direita = []
        for i in range(1, len(vetor)):
            comparacoesQuick += 1
            if vetor[i] < pivot:
                esquerda.append(vetor[i])
            else:
                direita.append(vetor[i])
        quick_sort(esquerda, comparacoesQuick)
        quick_sort(direita, comparacoesQuick)
        vetor[:] = esquerda + [pivot] + direita
    return comparacoesQuick


##Implementando max Heap Sort
def maxHeapify(vetor,n,i, comparacaoHeap):
    l = 2 * i + 1
    r = 2 * i + 2
    maior = i

    if l < n and vetor[l] > vetor[i]:
        maior = l
    if r < n and vetor[r] > vetor[maior]:
        maior = r
    comparacaoHeap += 1
    if maior != i:
        (vetor[i],vetor[maior]) = (vetor[maior],vetor[i])
        maxHeapify(vetor,n,maior, comparacaoHeap)
    return comparacaoHeap

##Implementando Heap Sort
def heapsort(vetor, comparacaoHeap):
    n = len(vetor)
    for i in range(n, -1, -1):
        comparacaoHeap = maxHeapify(vetor, n, i, comparacaoHeap)
    for i in range(n-1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]  # troca
        comparacaoHeap = maxHeapify(vetor, i, 0, comparacaoHeap)
    return comparacaoHeap
         
## Função main
def main():
    #Tratamento de erro dos parametros
    if len(sys.argv)!=3:
        print("Quantidade de parametros invalida!")
        exit(1)
    
    entrada = open(sys.argv[1],'r') #Arquivo de entrada
    saida = open(sys.argv[2],'w') #Arquivo de saída
       
    #Tratamento de erro para arquivo vazio
    if os.path.getsize(sys.argv[1]) == 0 and '\n':
        saida.write("Arquivo vazio!")
        entrada.close()
        saida.close()
        exit(1)
        
    else:
        # Lê a segunda linha da entrada e remove qualquer espaço em branco que possa existir no final da linha: strip() 
        linha = entrada.readline().strip()
        
        #Tratamento de erro para caso a primeira linha seja um caracter
        if not linha.isnumeric():
            saida.write("Arquivo invalido!")
            entrada.close()
            saida.close()
            exit(1)
    
        # Converte a linha lida para um número inteiro: int()
        N = int(linha)
        
        # Lê a segunda linha da entrada e remove qualquer espaço em branco que possa existir no final da linha: strip() 
        linha = entrada.readline().strip()
        
        #Tratamento de erro para caso o método seja inválido
        if N <= 0 or linha not in ['c', 'd', 'r']:
            saida.write("Arquivo invalido!")
            entrada.close()
            saida.close()
            exit(1)
            
        # Cria o vetor vazio
        vetor = []

        # Preenche o vetor de acordo com o método escolhido
        if linha == 'c': #Crescente
            vetor = list(range(1, N+1))
        elif linha == 'd': #Decrescente
            vetor = list(range(N, 0, -1))
        elif linha == 'r': #Randômico
            for numero in range(N):
                vetor.append(random.randint(0, 32000))        
                
        # Escreve o vetor gerado em um arquivo de saída
        with open(sys.argv[2], "w") as saida: 
            
            #Computação do Insertion Sort
            inicio = timeit.default_timer() * 1000
            vetorInsertion = vetor.copy() # criar uma cópia do vetor original
            compInsertion = insertionSort(vetorInsertion)
            fim = timeit.default_timer() * 1000
            saida.write("insertionSort: " + str(vetor) + ", ")
            saida.write(str(compInsertion) + " comp, ")
            saida.write(f"{fim - inicio:.8f} ms")
        
            
            #Computação do Selection Sort
            inicio = timeit.default_timer() * 1000
            vetorSeletion = vetor.copy() # criar uma cópia do vetor original
            compSelection = SelectionSort(vetorSeletion)
            fim = timeit.default_timer() * 1000
            saida.write("\nselectionSort: " + str(vetor) + ", ")
            saida.write(str(compSelection) + " comp, ")
            saida.write(f"{fim - inicio:.8f} ms")
            
            
            #Computação do Bubble Sort
            inicio = timeit.default_timer() * 1000
            vetorBubble = vetor.copy() # criar uma cópia do vetor original
            compBubble = bubbleSort(vetorBubble)
            fim = timeit.default_timer() * 1000
            saida.write("\nbubbleSort: " + str(vetor) + ", ")
            saida.write(str(compBubble) + " comp, ")
            saida.write(f"{fim - inicio:.8f} ms")
            
            #Computação do Merge Sort
            inicio = timeit.default_timer() * 1000
            vetorMerge = vetor.copy() # criar uma cópia do vetor original
            compMerge = mergeSort(vetorMerge)
            fim = timeit.default_timer() * 1000
            saida.write("\nmergeSort: " + str(vetor) + ", ")
            saida.write(str(compMerge) + " comp, ")
            saida.write(f"{fim - inicio:.8f} ms")
            
            #Computação do Quick Sort
            comparacoesQuick = 0
            inicio = timeit.default_timer() * 1000
            vetorQuick = vetor.copy() # criar uma cópia do vetor original
            compQuick = quick_sort(vetorQuick, comparacoesQuick)
            fim = timeit.default_timer() * 1000
            saida.write("\nquickSort: " + str(vetor) + ", ")
            saida.write(str(compQuick) + " comp, ")
            saida.write(f"{fim - inicio:.8f} ms")
            
            #Computação do Heap Sort
            comparacaoHeap=0
            inicio = timeit.default_timer() * 1000
            vetorHeap = vetor.copy() # criar uma cópia do vetor original
            compHeap = heapsort(vetorHeap, comparacaoHeap)
            fim = timeit.default_timer() * 1000
            saida.write("\nheapSort: " + str(vetor) + ", ")
            saida.write(str(compHeap) + " comp, ")
            saida.write(f"{fim - inicio:.8f} ms")
            
            #Fechamento dos arquivos
            entrada.close()
            saida.close()
            
main() #chamada da função
