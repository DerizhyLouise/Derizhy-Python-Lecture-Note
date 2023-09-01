def convert (Juubi):
    'mengubah ke integer'
    try:
        ekor = int(Juubi)
        print("Konversi berhasil Juubi berekor =", ekor)
    except:
        print("Konversi gagal!")
        ekor = -1
    return ekor

print(convert("Tidak mungkin Juubi memiliki ekor sebanyak 69"))