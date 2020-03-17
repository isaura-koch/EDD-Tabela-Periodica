import csv
import os

class TabelaPeriodica:
    def __init__(self):
        estados_materia = {
            'l': 'Líquido',
            's': 'Sólido',
            'g': 'Gasoso',
            'd': 'Desconhecido'
        }

        arquivo = csv.reader(open('tabela.txt'), delimiter=';')
        tabela_periodica = {}
        for i, dado in enumerate(arquivo):
            if i == 0:
                continue

            dados = {}
            dados['simbolo'] = dado[0]
            dados['nome'] = dado[1]
            dados['atomico'] = dado[2]
            dados['linha'] = dado[3]
            dados['coluna'] = dado[4]
            dados['estado'] = estados_materia[dado[5]]

            tabela_periodica[dados['simbolo']] = dados
        self.tabela_periodica = tabela_periodica or {}

    def lista_nomes(self):
        for _, elemento in self.tabela_periodica.items():
            print(elemento['nome'])

    def lista_dados_elemento(self, elemento):
        item = self.tabela_periodica[elemento]
        print("Símbolo: ", item['simbolo'])
        print("Nome: ", item['nome'])
        print("Número Atômico: ", item['atomico'])
        print("Linha Tabela: ", item['linha'])
        print("Coluna Tabela: ", item['coluna'])
        print("Estado da Matéria: ", item['estado'])

    def lista_tudo(self):
        print(self.tabela_periodica)


tabela = TabelaPeriodica()
try: 
    while True:
        
        print("***Bem-vindo(a) a tabela periódica EDD!***")
        opcao = int(input("Escolha uma opção: \n1 - Listar o nome de todas as propriedades. \n2 - Listar todos os dados de um elemento. \n3 - Listar tudo cadastrado. \n"))
        alternativas = "Deseja continuar? \n1 - Sim \n2 - Não\n"
        clear = os.system('cls' if os.name == 'nt' else 'clear')

        if opcao == 1:
            tabela.lista_nomes()
            escolha = int(input(alternativas))
            if escolha == 1:
                continue
            elif escolha == 2:
                break
            clear
        elif opcao == 2:
            elemento = input("Insira o elemento que deseja consultar. \nElementos Disponíveis: \nHg, O, Au, Mt \n")
            tabela.lista_dados_elemento(elemento)
            escolha = int(input(alternativas))
            if escolha == 1:
                continue
            elif escolha == 2:
                break
            clear
        elif opcao == 3:
            tabela.lista_tudo()
            escolha = int(input(alternativas))
            if escolha == 1:
                continue
            elif escolha == 2:
                break
            clear
except:
    print("Entrada inválida, tente novamente \n ---------------------")