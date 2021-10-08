def pi():
    return 3.14159
    

def pi_25():
    return 3.1415926535897932384626433
    
    
def pi_50():
    return 3.14159265358979323846264338327950288419716939937510
    
    
def pi_100():
    return 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    
    
def currant():
    return 299792458
    
    
def PlanckConstant():
    return 6.62607015 * (10 ** -34)
    

def ChargeOfElectrons():
    return 1.602176634 * (10 ** -19)
    
    
def BoltzmannConstant():
    return 1.380649 * (10 ** -23)
    
    
def AvogadroConstant():
    return 6.022114076 * (10 ** 23)
    
    
def RadiationIntensity():
    return 683


class Number:

    @staticmethod
    def pi(number):
        return number * pi()

    @staticmethod
    def pi_25(number):
        return number * pi_25()

    @staticmethod
    def pi_50(number):
        return number * pi_50()

    @staticmethod
    def pi_100(number):
        return number * pi_100()

    class Print:

        @staticmethod
        def pi(number):
            print(pi() * number)
