class Mobil:
    def __init__(self, warna, merek, kecepatan) :
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 20

    
mobil_1 = Mobil("Hitam", "Mercedes", 220)
print(mobil_1.warna)
print(mobil_1.merek)
print("Sebelum ditambah kecepatan: ")
print(mobil_1.kecepatan)     

mobil_1.tambah_kecepatan()
print("\nSetelah Bore up: ")
print(mobil_1.kecepatan)


class Mobil_Sport:
    def __init__(self, merek, kecepatan, turbo) :
        self.merek = merek
        self.kecepatan = kecepatan
        self.turbo = turbo

    def upgrade_turbo(self):
        self.turbo += "320kmh" 

mobil_1 = Mobil_Sport("lamborgini", "250kmh", "Setelah upgrade turbo ")
print("\nMobil Sport: ")
print(mobil_1.merek)
print(mobil_1.kecepatan)

mobil_1.upgrade_turbo()
print(mobil_1.turbo)




    
