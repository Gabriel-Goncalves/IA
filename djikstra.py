import heapq
from vertice import Vertice


class FilaDePrioridade:

    def __init__(self):
        self.fila = []
        self.index = 0

    def inserir(self, item, prioridade):
        heapq.heappush(self.fila, (-prioridade, self.index, item))
        self.index += 1

    def remover(self):
        return heapq.heappop(self.fila)[-1]


class Grafo:

    def __init__(self, raiz):
        self.raiz = raiz

    def get_raiz(self):
        return self.raiz

    def add(self, origem, destino):
        origem.add_vizinho(destino)
        destino.set_dad(origem)

    def custo(self, no):
        dad = no.get_dad()
        dist = no.get_distancia()
        while dad is not None:
            dist += dad.get_distancia()
            dad = dad.get_dad()
        return dist

    def buscar(self, origem, destino, fila, aux):
        if origem.get_nome() == 'Caldas Novas':
            aux.append(origem)

        else:
            for c in origem.get_vizinhos():
                a = self.custo(c)
                fila.inserir(c, -a)
            u = fila.remover()

            # print(u.get_nome(), u.get_dad().get_nome())
            self.buscar(u, destino, fila, aux)


gyn = Vertice('Gyn', 0)

bv = Vertice('Boa Vista', 45)
edeia = Vertice('Edéia', 124)
hidro = Vertice('Hidrolândia', 33)
silv = Vertice('Silvania', 67)

pont = Vertice('Pontalina', 69)
morr1 = Vertice('Morrinhos', 90)  # Vindo de hidrolandia
pira = Vertice('Piracanjuba', 70)
via = Vertice('Vianopolis', 18)
caldas1 = Vertice('Caldas Novas', 117)  # vindo de BV

morr2 = Vertice('Morrinhos', 124)  # vindo de pontalina
caldas2 = Vertice('Caldas Novas', 57)  # vindo de piracanjuba
caldas3 = Vertice('Caldas Novas', 78)  # Vindo de morrinhos
orizona = Vertice('Orizona', 46)

ipameri = Vertice('Ipameri', 97)

caldas4 = Vertice('Caldas Novas', 61)  # Vindo de ipameri

graf = Grafo(gyn)

# nivel 1
graf.add(gyn, bv)
graf.add(gyn, edeia)
graf.add(gyn, hidro)
graf.add(gyn, silv)

# nivel 2
graf.add(bv, caldas1)
graf.add(edeia, pont)
graf.add(hidro, morr1)
graf.add(hidro, pira)
graf.add(silv, via)

# nivel 3
graf.add(pont, morr2)
graf.add(morr1, caldas2)
graf.add(pira, caldas4)
graf.add(via, orizona)

# nivel 4
graf.add(morr2, caldas3)
graf.add(orizona, ipameri)

# nivel 5
graf.add(ipameri, caldas4)

fila_prioridade = FilaDePrioridade()
auxiliar = []

graf.buscar(gyn, caldas1, fila_prioridade, auxiliar)


dad = auxiliar[0].get_dad()
dist = auxiliar[0].get_distancia()
lista = [auxiliar[0].get_nome()]

while dad is not None:
    dist += dad.get_distancia()
    lista.append(dad.get_nome())
    dad = dad.get_dad()

print()

for c in range(len(lista) - 1, -1, -1):
    if lista[c] == 'Caldas Novas':
        print(lista[c])
    else:
        print(lista[c], end=' -> ')
print(f'custo {dist}')


