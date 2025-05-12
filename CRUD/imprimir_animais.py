from CRUD.Adicionar_Ler_json import FuncoesJason


class imprimir_Animais:
    
    def imprimir(self):
        jason = FuncoesJason()
        animais = jason.ler_json()
        
        for i in range(len(animais)):
            self.__nome = animais[i]['nome']
            self.__data_nascimento = animais[i]['data_nascimento']
            self.__descricao = animais[i]['descricao']
            self.__especie = animais[i]['especie']
            self.__habitat = animais[i]['habitat']
            self.__pais_origem = animais[i]['pais']
            print(f"\n \
                        Nome: {self.__nome}\n \
                        Data de Nascimento: {self.__data_nascimento}\n \
                        Descrição: {self.__descricao}\n \
                        Especie: {self.__especie}\n \
                        habitat: {self.__habitat}\n \
                        pais de origem: {self.__pais_origem}\n \
                    ")
        