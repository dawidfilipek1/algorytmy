def naive(lista):
    counter = 0;

    for i in range(0, len(lista)):

        for j in range(i+1, len(lista)):

            if(lista[i] > lista[j]):
                counter+=1
                
    return counter