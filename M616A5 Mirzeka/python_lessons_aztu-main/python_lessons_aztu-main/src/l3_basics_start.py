duyun5 = [None, "E", None]
duyun4 = [None, "D", duyun5]
duyun5[0] = duyun4  
duyun3 = [None, "C", duyun4]
duyun4[0] = duyun3  
duyun2 = [None, "B", duyun3]
duyun3[0] = duyun2  
duyun1 = [None, "A", duyun2]
duyun2[0] = duyun1  
cari = duyun1
while cari is not None:
    print(cari[1])
    cari = cari[2] 
cari = duyun5
while cari is not None:
    print(cari[1])
    cari = cari[0]  