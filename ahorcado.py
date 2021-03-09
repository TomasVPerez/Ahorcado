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

    while errores < len(fases) - 1: #-1 porque las fases arrancan en 0 y los errores en 1
        print("\n")
        msg = "Prueba una letra: "
        letra = input(msg)
        if letra in letrasFaltantes: 
            indiceLetra = letrasFaltantes.index(letra) #Busco el indice de la primer ocurrencua de la letra en las letras faltantes
            pizarra[indiceLetra] = letra #Actualizo la pizarra remplazando el espacio vacio correspondiente por la letra adivinada
            letrasFaltantes[indiceLetra] = "$" #Reemplazo en la lista de letras faltantes la letra adivinada por un "$" ya que es mas facil que removerla de la lista
            print("Correcto!")
            print("-"*15)
            print(" ".join(pizarra))
            print("-"*15)
        else:
            errores += 1
            print("Error!")
            print("-"*15)
            print(" ".join(pizarra)) #Muestro la pizarra para que el jugador la vea
            print("-"*15)
            faseFinal = errores + 1 #La fase final es los errores +1 ya que al hacer slice debo incluir el ultimo elemento
            print("\n".join(fases[:faseFinal])) #Muestro las fases basadas en la cantidad de errores
        if "__" not in pizarra:
            print("Ganaste!")
            break 

            

