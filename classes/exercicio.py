class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = 0

    def drive(self, km):
        self.quilometragem += km

    def descricao(self):
        return f"{self.marca} {self.modelo} ({self.ano}) : {self.quilometragem} km"

meuCarro = Carro("Toyota", "Corolla", 2020)

meuCarro.drive(120)

print(meuCarro.descricao())
