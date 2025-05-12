from CRUD.cadastrar_animal import Cadastro
from CRUD.Adicionar_Ler_json import FuncoesJason
from CRUD.imprimir_animais import imprimir_Animais
from CRUD.editar_animais import Edicao
from perguntas_informacoes_animais import informacoes
from CRUD.excluir_animal import Exclusao
jason = FuncoesJason()


def menu():
    print('////////////Sistema para gerenciamento de animais no Zoológico////////////\n')


def menu_operacoes():
    print("                     ----------OPERAÇÕES--------")
    print("                        1-Adicionar um Animal")
    print('                        2-listar Animais')
    print("                        3-Editar Animal")
    print("                        4-excluir Animal")
    print('                        5-Sair do Programa\n')


def adicionar():
    infos = informacoes()

    nome, data_nascimento, descricao, especie, habitat, pais_origem = infos.infos()
    cadastrar = Cadastro(nome, data_nascimento, descricao,
                         especie, habitat, pais_origem)
    cadastrar.cadastrar_animal()


def listar():
    impressao = imprimir_Animais()
    impressao.imprimir()


def editar(animal_editar):
    editar = Edicao(animal_editar)
    editar.edita_animal()


def excluir(animal_exculir):
    deletar = Exclusao(animal_exculir)
    deletar.excluir()


while True:
    menu()
    menu_operacoes()
    while True:
        try:
            resposta = int(input('Qual operação deseja realizar?: '))
            break
        except ValueError:
            print("informe uma opção correta")
        continue

    match resposta:
        case 1:
            adicionar()
        case 2:
            listar()
        case 3:
            animal_desejado = input("Qual o nome do animal que deseja editar?")
            editar(animal_desejado)
        case 4:
            animal_desejado = input(
                "Qual o nome do animal que deseja deletar?")
            excluir(animal_desejado)
        case 5:
            print("Adeus!")
            break
        case _:
            print('Digite uma das opções')
