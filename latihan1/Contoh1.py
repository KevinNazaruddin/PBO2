class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")

mobilA = Mobil("Toyota Kijang Inova", "Hitam")
mobilA.info() # Output: Mobil Toyota Kijang Inova berwarna Hitam