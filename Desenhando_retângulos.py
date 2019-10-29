larg = int(input("digite a largura:"))
alt = int(input("digite a altura:"))
coluna = 1
altura = 1


while alt >= altura:
    altura = altura + 1
    while larg >= coluna:
            print ("#", end = "")
            coluna = coluna + 1        
    coluna  =  1
    print()

    