import math


class Distance(object):
    def __init__(self, tag, reader):
        self.reader = reader   # these parameters represents readers position as a list of x,y,z
        self.tag = tag         # these parameters represents tags position as a list of x,y,z
        self.x = 0
        self.y = 0
        self.z = 0

    def reader_position(self):
        if len(self.reader) == 5:
            self.x = int(self.reader[0] + self.reader[1])
            self.y = int(self.reader[3] + self.reader[4])
        elif len(self.reader) == 8:
            self.x = int(self.reader[0] + self.reader[1])
            self.y = int(self.reader[3] + self.reader[4])
            self.z = int(self.reader[6] + self.reader[7])
        else:
            print("Wrong Entry: Format is either 20,20,20, or 20,20")
        return self.x, self.y, self.z

    def tag_position(self):
        if len(self.tag) == 5:
            self.x = int(self.tag[0] + self.tag[1])
            self.y = int(self.tag[3] + self.tag[4])
        elif len(self.reader) == 8:
            self.x = int(self.tag[0] + self.tag[1])
            self.y = int(self.tag[3] + self.tag[4])
            self.z = int(self.tag[6] + self.tag[7])
        else:
            print("Wrong Entry: Format is either 20,20,20, or 20,20")
        return self.x, self.y, self.z

    def distance(self):
        if len(self.tag) == len(self.reader):
            xt, yt, zt = self.reader_position()
            xr, yr, zr = self.tag_position()
            x = math.pow(xt-xr, 2)
            y = math.pow(yt-yr, 2)
            z = math.pow(zt-zr, 2)
            return math.sqrt(x + y + z)
        else:
            print("Enter the Correct Matching entries")


if "__main__" == __name__:
    halo = Distance("45,30", "10,50")

    print(halo.tag_position())
    print(halo.reader_position())
    print(halo.distance())
