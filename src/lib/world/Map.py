from noise import snoise2

class Map:

    @staticmethod
    def icon(x, y):
        height = snoise2(x/10, y/10)

        if (height < 0):
            return "  "
        elif (height < 0.3):
            return "~ "
        elif (height < 0.9):
            return "# "
        else:
            return "/\\"

    @staticmethod
    def getMap(x, y, size=10):
        result = ""
        for i in range(x - size, x + size):
            for j in range(y - size, y + size):
                result += Map.icon(i, j)
            result += "\n"
        return result