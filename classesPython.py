class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade


#Declarando e imprimindo valores
pessoa1 = Pessoa
pessoa1.idade = 19
pessoa2 = Pessoa
pessoa3 = Pessoa("Bruno", 29)
pessoa2.nome = "Bruno"

print(pessoa3.getNome())
print(pessoa2.getNome())