from task1 import absensi
import unittest

class cekJumlah(unittest.TestCase):
    def test_absensiDosen(self):
        self.assertEqual(absensi.jlhD(), 2)
    
    def test_absensiMHS(self):
        self.assertEqual(absensi.jlhM(), 4)
        
if __name__ == '__main__':
    unittest.main()