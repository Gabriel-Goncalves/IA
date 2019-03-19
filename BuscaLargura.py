from vertice import Vertice


class Grafo:

    def __init__(self, raiz):
        self.raiz = raiz

    def get_raiz(self):
        return self.raiz

    def add(self, origem, destino):
        origem.add_vizinho(destino)
        destino.set_dad(origem)

    def buscar(self, origem, destino, aux):
        print(origem.get_nome(), ", visitado")
        origem.set_visitado(True)
        fila = []
        for c in origem.get_vizinhos():
            print(c.get_nome(), ', visitado')
            fila.append(c)
            c.set_visitado(True)

        while len(fila) > 0:

            v = fila[0]
            for u in v.get_vizinhos():
                if u.get_nome() == destino.get_nome():
                    print(u.get_nome(), ', visitado')
                    aux.append(u)
                    fila = [0]
                    break

                elif u.get_visitado() is False:
                    u.set_visitado(True)
                    fila.append(u)
                    print(u.get_nome(), ', visitado')

            fila.pop(0)



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

auxiliar = []

graf.buscar(gyn, caldas1, auxiliar)

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

