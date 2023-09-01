# Dictionary

member1 = {"ID":101,
           "Nama":"Rayhan",
           "Pekerjaan":"Mahasiswa",
           "Status member":"Gold"
           }

member2 = {"ID":102,
           "Nama":"Margaret",
           "Pekerjaan":"Admin",
           "Status member":"Diamond"
           }

memberlist = {101:member1,102:member2}
print(member1["Pekerjaan"],"\n")
print(member1.keys(),"\n")
print(member1.values(),"\n")
print(member1.items(),"\n")
print(memberlist[102])

'''
Dictionary :
"variable = {keys,values}"
'''
