import json


class FuncoesJason:

    __arquivo_animal = "animais.json"

    def ler_json(self):
        with open(self.__arquivo_animal, "r", encoding="utf-8") as f:
            return json.load(f)
        f.close()
        

    def salvar_json(self, dados):
        with open(self.__arquivo_animal, 'w') as f:
            json.dump(dados, f)
        f.close()
