import math


class Numbers(object):

    def __init__(self, tx:  float = 30.0, freq: float = 910 * math.pow(10, 6), rx: float = 0, pl: float = 2,
                 alpha: float = 1, area: float = 1, d=1, g: float = 1):
        self.tx = tx  # Transmit Power in dBm
        self.freq = freq  # UHF frequency in MHz
        self.rx = rx  # Received Power RSSI
        self.c = 3 * math.pow(10, 8)  # Speed of Light
        self.pl = pl  # Path Loss Exponent
        self.area = area  # Cross Section Area of the Tag
        self.g = g  # Antennas Gain
        self.alpha = alpha
        self.d = d  # Distance reader to the reference tag

    def path_loss(self)-> float:
        a = self.tx + 2 * self.g - 20 * math.log(4*math.pi * self.freq/self.c)-20*math.log((self.d/100))
        return a

    def tag_tag(self, d):
        return self.path_loss() + int(8.6859 * math.log((d / 100) * self.alpha) / math.log(math.e))
