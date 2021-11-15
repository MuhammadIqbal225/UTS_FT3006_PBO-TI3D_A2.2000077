class Kendaraan:

    
    def __init__(self, inputName, inputFuel):
        self.name = inputName
        self.inputfuel = inputFuel
        Kendaraan.jumlah += 1
        print("membuat kendaraan dengan nama" + inputName)
        print("banyak bahan bakan kendaraan" + inputFuel)


mobil1 = Kendaraan("yaris",100)
print(Kendaraan.jumlah)
mobil2 = Kendaraan("pajero",110)
print(Kendaraan.jumlah)
mobil3 = Kendaraan("pick up",1000)
print(Kendaraan.jumlah)

