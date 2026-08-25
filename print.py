class Carro:

    def __init__(self,nome,marca,preco,aceleracao):
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.aceleracao = aceleracao

    def acelerar(self,aceleracao):
        velocidade = 0
        while velocidade <= 100:
            print(velocidade)
            velocidade += aceleracao

            


Gol = Carro("gol","volkswagen",20000,20)

Gol.acelerar(Gol.aceleracao)

