class Square:

    @staticmethod
    def square(FirstNumber, SecondNumber):
        return FirstNumber ** 2 + 2 * FirstNumber * SecondNumber + SecondNumber ** 2

    @staticmethod
    def singleSquare(Number):
        return Number ** 2

    @staticmethod
    def square_(FirstNumber, SecondNumber):
        return FirstNumber ** 2 - 2 * FirstNumber * SecondNumber + SecondNumber ** 2

    class Extended:

        @staticmethod
        def square(FirstNumber, SecondNumber, ThirdNumber):
            return FirstNumber ** 2 + SecondNumber ** 2 + ThirdNumber ** 2 + 2 * FirstNumber * SecondNumber + \
                   2 * SecondNumber * ThirdNumber + 2 * FirstNumber * ThirdNumber


class Cube:

    @staticmethod
    def cube(FirstNumber, SecondNumber):
        return FirstNumber ** 3 + 3 * FirstNumber ** 2 * SecondNumber + 3 * FirstNumber * SecondNumber ** 2 + \
                   SecondNumber ** 3

    @staticmethod
    def cube_(FirstNumber, SecondNumber):
        return FirstNumber ** 3 - 3 * FirstNumber ** 2 * SecondNumber + 3 * FirstNumber * SecondNumber ** 2 - \
               SecondNumber ** 3


class Power:

    @staticmethod
    def power(FirstNumber, SecondNumber):
        return FirstNumber ** SecondNumber


class ProducerFormula:

    @staticmethod
    def a2substractb2(a, b):
        return (a + b) * (a - b)

    @staticmethod
    def a3addb3(a, b):
        return (a + b)*(a ** 2 - a * b + b ** 2)


class Print:

    class Square:

        @staticmethod
        def square(FirstNumber, SecondNumber):
            print(FirstNumber ** 2 - 2 * FirstNumber * SecondNumber + SecondNumber ** 2)

        @staticmethod
        def square_(FirstNumber, SecondNumber):
            print(FirstNumber ** 2 - 2 * FirstNumber * SecondNumber + SecondNumber ** 2)

        @staticmethod
        def singleSquare(Number):
            print(Number ** 2)

        class Extended:

            @staticmethod
            def square(FirstNumber, SecondNumber, ThirdNumber):
                print(FirstNumber ** 2 + SecondNumber ** 2 + ThirdNumber ** 2 + 2 * FirstNumber * SecondNumber +
                      2 * SecondNumber * ThirdNumber + 2 * FirstNumber * ThirdNumber)

        class Cube:

            @staticmethod
            def singleCube(Number):
                print(Number ** 3)

            @staticmethod
            def cube(FirstNumber, SecondNumber):
                print(FirstNumber ** 3 + 3 * FirstNumber ** 2 * SecondNumber + 3 * FirstNumber * SecondNumber ** 2 +
                      SecondNumber ** 3)

            @staticmethod
            def cube_(FirstNumber, SecondNumber):
                print(FirstNumber ** 3 - 3 * FirstNumber ** 2 * SecondNumber + 3 * FirstNumber * SecondNumber ** 2 -
                      SecondNumber ** 3)

        class Power:
            @staticmethod
            def power(FirstNumber, SecondNumber):
                print(FirstNumber ** SecondNumber)
