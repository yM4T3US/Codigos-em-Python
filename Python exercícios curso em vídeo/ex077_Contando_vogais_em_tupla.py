tupla = ("cachorro", "gato", "papagaio", "lebre", "formiga")
for k in tupla:
    print(f"\n{k} = ", end="")
    for letra in k:
        if letra.lower() in "aeiou":
            print(letra, end=" ")