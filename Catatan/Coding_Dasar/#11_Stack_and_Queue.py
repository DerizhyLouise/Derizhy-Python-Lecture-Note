# Stack / Tumpukan
tumpukan = [1,2,3,4,5]
print("Data sekarang adalah:",tumpukan)

tumpukan.append(6)
print("Data masuk:",6)
print("Data sekarang:",tumpukan)
tumpukan.append(7)
print("Data masuk:",7)
print("Data sekarang:",tumpukan)

out = tumpukan.pop()
print("Data keluar:",out)
print("Data sekarang:",tumpukan)

print("\n")
# Queue / Antrian
from collections import deque
antrian = deque ([1,2,3,4,5])
print("Data sekarang:",antrian)

antrian.append(6) # Menambah antrian dari depan
print("Data masuk:",6)
print("Data sekarang:",antrian)
antrian.appendleft(0) # Menambah antrian dari belakang
print("Data masuk:",0)
print("Data sekarang:",antrian)

out = antrian.popleft() # Menghapus dari belakang
print("Data keluar:",out) 
print("Data sekarang:",antrian)
out = antrian.pop() # Menghapus dari depan
print("Data keluar:",out)
print("Data sekarang:",antrian)

'''
Perbedaan Stack dan Queue
Stack = Tumpukan, artinya data hanya dapat ditambah atau dihapus dari depan
Queue = Antrian, artinya data dapat ditambah atau dihapus dari mana saja
'''