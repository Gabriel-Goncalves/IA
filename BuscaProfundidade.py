import random
from vertice import Vertice


class Grafo:

    def __init__(self, raiz):
        self.raiz = raiz

    def get_raiz(self):
        return self.raiz

    def add(self, origem, destino):
        origem.add_vizinho(destino)
        destino.set_dad(origem)

    def buscar(self, origem, destino, pilha):

        destino_achado = False
        pilha.append(origem)
        origem.set_visitado(True)

        if destino.get_nome() == origem.get_nome():
            destino_achado = True

        if destino_achado is False:
            elemento = random.choice(origem.get_vizinhos())
            self.buscar(elemento, destino, pilha)


gyn = Vertice('Gyn', 0)

bv = Vertice('Boa Vista', 45)
edeia = Vertice('Edéia', 124)
hidro = Vertice('Hidrolândia', 33)
silv = Vertice('Silvânia', 67)

pont = Vertice('Pontalina', 69)
morr1 = Vertice('Morrinhos', 90)  # Vindo de hidrolandia
pira = Vertice('Piracanjuba', 70)
via = Vertice('Vianópolis', 18)
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
graf.add(pira, caldas3)
graf.add(via, orizona)

# nivel 4
graf.add(morr2, caldas3)
graf.add(orizona, ipameri)

# nivel 5
graf.add(ipameri, caldas4)

"""
gyn.add_vizinho(bv)
gyn.add_vizinho(edeia)
gyn.add_vizinho(hidro)
gyn.add_vizinho(silv)

bv.add_vizinho(caldas1)

edeia.add_vizinho(pont)

hidro.add_vizinho(morr1)
hidro.add_vizinho(pira)

silv.add_vizinho(via)

pont.add_vizinho(morr2)

pira.add_vizinho(caldas2)

via.add_vizinho(orizona)

morr1.add_vizinho(caldas3)
morr2.add_vizinho(caldas3)

orizona.add_vizinho(ipameri)

ipameri.add_vizinho(caldas4)
"""

pi = []
graf.buscar(gyn, caldas1, pi)

custo = 0

for c in pi:
    if c.get_nome() == 'Caldas Novas':
        print(c.get_nome())
        custo += c.get_distancia()
    else:
        print(c.get_nome(), end=' -> ')
        custo += c.get_distancia()

print(f'Custo: {custo}')

"""
for c in range(0, len(pi) - 1):
    if pi[c] == 'Caldas Novas':
        print(f'{pi[c]} \nCusto:{pi[c + 1]}')
    else:
        print(pi[c], end=' -> ')

"""