class Dataset(object):
    def __init__(self,id, PMU, P, Q, V, modelo, info ,nombre, inicio, fin,createdAt,updatedAt) -> None:
        self.nombre = nombre
        self.info = info
        self.id = id
        self.modelo = modelo
        self.pmu = PMU
        self.P = P
        self.Q = Q
        self.info = info
        self.inicio = inicio
        self.fin = fin 
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        pass

        