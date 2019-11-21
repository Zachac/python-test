from noise import snoise2

class Map:

    @staticmethod
    def icon(x, y):
        height = snoise2(x/10, y/10)

        if (height < 0):
            return "  "
        else:
            return "~ "

    @staticmethod
    def getMap(x, y):
        result = ""
        for i in range(x - 10, x + 10):
            for j in range(y - 10, y + 10):
                result += Map.icon(i, j)
            result += "\n"
        return result