class ElementoSimples:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None


class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def inserir(self, sigla, nomeEstado):
        nodo = ElementoSimples(sigla, nomeEstado)
        if (self.head == None):
            self.head = nodo
        else:
            nodo.proximo = self.head
            self.head = nodo
            return 0

    def imprimir(self, linha, tamanho):
        temp = self.head
        if linha > tamanho:
            print()
        else:
            print(f'{linha}: ', end=' ')
        while temp:
            print(f'{temp.sigla} ->', end='')
            temp = temp.proximo
        print('None')


class TabelaHash:
    def __init__(self):
        self.tam = 10
        self.length = 0
        self.h = [ListaEncadeadaSimples() for i in range(0, self.tam)]

    def HashFunc(self, k):
        k = list(k)
        if k == ['D', 'F']:
            return 7
        else:
            return (ord(k[0]) + ord(k[1])) % self.tam

    def inserir(self, sigla, nomeEstado):
        pos = self.HashFunc(sigla)
        add = self.h[pos].inserir(sigla, nomeEstado)

    def imprimir(self):
        a = -1
        for i in range(self.tam):
            a += 1
            self.h[i].imprimir(a, self.tam)


Teste = TabelaHash()

while True:
    print('1 - Inserir na Tabela Hash')
    print('2 - Imprimir a Tabela Hash')
    print('3 - Sair')

    y = int(input('Escolha uma opção:'))
    if y == 1:
        sigla = input('Digite a sigla de um estado: ')
        nomeEstado = input('Digite o nome do estado: ')
        Teste.inserir(sigla, nomeEstado)
        print()

    elif y == 2:
        print()
        Teste.imprimir()
        print()

    elif y == 3:
        print('Encerrando o programa....')
        break

