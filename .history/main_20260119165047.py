from naive import naive

while(True):
    print("Witaj użytkowniku!")
    temp = input("Podaj ciąg znaków (każda liczba musi być oddzielona spacją, kliknij enter aby przerwać): ")
    print("=================================")

    if(temp == ''): break

    lista = [];
    for i in temp.split(' '):
        
        try:
            lista.append(int(i))
        except:
            continue
    
    result = naive(lista)
    print(result)
