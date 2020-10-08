def getPower():
    def getNumber():
        """ Asks for two inputs from the user x1 and x2 --> integer
            Returns x1 to the power of x2

            x1 ** x2 ---> return
            3 ** 2 ---> 9
            """
        # 1. Asks the user to enter a number “x”
        x = int(input("write your desired root: "))
        # 2. Asks the user to enter a number “y”
        y = int(input("write your desired power: "))
        # 3. Prints out number “x”, raised to the power “y”.
        number = x ** y
        print(x, 'to the power of', y, 'is', number)
        return x

    # 4. Prints out the log (base 2) of “x”.
    def getLog():
        """Returns a rounded approximation to the result of log (base 2) x1 from getNumber function

           log(base 2)8 ---> 3"""
        number = getNumber()
        epsilon = 0.01
        step = epsilon ** 2
        exponent = 0
        while abs(2 ** exponent - number) >= epsilon and exponent < number:
            exponent += step

        # import numpy as np
        # exponent = np.log2(number)

        print('Log base 2 of', number, 'is', round(exponent, 2))
        return exponent

    return getLog()

getPower()
