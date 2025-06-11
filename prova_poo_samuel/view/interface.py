from controller.controle_produto import controle_produto

class interface:
    def __init__(self):
        self.controle = controle_produto()

    def menu(self):
        valor = True
        while(valor == True):
            print("1 - para cadastrar produto ")
            print("2 - visualizar a lista de produto ")
            print("3 - atualizar quantidade ou preco ")
            print("4 - excluir um produto ")
            print("5 - consultar um produto por nome ou id ")
            print("6 - exibir o valor total do estoque ")
            print("7 - sair do programa")
            escolha = int(input("digite uma das opcoes: "))
            if(escolha == 1):
                nome  = input("digite o nome do produto: ")
                quantidade = int(input("digite a quantidade do produto: "))
                preco = float(input("digite o preco do produto:"))
                self.controle.inserir_produtos(nome, quantidade, preco)

            if(escolha == 2):
                print(self.controle.olhar_produtos())
                

            elif(escolha == 3):
                id_1 = input("digite o id do produto a ser modificado: ")
                print("digite 1 para mudar o preco")
                print("digite 2 para mudar a quantidade")
                escolha1 = int(input("digite uma das opcoes: "))
                if(escolha1 == 1):
                    preco_mud = float(input("digite o preco novo do produto: "))
                elif(escolha1 == 2):
                    quantidade_mud = int(input("digite a quantidade nova do produto: "))
                else:
                    print("valor invalido")
                self.controle.atualizar_preco(preco_mud)
                self.controle.atualizar_quantidade(quantidade_mud)
            
            elif(escolha == 4):
                id_2 = int(input("digite o id do produto a ser deletado: "))
                self.controle.apagar_produto(id_2)

            elif(escolha == 5):
                print("digite 1 para consultar o produto por nome ")
                print("digite 2 para consultar o produto por id")
                escolha3 = int(input("digite uma das opcoes: "))
                if(escolha3 == 1):
                    nome_mud = input("digite o nome do produto a ser procurado: ")
                elif(escolha3 == 2):
                    id_3 = int(input("digite o id do produto a ser procurado:"))
                else:
                    print("valor invalido")
                
                self.controle.procurar_produtos_nome(escolha3,nome_mud)
                self.controle.procurar_produtos_id(escolha3,id_3)

            elif(escolha == 6):
                self.controle.valor_total()
            
            elif(escolha == 7):
                print("processo finalizado....")
                valor = False

            else:
                print("valor invalido")