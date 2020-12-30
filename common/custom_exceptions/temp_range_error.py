class TempRangeError(Exception):
    pass


class TempInRange(TempRangeError):
    """Raised when the temperature is within the specified range"""
    pass


class TempOutOfRange(TempRangeError):
    """Raised when the temperature is outside the specified range"""
    msg = "The temperature is out of defined range"
    pass

