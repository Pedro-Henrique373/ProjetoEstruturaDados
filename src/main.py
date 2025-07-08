class ElementoSimples:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

    def __str__(self):
        return str(self.numero), str(self.cor)


class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None
        self.tam = 0

        if nodos is not None:
            nodo = ElementoSimples(dado=nodos.pop(0))
            self.head = nodo
            for elem in nodos:
                nodo.proximo = ElementoSimples(dado=elem)
                nodo = nodo.proximo

    def __str__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(nodo.dado)
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)

    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    def __len__(self):
        return self.tam

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.proximo
            else:
                raise IndexError('List index out of range')
        if pointer:
            return pointer.numero
        raise IndexError('List index out of range')

    def inserirSemPrioridade(self, numero, cor):
        nodo = ElementoSimples(numero, cor)
        tamanho1 = self.tam
        if self.head is None:
            self.head = nodo
            nodo.numero = numero
            self.tam = self.tam + 1
            return

        nodo_atual = self.head
        while (nodo_atual.proximo != None):
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo
        self.tam = self.tam + 1

    def inserirComPrioridade(self, numero, cor):
        nodo = ElementoSimples(numero, cor)
        tamanho2 = self.tam
        if self.head is None:
            self.head = nodo
            nodo.numero = numero
            self.tam = self.tam + 1
            return

        nodo_atual = self.head
        while (nodo_atual.proximo != None):
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo
        self.tam = self.tam + 1

    def atenderPaciente(self):
        if self.head == None:
            print('Nenhum paciente esta na fila')
            return
        if self.head:
            primPaciente = self.head
            primPacNumCartão = self.head.numero
            segunPaciente = self.head.proximo
            self.head = segunPaciente
            return primPacNumCartão

    def returnCor(self, corCartão):
        c = self.head.cor
        corCartão = self.head.cor
        return  corCartão

    def imprimir(self):
        temp = self.head
        i = 0
        print('Lista -> ', end='')
        while temp:
            print(f'[{temp.cor},{temp.numero}]', end=' ')
            temp = temp.proximo
        print(end='\n')


ListaPaciente = ListaEncadeadaSimples()

while True:
    print('1 – Adicionar paciente a fila')
    print('2 – Mostrar pacientes na fila')
    print('3 – Chamar paciente')
    print('4 – Sair')

    y = int(input('>>'))
    if y == 1:
        cartCor = input('Informe a cor do cartão (A/V): ')
        cartNum = input('Informe o numero do cartão: ')
        if cartCor == 'V':
            ListaPaciente.inserirSemPrioridade(cartNum, cartCor)
        elif cartCor == 'A':
            ListaPaciente.inserirComPrioridade(cartNum, cartCor)

    elif y == 2:
        ListaPaciente.imprimir()

    elif y == 3:
        a = None
        x = ListaPaciente.returnCor(a)
        a = ListaPaciente.atenderPaciente()
        print(f'Atendendo o paciente com cartão de cor {x} e número {a}')

    elif y == 4:
        print('Encerrando o programa')
        print()
        break

    else:
        print('Digite uma opção válida:')
        continue
