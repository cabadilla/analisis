FichasMano=[1,3,3,3,3,1]
def CombinacionesColor(ListaFichas, N):
    '''
    Objetivo: Funcion que saca las cominaciones de fichas que tenga dependiendo del color
    Recibe: Fichas que tenga en la mano y un numero para poder iterar
    Retorna: La lista de las combinaciones
    '''
    if N>5:
        return []
    else:
        Lista=[]
        Lista.append(ListaFichas[N])
        for i in range(N+1, 6):
            if ListaFichas[i] in Lista:
                Lista.append(ListaFichas[i])
        return [Lista]+CombinacionesColor(ListaFichas, N+1)

print(CombinacionesColor(FichasMano, 0))