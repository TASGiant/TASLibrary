pi = 3.14159


class Area:

    @staticmethod
    def circle(r):
        return pi * r ** 2

    @staticmethod
    def triangle(a, b):
        return 0.5 * a * b

    @staticmethod
    def rectangel(a, b):
        return a * b

    class Print:

        @staticmethod
        def circle(r):
            print(pi * r ** 2)

        @staticmethod
        def triangle(a, b):
            print(0.5 * a * b)

        @staticmethod
        def rectangel(a, b):
            print(a * b)
