import random
lista1 = ["kian", "gal", "escriptas", "conhecimento", "medo", "morte", "sangue", "energia", "joui", "mia", "verissimo", "arthur", "paranormal", "kaiser", "cesar", "ordem", "caos", "escada", "shinokage", "cineraria", "luzidio", "thiago", "liz", "chris", "magistrada", "anfitriao", "diabo", "deus", "orfeu"]
palavra = random.choice(lista1)
letras_user = []
chances = 4
ganhou = False

while True:
        print("Bem vindo à Forca!")
        print(" ")
        print(f"Você tem {chances} changes.")
        print(" ")
        print("Palavras que já foram:", end = " ")
        print(letras_user)
        for letra in palavra:
                if letra.lower() in letras_user:
                        print(letra, end = " ")
                else:
                        print("_", end = " ")
        print(" ")
        print(" ")
        tent = input("Escolha uma letra para advinhar a palavra oculta!: ").lower()
        print(" ")
        if tent not in letras_user:
                if len(tent) == 1 and tent.isalpha() and tent.isascii():
                        letras_user.append(tent)
                else:
                        print("Carácter inválido! Tente uma letra sem acento.")
                        print(" ")
        else:
                print("Essa letra já foi chutada! Tente outra.")
                print(" ")

        if len(tent) == 1 and tent.isalpha() and tent.isascii():
                if tent not in palavra:
                        chances -= 1
        else:
                chances == chances

        if tent in letras_user:
                chances == chances

        ganhou = True 
        for letra in palavra:
                if letra not in letras_user:
                        ganhou = False

        if chances == 0 or ganhou:
                break

if ganhou:
        print(" ")
        print(f"Parabéns! Você ganhou. A palavra era {palavra}.")
else:
        print(" ")
        print(f"Você perdeu. A palavar era {palavra}.") 