import random

from palavras_forca import lista1

palavra = random.choice(lista1).lower() 

letras_user = [] 

chances = 5 

ganhou = False 

while True:
    print("🪢 😵🪑 ⋮ ⌗ ┆ Bem vindo à Forca.ᐟ")
    print(" ") 
    print(f"🏮 ⋮ ⌗ ┆ Você tem {chances} chances ՞. .՞") 
    print(" ") 
    print("💡 ⋮ ⌗ ┆ Letras que já foram:", end = " " ) 
    print(f"{letras_user} ⊂⁠(⁠´⁠･⁠◡⁠･⁠⊂⁠ )⁠∘⁠˚⁠˳⁠°") 
    print(" ") 
    for letra in palavra: 
            if letra.lower() in letras_user:  
                print(letra, end = " ") 
            else: 
                print("_", end = " ") 
    print(" ") 
    print(" ") 
    tent = input("🔮 ⋮ ⌗ ┆ Escolha uma letra para advinhar a palavra oculta ｡°‧: ").lower() 
    print(" ") 
    if tent not in letras_user: 
        if len(tent) == 1 and tent.isalpha() and tent.isascii(): 
                letras_user.append(tent) 
        else:
                print("🔖 ⋮ ⌗ ┆ Carácter inválido! Tente uma letra sem acento.") 
                print(" ") 
    else: 
        chances == chances 
        print("🎟️ ⋮ ⌗ ┆ Essa letra já foi chutada.ᐟ Tente outra ¯ヾ⁠(⁠･⁠ω⁠･⁠*)⁠ﾉ") 
        print(" ") 
    if tent in letras_user:  
        if tent not in palavra: 
                chances -= 1 
        else: 
                chances == chances
        # if tent not in palavra and len(tent) == 1 and tent.isascii() and tent.isalpha(): 
        if tent not in palavra and tent in letras_user: 
            print("     🚩 ⋮ ⌗ ┆ Letra errada.ᐟ ✗") 
            print(" ") 
        ganhou = True  
        for letra in palavra: 
                if letra not in letras_user: 
                        ganhou = False 
        if chances == 0 or ganhou: 
                break 
if ganhou: 
        print(" ") 
        print(f"Yaaay.ᐟ Você ganhou ₍₍⚞(˶>ᗜ<˶)⚟⁾⁾ A palavra era {palavra}") 

else: 
        print(" ") 
        print(f"Você perdeu ૮◞ ˕ ◟ ྀིა A palavra era {palavra}") 