from agenda import Agenda
from contato import Contato


from agenda import Agenda
from contato import Contato

def main():
    agenda = Agenda()

    while True:
        print("\n1. Adicionar contato")
        print("2. Remover contato")
        print("3. Listar contatos")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            contato = Contato(nome, telefone, email)
            agenda.adicionar_contato(contato)
        elif escolha == '2':
            nome = input("Nome do contato a ser removido: ")
            agenda.remover_contato(nome)
        elif escolha == '3':
            agenda.listar_contatos()
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()