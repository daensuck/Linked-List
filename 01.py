class Node:
    def __init__(self,newItem,nextNode):
        self.item = newItem
        self.next = nextNode

class MyLinkedList:
    def __init__(self):
        self.inicio = None #inicio da lista
        self.final = None #final da lista
        self.count = 0 #numero de elementos

    def AddFirst(self,newItem):
        # cria o novo no para conter o item
        newNode = Node(newItem,None)

        #faz o novo no apontar para o inicio
        newNode.next = self.inicio

        # dps da inserção, inicio devera
        # apontar para o novo no criado
        self.inicio = newNode

        #caso seja o primeiro no sendo inserido, final tbm deve apontar para o no
        if (self.final == None):
            self.final = newNode

        self.count += 1

    def AddLast(self,newItem):
        #cria um no novo para armazenar o item. Como o
        # no sera inserido no final, seu campo next
        # é inicializado com None
        newNode = Node(newItem,None)

        #faz o encadeamento com o ultimo no, caso ele
        # exista. caso contrario, inicio deve ser
        #atualizado, pois é o caso da primeira inserção
        if(self.final == None):
            self.inicio = newNode
        else:
            self.final.next = newNode

        self.final = newNode
        self.count += 1

    def InsertAt(self,p,newItem):
        # nao permite a inserção alem do limite
        if (p < 0 or p > self.count):
            raise Exception('Posição inválida.')
        
        newNode = Node(newItem,None) #cria novo no

        if (p == 0):
            #inserção no inicio
            newNode.next = self.inicio
            self.inicio = newNode
        else:
            # inserção no meio ou no final. avança o ponteiro aux ate atingir o no da po p-1
            aux = self.inicio
            for i in range(0,p-1):
                aux = aux.next
            
            newNode.next = aux.next
            aux.next = newNode
        
        if (p == self.count):
            self.final = newNode

        self.count += 1
        
        
    def RemoveFirst(self):
        if(IsEmpty()):
            raise Exception('Lista vazia')

        # na remoção do primeiro no deve-se
        # fazer inicio apontar para o segundo no
        # caso exista (ou None)
        self.inicio = self.inicio.next

        #caso seja o unico no da lista
        # eh preciso atualizar tbm final
        if(self.inicio == None):
            self.final = None

        self.count += 1


    def RemoveLast(self):
        if IsEmpty():
            raise Exception('Lista Vazia')
        
        if self.count == 1:
            #remove o unico no da lista
            self.inicio =  None
            self.final = None
        
        else: 
            #percorre os nos ate atingir o penultimo no
            aux = self.inicio
            for i in range (0,self.count-2):
                aux = aux.next
        
            #faz o next do ultimo no apontar para none, removendo
            aux.next = None
            self.final = aux
        
        self.count -=1

    def Remove(self,item):
        if IsEmpty():
            raise Exception ('A lista esta vazia')
        
        #busca pelo primeiro no que contem o item
        aux = self.inicio
        anterior = None

        while (aux != None and aux.item != item):
            anterior = aux
            aux = aux.next

        #aux sera None qnd o item nao eh encontrado
        if (aux == None):
            return False
        
        if (aux == self.inicio):
            self.inicio = aux.next #no removido eh o primeiro
        else:
            anterior.next = aux.next # no interm ou ultimo

        # se eh no final, final deve ser atualizado
        if (aux == self.final):
            self.final = anterior

        self.count -= 1
        return True 

    def RemoveAt(self,i):

    def AddSorted(self,newItem):    
        #encontra a posição de inserção percorrendo
        #os nos enquanto os itens sao menores
        aux = self.inicio
        anterior = None
        
        while (aux != None and aux.item < newItem):
            anterior = aux 
            aux = aux.next

        newNode = Node(newItem,aux)
        newNode.next = aux.next

        if (aux == self.inicio):
            self.inicio = newNode
        else:
            anterior.next = newNode
        if (aux == self.final):
            self.final = newNode
        self.count += 1
        


    def Find(self,item):
    def Get(self,i):
    def Set(self,i,newItem):

    