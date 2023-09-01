from Kalku import kalku

def test_tambah():
    assert kalku.tambah(10,-30) == -20

def test_kurangBenar():
    assert kalku.kurang(10,-30) == 40
    
def test_kurangSalah():
    assert kalku.kurang(10,-30) == -40

def test_kali():
    assert kalku.kali(10,-30) == -300

def test_bagi():
    assert kalku.bagi(10,-20) == -0.5