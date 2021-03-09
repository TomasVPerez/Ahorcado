def ahorcado(palabra):
    errores = 0
    fases = ["",
            "___________          ",
            "|                    ",
            "|          |         ",
            "|          0         ",
            "|         /|\        ",
            "|         / \        ",
            "|                    "]

    letrasFaltantes = list(palabra)
    pizarra = ["__"] * len(palabra)
    print("Bienvenido al ahorcado!")

    while errores < len(fases) - 1: 
        print("\n")
        msg = "Prueba una letra: "
        letra = input(msg)
        if letra in letrasFaltantes: 
            indiceLetra = letrasFaltantes.index(letra)
            pizarra[indiceLetra] = letra 
            letrasFaltantes[indiceLetra] = "$" 
            print("Correcto!")
            print("-"*15)
            print(" ".join(pizarra))
            print("-"*15)
        else:
            errores += 1
            print("Error!")
            print("-"*15)
            print(" ".join(pizarra)) 
            print("-"*15)
            faseFinal = errores + 1
            print("\n".join(fases[:faseFinal]))
        if "__" not in pizarra:
            print("Ganaste!")
            break 

            

