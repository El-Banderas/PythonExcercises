class Carro:
    def __init__(self, velocidade, cor):
        self.velocidade = velocidade
        self.cor = cor
    
    def setVelocidade(self, velocidade):
        self.velocidade = velocidade

class Camiao(Carro):
    def __init__(self, velocidade, cor, peso_maximo):
        Carro.__init__(self, velocidade, cor)
        self.peso_maximo = peso_maximo
        self.peso_atual = 0
    
    def acrescenta_peso(self, novo_peso):
        self.peso_atual+=novo_peso
    
    def tira_peso(self, novo_peso):
        self.peso_atual-=novo_peso
    
    def get_peso(self):
        return self.peso_atual
