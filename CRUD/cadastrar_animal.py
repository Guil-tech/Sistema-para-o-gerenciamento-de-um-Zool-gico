from CRUD.Adicionar_Ler_json import FuncoesJason

class Cadastro:


    def __init__(self, nome= str(), data_nascimento= str(), descricao= str(), especie= str(), habitat= str(), pais_origem= str()):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__descricao = descricao
        self.__especie = especie
        self.__habitat = habitat
        self.__pais_origem = pais_origem
    
    def cadastrar_animal(self):
        return self.__processo_cadastrar_animal()
    
    def __processo_cadastrar_animal(self):
        jason = FuncoesJason()
        self.__animal_novo = {
            "nome": self.__nome,
            "data_nascimento": self.__data_nascimento,
            "descricao": self.__descricao,
            "especie": self.__especie,
            "habitat": self.__habitat,
            "pais": self.__pais_origem
        }

        self.animais = jason.ler_json()
        self.animais.append(self.__animal_novo)
        jason.salvar_json(self.animais)
    def imprimir(self):
        return print(f"Nome: {self.__nome} \nData de Nascimento: {self.__data_nascimento} \nDescrição: {self.__descricao}\nEspecie: {self.__especie}\
                     \nhabitat: {self.__habitat} \npais de origem: {self.__pais_origem}\n")
