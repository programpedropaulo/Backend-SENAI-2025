class ContaBancaria:
  def __init__(self, titular, saldo):
    self.titular = titular
    self.__saldo = saldo

  # getter para acessar saldo
  def get_saldo(self):  # <<< aqui tá corrigido
    return self.__saldo

  # método de depósito com validação
  def deposito(self, valor):
    if valor > 0:
      self.__saldo += valor
    else:
      print("O valor precisa ser positivo.")

  # método de saque com validação
  def saque(self, valor):
    if 0 < valor <= self.__saldo:
      self.__saldo -= valor
    else:
      print("Saldo insuficiente ou valor inválido.")

# EXEMPLO DE USO:
conta = ContaBancaria("Lino", 1000)

print(conta.get_saldo())  # 1000

conta.deposito(500)
print(conta.get_saldo())  # 1500

conta.saque(200)
print(conta.get_saldo())  # 1300

conta.saque(2000)         # Saldo insuficiente ou valor inválido.
