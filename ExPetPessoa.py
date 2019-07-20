class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

pessoa = Pessoa('Camila', 21, 50, 1.59)

print(f"A {pessoa.nome} tem {pessoa.idade} anos.")

