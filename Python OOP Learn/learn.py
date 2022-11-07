# kalo pake kurung, inheritance mau nge extend class lain
# constructor -> initial value
# biasanya constructor itu method, kalo di java nama methodnya sama kaya nama class
class Manusia:

    # tiap method di dalem class, seminimal2 nya satu argumen yaitu self.
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def print(self):
        print(f"nama {self.nama} umur {self.umur}")


test = Manusia("fabian", 19)
test.print()
print(isinstance(test, Manusia))
