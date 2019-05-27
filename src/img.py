import png


class img:
    def __init__(self, width=512, height=512):
        self.width = width
        self.height = height
        self.data = []
        for _ in range(0, self.height):
            for _ in range(0, self.width):
                self.data += [255, 255, 255]

    def _pixelpos(self, x, y):
        if x < 0 or x >= self.width:
            raise IndexError('invalid x')
        if y < 0 or y >= self.height:
            raise IndexError('invalid y')
        return (self.width * y + x) * 3

    def getpixel(self, x, y):
        pos = self._pixelpos(x, y)
        return (self.data[pos], self.data[pos+1], self.data[pos+2])

    def putpixel(self, x, y, rgb):
        pos = self._pixelpos(x, y)
        for i in range(0, 3):
            self.data[pos + i] = rgb[i]

    def save(self, path):
        with open(path, 'wb') as f:
            w = png.Writer(self.width, self.height)
            w.write_array(f, self.data)
            f.close()
