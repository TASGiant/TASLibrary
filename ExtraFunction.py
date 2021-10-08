class ExtraFunction:

    @staticmethod
    def sum_double(a, b):
        if a == b:
            return 2 * (a + b)
        else:
            return a + b

    @staticmethod
    def makes(a, b, c):
        if a + b == c:
            return True
        elif a == c or b == c:
            return True
        else:
            return False

    @staticmethod
    def near_num(Num, Target_Num, Near_Num):
        if abs(Target_Num - Num) <= Near_Num:
            return str(Num) + " is near to " + str(Target_Num)
        else:
            return str(Num) + " is not near to " + str(Target_Num)

    class Print:

        @staticmethod
        def sum_double(a, b):
            if a == b:
                print(2 * (a + b))
            else:
                print(a + b)

        @staticmethod
        def makes(a, b, c):
            if a + b == c:
                print(True)
            elif a == c or b == c:
                print(True)
            else:
                print(False)

        @staticmethod
        def near_num(Num, Target_Num, Near_Num):
            if abs(Target_Num - Num) <= Near_Num:
                print(str(Num) + " is near to " + str(Target_Num))
            else:
                print(str(Num) + " is not near to " + str(Target_Num))
