# Pesquisa de Satisfação - TudoWeb

NUM_ENTREVISTADOS = 50

quantidade_excelente = 0
quantidade_ruim = 0

print("=" * 50)
print("PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("=" * 50)

for i in range(1, NUM_ENTREVISTADOS + 1):
    print(f"\nEntrevistado {i} de {NUM_ENTREVISTADOS}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção (1, 2 ou 3): "))

    while opiniao not in (1, 2, 3):
        print("Opção inválida! Digite 1, 2 ou 3.")
        opiniao = int(input("Digite sua opção: "))

    if opiniao == 1:
        quantidade_excelente += 1
        classificacao = "EXCELENTE"
    elif opiniao == 2:
        classificacao = "BOM"
    else:
        quantidade_ruim += 1
        classificacao = "RUIM"

    print(f"Resposta registrada para {nome} ({idade} anos): {classificacao}")

print("\n" + "=" * 50)
print("RESULTADO FINAL DA PESQUISA")
print("=" * 50)
print(f"Quantidade de respostas EXCELENTE: {quantidade_excelente}")
print(f"Quantidade de respostas RUIM: {quantidade_ruim}")
print("=" * 50)
