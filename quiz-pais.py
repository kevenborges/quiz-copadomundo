import random
lista = ["alemanha", "arábia saudita", "argentina", "austrália", "bélgica", 
"brasil", "camarões", "canadá", "catar", "coreia do sul", "costa rica", "croácia", 
"dinamarca", "equador", "espanha", "estados unidos", "frança", "gana", "holanda", 
"inglaterra", "irã", "japão", "marrocos", "méxico", "país de gales", "polônia", "portugal", 
"senegal", "sérvia", "suíça", "tunísia", "uruguai"]

america = ["argentina", "brasil", "canadá", "costa rica", "equador", "estados unidos", "méxico", "uruguai"]
europa = ["alemanha", "bélgica", "croácia", "dinamarca", "espanha", "frança", "holanda", "inglaterra", "país de gales", "polônia", "portugal", "sérvia", "suíça"]
asia = ["arábia saudita", "catar", "coreia do sul", "japão", "irã"]
oceania = ["austrália"]
africa = ["camarões", "gana", "marrocos", "senegal", "tunísia"]

azul = ["argentina", "austrália", "costa rica", "holanda", "sérvia", "senegal", "uruguai"]
vermelho = ["alemanha", "bélgica", "canadá", "croácia", "dinamarca", "estados unidos", "frança", "marrocos", "país de gales", "portugal", "suíça", "tunísia"]
verde = ["arábia saudita", "brasil", "camarões", "gana", "irã", "méxico"]
branco = ["catar", "coréia do sul", "inglaterra", "japão", "polônia"]
amarelo = ["equador", "espanha"]

pais = random.choice(lista)
tentativas = 4
resposta = input("Tente adivinhar um dos 32 países da Copa do Mundo de 2022: ").lower()
while (resposta != pais and tentativas > 0):
    print("\nVocê errou!\n")
    print(f"Você ainda tem {tentativas} tentativas.\n")
    if tentativas == 3:
        if pais in azul:
            print("Dica: Uma das cores da bandeira é azul.\n")
        if pais in vermelho:
            print("Dica: Uma das cores da bandeira é vermelha.\n")
        if pais in verde:
            print("Dica: Uma das cores da bandeira é verde.\n")
        if pais in branco:
            print("Dica: Uma das cores da bandeira é branco.\n")
        if pais in amarelo:
            print("Dica: Uma das cores da bandeira é vermelho.\n")
    if tentativas == 2:
        if pais in america:
            print("Dica: É um país da América.\n")
        if pais in europa:
            print("Dica: É um país da Europa.\n")
        if pais in asia:
            print("Dica: É um país da Ásia.\n")
        if pais in africa:
            print("Dica: É um país da África.\n")
        if pais in oceania:
            print("Dica: É um páis da Oceania.\n")
        tentativas = tentativas - 1
        resposta = input("Digite novamente o nome de um país: ").lower()
    else:
        if tentativas == 1:
            print(f"Dica: A primeira letra do país é {pais[0].upper()}.")
        tentativas = (tentativas - 1)
        resposta = input("Digite novamente o nome de um país: ").lower()
if resposta == pais:
        print("\nVocê acertou!!! Parabéns, tu é pica\n")
else:
        print(f"\nVocê errou todas as tentativas, o país era: {pais}")

        # code by Keven Borges Barros, discente em Bacharelado em Sistemas de Informação - FURG
