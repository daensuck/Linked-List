class Node:
    def __init__(self, newItem, nextNode):
        self.item = newItem
        self.next = nextNode

class MyLinkedList:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.count = 0

    def AddFirst(self, newItem):
        newNode = Node(newItem, None)
        newNode.next = self.inicio
        self.inicio = newNode
        if self.final == None:
            self.final = newNode
        self.count += 1

    def AddLast(self, newItem):
        newNode = Node(newItem, None)
        if self.final == None:
            self.inicio = newNode
        else:
            self.final.next = newNode
        self.final = newNode
        self.count += 1

    def InsertAt(self, p, newItem):
        if p < 0 or p > self.count:
            raise Exception('Posição inválida.')
        newNode = Node(newItem, None)
        if p == 0:
            newNode.next = self.inicio
            self.inicio = newNode
        else:
            aux = self.inicio
            for i in range(0, p - 1):
                aux = aux.next
            newNode.next = aux.next
            aux.next = newNode
        if p == self.count:
            self.final = newNode
        self.count += 1

    def RemoveFirst(self):
        if self.IsEmpty():
            raise Exception('Lista vazia')
        self.inicio = self.inicio.next
        if self.inicio == None:
            self.final = None
        self.count -= 1

    def RemoveLast(self):
        if self.IsEmpty():
            raise Exception('Lista Vazia')
        if self.count == 1:
            self.inicio = None
            self.final = None
        else:
            aux = self.inicio
            for i in range(0, self.count - 2):
                aux = aux.next
            aux.next = None
            self.final = aux
        self.count -= 1

    def Remove(self, item):
        if self.IsEmpty():
            raise Exception('A lista esta vazia')
        aux = self.inicio
        anterior = None
        while aux != None and aux.item != item:
            anterior = aux
            aux = aux.next
        if aux == None:
            return False
        if aux == self.inicio:
            self.inicio = aux.next
        else:
            anterior.next = aux.next
        if aux == self.final:
            self.final = anterior
        self.count -= 1
        return True

    def RemoveAt(self, i):
        if i < 0 or i >= self.count:
            raise Exception('Posição inválida')
        if i == 0:
            self.RemoveFirst()
        else:
            aux = self.inicio
            for j in range(0, i - 1):
                aux = aux.next
            noRemovido = aux.next
            aux.next = noRemovido.next
            if noRemovido == self.final:
                self.final = aux
            self.count -= 1

    def AddSorted(self, newItem):
        aux = self.inicio
        anterior = None
        while aux != None and aux.item < newItem:
            anterior = aux
            aux = aux.next
        newNode = Node(newItem, aux)
        if anterior == None:
            self.inicio = newNode
        else:
            anterior.next = newNode
        if aux == None:
            self.final = newNode
        self.count += 1

    def Find(self, item):
        aux = self.inicio
        pos = 0
        while aux != None:
            if aux.item == item:
                return pos
            aux = aux.next
            pos += 1
        return -1

    def Get(self, i):
        if i < 0 or i >= self.count:
            raise Exception('Posição inválida')
        aux = self.inicio
        for j in range(0, i):
            aux = aux.next
        return aux.item

    def Set(self, i, newItem):
        if i < 0 or i >= self.count:
            raise Exception('Posição inválida')
        aux = self.inicio
        for j in range(0, i):
            aux = aux.next
        aux.item = newItem

    def Display(self):
        aux = self.inicio
        while aux != None:
            print(aux.item, end=" ")
            aux = aux.next

    def IsEmpty(self):
        return self.count == 0


def main():
    x = MyLinkedList()
    opcao = 0

    while opcao != 9:
        print("------ Menu de Opcoes -----")
        print()
        print("[1] - Adicionar elemento no inicio")
        print("[2] - Adicionar elemento no final")
        print("[3] - Adicionar elemento ordenadamente")
        print()
        print("[4] - Remover elemento do inicio")
        print("[5] - Remover elemento do final")
        print("[6] - Remover elemento de uma dada posicao")
        print()
        print("[7] - Consultar se um dado elemento está na lista")
        print("[8] - Mostrar a lista")
        print("[9] - Encerrar")
        print()

        opcao = int(input("Informe a opção desejada: "))

        if opcao == 1:
            item = int(input("Informe o valor a ser inserido no inicio: "))
            x.AddFirst(item)

        elif opcao == 2:
            item = int(input("Informe o valor a ser inserido no final: "))
            x.AddLast(item)

        elif opcao == 3:
            item = int(input("Informe o valor a ser inserido ordenadamente: "))
            x.AddSorted(item)

        elif opcao == 4:
            x.RemoveFirst()
            print("Primeiro elemento removido com sucesso!")
            
        elif opcao == 5:
            x.RemoveLast()
            print("Ultimo elemento removido com sucesso!")
          
        elif opcao == 6:
            pos = int(input("Informe a posicao a ser removida: "))
            x.RemoveAt(pos)
            print("Elemento removido com sucesso!")
            

        elif opcao == 7:
            item = int(input("Informe o valor a ser consultado: "))
            pos = x.Find(item)
            if pos == -1:
                print(f"Elemento {item} não foi encontrado na lista.")
            else:
                print(f"Elemento {item} encontrado na posicao {pos} da lista.")

        elif opcao == 8:
            if x.IsEmpty():
                print("Lista vazia!")
            else:
                x.Display()
                print()

        else:
            print("Opcao invalida!")

main()