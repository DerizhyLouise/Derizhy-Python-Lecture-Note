# Import

import Tester #Tester adalah nama file yang diimport atau disebut module

print(Tester.c)
print(Tester.d)

Tester.manusia()

# Module

import Tester as t

t.tambah(1,2)
t.kurang(5,4)

from Tester import * # Untuk mengimport keseluruhan Tester.py
kali(3,5)

from Tester import tambah as t
t(8,2)