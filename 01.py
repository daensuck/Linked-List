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

    def InsertAt(self,i,newItem):

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
    def Remove(self,item):
    def RemoveAt(self,i):

    def Find(self,item):
    def Get(self,i):
    def Set(self,i,newItem):

    #teste