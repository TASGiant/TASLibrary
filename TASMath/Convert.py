class Temperature:
    class Fahrenheit:

            @staticmethod
            def celsius(C):
                return ((C - 32) * 5) / 9

            @staticmethod
            def kelvin(K):
                return (((K - 32) * 5) / 9) + 273.15

    class Celcious:

            @staticmethod
            def fahrenheit(C):
                return ((C * 9) / 5) + 32

            @staticmethod
            def kelvin(C):
                return C + 273.15

    class Kelvin:

            @staticmethod
            def celsius(K):
                return K - 273.15

            @staticmethod
            def fahrenheit(K):
                return (K * (9 / 5)) - 459.67

    class Print:

            class Fahrenheit:

                @staticmethod
                def celsius(C):
                    print(((C * 9) / 5) + 32)

                @staticmethod
                def kelvin(F):
                    print((((F - 32) * 5) / 9) + 273.15)

            class Celcious:

                @staticmethod
                def fahrenheit(F):
                    print(((F - 32) * 5) / 9)

                @staticmethod
                def kelvin(C):
                    print(C + 273.15)

            class Kelvin:

                @staticmethod
                def celsius(K):
                    print(K - 273.15)

                @staticmethod
                def fahrenheit(K):
                    print((K * (9 / 5)) - 459.67)
