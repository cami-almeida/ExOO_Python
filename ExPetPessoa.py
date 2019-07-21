class Pessoa:
    def __init__(self, nomeDono, idadeDono):
        self.nomeDono = nomeDono
        self.idadeDono = idadeDono

pessoa = Pessoa('Camila', 21)


class Pet(Pessoa):
    def __init__(self, nomeDono, idadeDono, nomePet):
        super().__init__(nomeDono, idadeDono)
        self.nomePet = nomePet

    def idadePet(self):
        ano_nasc = int(input(f'Digite o ano que o {self.nomePet} nasceu: '))
        idade = 2019 - ano_nasc
        print(f"{self.nomeDono} é dono(a) do {self.nomePet} que possui {idade} anos.")


pet = Pet("Camila", 21, "Bidu") 
pet.idadePet()
print(f"{pessoa.nomeDono} tem {pessoa.idadeDono} anos.")