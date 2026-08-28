from assinante import Assinante

class Plataforma:
    def __init__(self):
        self.assinantes = []

    def cadastrar_assinante(self):
        print("==== CADASTRO DE ASSINANTE ====")
        print("escolha um dos planos disponiveis: ")
        print("1 = Basico\n")
        print("2 = Padrão\n")
        print("3 = Premium")

        opcao = input("informe sua escolha: ")
        if opcao == "1":
            plano = "basico"
            print("Plano basico escolhido!")
        elif opcao == "2":
            plano = "padrão"

            print("Plano padrão escolhido!")
        elif opcao == "3":
            plano = "premium"

            print("Plano premium escolhido!")
        else:
            print("opção invalida!")
            return
        print("=============")

        nome = input("informe seu nome: ")
        senha = input("informe sua senha: ")

        novo_assinante = Assinante(nome, plano, senha)

        self.assinantes.append(novo_assinante)   

    def listar_assinantes(self): 
        print("==== LISTANDO ASSINANTES ====")
        for assinante in self.assinantes:
            print(assinante.exibir_dados())

    def buscar_por_id(self, id_conta):
        for assinante in self.assinantes:
            if assinante.id_conta == id_conta:
                return assinante
        else:
         return None

    def cancelar_assinatura(self, id_conta):
         resultado_busca = self.buscar_por_id(id_conta)

         if resultado_busca != None:
             self.assinantes.remove(resultado_busca)
             return True
         return False

    


        












