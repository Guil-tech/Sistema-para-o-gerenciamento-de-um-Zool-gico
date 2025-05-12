
class informacoes:

    def __init__(self):
        self.nome = input('Informe o nome do animal: ')
        self.data_nascimento = input('Informe a data de nascimento: ')
        self.descricao = input('Informe uma descrição: ')
        self.especie = input('Informe a espécie do animal: ')
        self.habitat = input('Informe seu habitat: ')
        self.pais_origem = input('Informe o pais de origem: ')
    
    def infos(self):
        return self.nome, self.data_nascimento, self.descricao, self.especie, self.habitat, self.pais_origem 