import PerusahaanABC
import unittest

class searchTest(unittest.TestCase):
    def setUp(self):
        self.gudang = PerusahaanABC.gudang1
        self.kode = 12
        
    def testCari(self):
        self.assertEqual(self.gudang.cek(self.kode), self.kode)
        
if __name__ == '__main__':
    unittest.main()