class Vertice:

    def __init__(self, nome, distancia):
        self.nome = nome
        self.distancia = distancia
        self.dad = None
        self.vizinhos = []
        self.visitado = False

    def add_vizinho(self, vizinho):
        self.vizinhos.append(vizinho)

    def set_dad(self, dad):
        self.dad = dad

    def get_dad(self):
        return self.dad

    def get_visitado(self):
        return self.visitado

    def set_visitado(self, boo):
        self.visitado = boo

    def get_vizinhos(self):
        return self.vizinhos

    def get_distancia(self):
        return self.distancia

    def get_nome(self):
        return self.nome
