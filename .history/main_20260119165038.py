from naive import naive

while(True):
    print("Witaj użytkowniku!")
    temp = input("Podaj ciąg znaków (każda liczba musi być oddzielona spacją, kliknij enter aby przerwać): ")
    print("=================================")

    if(temp == ''): break


    lista = [];
    for i in temp.split(' '):
        print(lista)

        if(i.isnumeric()):
            lista.append(i)
        else:
            print("Dane zostały źle wprowadzone! Proszę spróbować jeszcze raz.")
            continue
        


    result = naive(lista)
    print(result)
