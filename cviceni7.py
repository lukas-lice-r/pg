class ferda:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

    def secti(self, jiny_vektor):
        print(f" tady asdfsdafgdasfg   {jiny_vektor}")
        print(self.x)
        xx = self.x + jiny_vektor.x   # ne jiny_vektor[0]
        yy = self.y + jiny_vektor.y
        return f"{xx}, {yy}" 

    def vynasob(self, skalar):
        xx = self.x * skalar
        yy = self.y * skalar
        return f"{xx}, {yy}"



if __name__ == "__main__":

    v1 = ferda(10 ,5)
    print(v1.x, v1.y)
    print(v1)

    v2 = ferda(3, 8)
    print(v1.secti(v2))

    print(v1.vynasob(2))

    print(v1)
    print(v2)