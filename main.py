from plataforma import Plataforma

nova_plataforma = Plataforma()

while True:
 print("\n==== MENU ====")
 print("1 - Cadastrar assinante")
 print("2 - Listar assinantes")
 print("3 - Cancelar assinatura")
 print("4 - Sair")

 opcao = input("Escolha uma opção: ")

 if opcao == "1":
    nova_plataforma.cadastrar_assinante()

 elif opcao == "2":
    nova_plataforma.listar_assinantes()

 elif opcao == "3":
    id_conta = int(input("Digite o ID da conta: "))

    if nova_plataforma.cancelar_assinatura(id_conta):
        print("Assinatura cancelada!")
    else:
        print("Assinante não encontrado!")

 elif opcao == "4":
    print("Sistema encerrado!")
    break

 else:
    print("Opção inválida!")

