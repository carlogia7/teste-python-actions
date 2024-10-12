# Inicializando a agenda telefônica com 5 contatos
agenda_telefonica = {
  "Joao": "1234-5678",
  "Bob": "2345-6789",
  "Carlos": "3456-7890",
  "Pedro": "4567-8901",
  "Julia": "5678-9012"
}

def exibirAgenda(agenda) :
  print("\nagenda Telefônica:")
  for nome, telefone in agenda.items():
    print(f"{nome}: {telefone}")

def buscarContato(agenda):
  nome = input("Digite o nome do contato que deseja buscar: ")
  if nome in agenda:
    print(f"contato encontrado: {nome} - Telefone: {agenda[nome]}")
  else:
    print(f"Contato {nome} não encontrado.")
    adicionar = input("Deseja adicionar esse contato? (sim/não): ")
    if adicionar == "sim":
      telefone = input(f"Digite o telefone para {nome}: ")
      agenda[nome] = telefone
      print(f"Contato {nome} adicionado com sucesso!")

exibirAgenda(agenda_telefonica)
buscarContato(agenda_telefonica)
