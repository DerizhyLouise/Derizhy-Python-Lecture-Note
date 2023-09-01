class segiEmpat:
    sisi1 = 0
    sisi2 = 1
    sisi3 = 2
    sisi4 = 3
    def keliling (self):
        return self.sisi1 + self.sisi2 + self.sisi3 + self.sisi4
    
class persegi (segiEmpat):
    def luas(self, s):
        return s * s