palabra = input("ingrese texto o palabra ")

palabra_organizada= palabra.replace(" ", "").lower()

print(palabra_organizada, palabra_organizada[::-1])

if palabra_organizada==palabra_organizada[::-1]:
    print("es palindromo")
else:
    print("no es palindromo")