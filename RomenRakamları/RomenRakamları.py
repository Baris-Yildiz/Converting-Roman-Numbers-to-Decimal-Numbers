rakam = input("Enter A Roman Number : ")
def LatineCevir(romenrakami):
    result = 0
    romenrakamlari = ['I','V','X','L','C','D','M']
    latinrakamlari = [1,5,10,50,100,500,1000]
    for index in range(len(romenrakami)):
        try:
            if(latinrakamlari[romenrakamlari.index(romenrakami[index])] < latinrakamlari[romenrakamlari.index(romenrakami[index+1])]):
                result -= int(latinrakamlari[romenrakamlari.index(romenrakami[index])])
            else:
                result += int(latinrakamlari[romenrakamlari.index(romenrakami[index])])
        except:
            result += int(latinrakamlari[romenrakamlari.index(romenrakami[index])])
    return result
print(LatineCevir(rakam))




        



