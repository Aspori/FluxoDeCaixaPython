import os

os.system('cls')

# Fazendo um fluxo de caixa

fluxo_de_caixa = []

print("______________")
print("@ Fluxo de caixa")
print("______________")
print("1- Adicionar receita")
print("2- Adicionar despesa")
print("______________")
print("\n# Digite outro número para encerrar #\n")

def adicionar_receita():
    nome = input("Nome: ")
    valor = float(input("Valor: R$") )
    fluxo_de_caixa.append({
        "nome": nome,
        "valor": valor
    })
def adicionar_despesa():
    nome = input("Nome: ")
    valor = float(input("Valor: R$") )
    valor = valor * -1
    fluxo_de_caixa.append({
        "nome": nome,
        "valor": valor
    })

while True:
    
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        adicionar_receita()
    elif opcao == 2:
        adicionar_despesa()

        
        
    else:
        break

print("\n")
# Nota fiscal
total = 0
for fc in fluxo_de_caixa:
    print("Nome:", fc["nome"], "Valor: R$", fc["valor"], 1)
    total = total + fc["valor"]



print("\nValor em conta é: R$", total, "\n")


