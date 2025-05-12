from CRUD.Adicionar_Ler_json import FuncoesJason

class Exclusao:

    def __init__(self, animal_exluir):
        self.__animal_excluir = animal_exluir
    
    def excluir(self):
        jason = FuncoesJason()
        self.__animais = jason.ler_json()

        
        if  self.procura_animal(): 
            del self.__animais[self.__indicie_animal]
            jason.salvar_json(self.__animais)
        return None
        

    def procura_animal(self):
        for i in range(len(self.__animais)):
            if self.__animal_excluir == self.__animais[i]['nome']:
                self.__indicie_animal = i
                return True
        print('Animal Não existe')
        return False