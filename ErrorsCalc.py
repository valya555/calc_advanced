
class InputError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid Input Given."

class FloatError(Exception):
    
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid Use Of Decimal Dot."