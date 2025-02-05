
## Desafio Classificador de nível de Herói##


nome = input("Digite o nome do Herói: ")
xp = float(input("Quanto de XP o seu Herói possuí?: "))

nivel = ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Ascendente", "Imortal", "Radiante"]

if xp < 1000:
    print(f"O Herói de nome {nome} está no nível de {nivel[0]}")

elif xp > 1001 and xp < 2000:
    print(f"O Herói de nome {nome} está no nível de {nivel[1]}")

elif xp > 2001 and xp < 5000:
    print(f"O Herói de nome {nome} está no nível de {nivel[2]}")

elif xp > 5001 and xp < 7000:
    print(f"O Herói de nome {nome} está no nível de {nivel[3]}")

elif xp > 7001 and xp < 8000:
    print(f"O Herói de nome {nome} está no nível de {nivel[4]}")

elif xp > 8001 and xp < 9000:
    print(f"O Herói de nome {nome} está no nível de {nivel[5]}")

elif xp > 9001 and xp < 10000:
    print(f"O Herói de nome {nome} está no nível de {nivel[6]}")

elif xp >= 10001:
    print(f"O Herói de nome {nome} está no nível de {nivel[7]}")
