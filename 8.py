def fibonnaci(limite):
    serie=[]
    a,b =0,1
    while a < limite:
        serie.append(a)
        a,b = b, a+b


def fibonnaci2(limite):
    serie=[]
    a,b =0,1
    while a < limite:
        serie.append(a)
        a,b = b, a+b
    return serie

fibonnaci(80)
serie_fibonnaci=fibonnaci2(80)
print(' ')
print(serie_fibonnaci)