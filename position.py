import math


class Position(object):

    def __init__(self, pos1: str = "00,00,00", pos2: str = "40,00,00", pos3: str = "00,45,00", pos4: str = "40,45,00",
                 wg1: float = 1, wg2: float = 1, wg3: float = 1, wg4: float = 1):
        self.wg1 = wg1
        self.pos1 = pos1
        self.wg2 = wg2
        self.pos2 = pos2
        self.wg3 = wg3
        self.pos3 = pos3
        self.wg4 = wg4
        self.pos4 = pos4

    def mahala(self):
        if len(self.pos1) == 8:
            a = self.wg1 * int(self.pos1[0] + self.pos1[1])
            b = self.wg1 * int(self.pos1[3] + self.pos1[4])
            c = self.wg1 * int(self.pos1[6] + self.pos1[7])

            d = self.wg2 * int(self.pos2[0] + self.pos2[1])
            e = self.wg2 * int(self.pos2[3] + self.pos2[4])
            f = self.wg2 * int(self.pos2[6] + self.pos2[7])

            g = self.wg3 * int(self.pos3[0] + self.pos3[1])
            h = self.wg3 * int(self.pos3[3] + self.pos3[4])
            i = self.wg3 * int(self.pos3[6] + self.pos3[7])

            j = self.wg4 * int(self.pos4[0] + self.pos4[1])
            k = self.wg4 * int(self.pos4[3] + self.pos4[4])
            lm = self.wg4 * int(self.pos4[6] + self.pos4[7])

            return math.fabs(a + d + g + j), math.fabs(b + e + h + k), math.fabs(c + f + i + lm)
        else:
            a = self.wg1 * int(self.pos1[0] + self.pos1[1])
            b = self.wg1 * int(self.pos1[3] + self.pos1[4])

            c = self.wg2 * int(self.pos2[0] + self.pos2[1])
            d = self.wg2 * int(self.pos2[3] + self.pos2[4])

            e = self.wg3 * int(self.pos3[0] + self.pos3[1])
            f = self.wg3 * int(self.pos3[3] + self.pos3[4])

            g = self.wg4 * int(self.pos4[0] + self.pos4[1])
            h = self.wg4 * int(self.pos4[3] + self.pos4[4])
            return math.fabs(a + c + e + g), math.fabs(b + d + f + h)

# print(Position().mahala())
