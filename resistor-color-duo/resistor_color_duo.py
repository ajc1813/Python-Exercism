def value(colors):
    colour=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    band_one=str(colour.index(colors[0]))
    band_two=str(colour.index(colors[1]))
    band_one+=band_two
    return int(band_one)
