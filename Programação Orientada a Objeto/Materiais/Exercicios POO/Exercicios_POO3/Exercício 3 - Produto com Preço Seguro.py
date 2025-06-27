class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome        # atributo privado
        self.__preco = preco      # atributo privado

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            print(f"Preço do produto {self.__nome} alterado para R${novo_preco:.2f}")
        else:
            print("Digite um valor válido (maior que zero).")

produto1 = Produto("teclado mecanico", 150)
print(produto1.get_preco())

produto1.set_preco(130)
print(produto1.get_preco())

produto1.set_preco(-10)
print(produto1.get_preco())