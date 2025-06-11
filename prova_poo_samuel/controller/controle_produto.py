from model.produto import produto
from model.produto_dao import produto_dao

class controle_produto:
    def __init__ (self):
        self.dao = produto_dao()
    
    def inserir_produtos(self,nome,quantidade,preco):
        prod = produto(nome,quantidade,preco)
        if(preco > 0):
            return self.dao.cadastrar_produto(prod)
    
    def olhar_produtos(self):
        return self.dao.ver_produtos()
    


    def atualizar_preco(self,escolha1,preco_mud, id_1):
        if escolha1 == 1:
            self.dao.trocar_preco(preco_mud,id_1)

    def atualizar_quantidade(self,escolha1,quantidade_mud,id_1):
        if escolha1 == 2:
            self.dao.trocar_quantidade(quantidade_mud),id_1

    def apagar_produto(self,id_2):
        self.dao.excluir_produto(id_2)
    
    def procurar_produtos_nome(self,escolha3,nome_mud):
        if(escolha3 == 1):
            self.dao.consultar_nome(nome_mud)
    
    def procurar_produtos_id(self,escolha3,id_3):
        if(escolha3 == 2):
            self.dao.consultar_id(id_3)
    
    def valor_total(self):
        self.dao.valor_total()

