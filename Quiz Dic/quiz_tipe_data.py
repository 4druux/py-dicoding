"""
TODO:
Buatlah variabel firstName, lastName, age, isMarried dengan ketentuan:
- firstName: isi dengan nama depan Anda bertipe data string.
- lastName: isi dengan nama belakang Anda bertipe data string.
- age: isi dengan umur Anda bertipe data integer.
- isMarried: isi dengan status pernikahan Anda bertipe data boolean.

Catatan:
- Value variabel harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""

# tipe data string
firstName = "Andrew"
lastName = "Samaga"
age = 21
isMarried = False

print(firstName, lastName, age, isMarried)


# tipe data dictionary
data_diri = {"firstName":"Andrew","lastName":"Samaga", "age":20, "isMarried": False}

print(data_diri)

# prosedur
def greeting(name):
    print(f"Hallo {name}! Selamat Datang")
greeting("Andrew")