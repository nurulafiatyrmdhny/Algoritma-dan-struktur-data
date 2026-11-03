list_buah = ['Pisang', 'Nanas', 'Semangka', 'Kelubi']

print(list_buah)

# ubah data pertama
list_buah[0] = 'Jeruk'

print(list_buah)

# ubah data terakhir
list_buah[-1] = 'Mangga'

print(list_buah)

# ubah data dalam range 
list_buah[1:3] = ['Alpukat', 'Manggis']

print(list_buah)

# tambah data di belakang list
list_buah.append('Blueberry')
print(list_buah)

# tambah data awal list
list_buah.insert(0, 'Anggur')
print(list_buah)

# tambah data di index mana pun dalam list
list_buah.insert(2, 'Rambutan')
print(list_buah)