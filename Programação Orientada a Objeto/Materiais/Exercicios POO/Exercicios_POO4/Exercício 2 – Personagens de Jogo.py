"""Exercício 2 – Personagens de Jogo
Crie uma classe Personagem com o método atacar().
 Crie três subclasses: Guerreiro, Arqueiro e Mago, cada uma com uma implementação diferente de atacar().
Use uma função chamada executar_ataque(personagem) que recebe qualquer objeto e executa o método atacar(). Teste com todos os tipos.
"""

class Personagem: 
  def __init__(self, guerreiro, arqueiro, mago):
    self.guerreiro = guerreiro
    self.arqueiro = arqueiro
    self.mago = mago
  
  def atacar(self):
    return "tipos de ataque"
  
class