from CRUD.Adicionar_Ler_json import FuncoesJason
from CRUD.cadastrar_animal import Cadastro
from perguntas_informacoes_animais import informacoes

class Edicao:

    def __init__(self, animal_editar):
        self.__jason = FuncoesJason()
        self.__animais = self.__jason.ler_json()
        self.__animal_editar = animal_editar

        

    def procura_animal(self):
        for i in range(len(self.__animais)):
            if self.__animal_editar == self.__animais[i]['nome']:
                self.__indicie_animal = i
                return True
        return False 
    
    def edita_animal(self):
        verificador = self.procura_animal()
        if verificador:
            del self.__animais[self.__indicie_animal]
            self.__jason.salvar_json(self.__animais)

            print("Animal encontrado, diga os novos dados: ")
            infos = informacoes()
            nome, data_nascimento, descricao, especie, habitat, pais_origem = infos.infos()
            cadastrar = Cadastro(nome, data_nascimento, descricao, especie, habitat, pais_origem)
            cadastrar.cadastrar_animal()
            return None
        print("Animal não existe para editar")



