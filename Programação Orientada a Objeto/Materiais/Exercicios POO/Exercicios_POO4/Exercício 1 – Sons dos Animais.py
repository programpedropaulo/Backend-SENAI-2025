class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "som genérico de animal"

class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

class Vaca(Animal):
    def emitir_som(self):
        return "Muuu"

# Instâncias
cachorro = Cachorro("Rex")
gato = Gato("Mingau")
vaca = Vaca("Mimosa")

# Sem usar for, cada chamada é direta:
print(cachorro.nome, "faz", cachorro.emitir_som())
print(gato.nome, "faz", gato.emitir_som())
print(vaca.nome, "faz", vaca.emitir_som())
