def divide_nums(num1, num2):
    """This method will be used to divide the first number by the second.
    Includes robust error handling for zero division.

    :param int num1: The numerator (number to be divided)
    :param int num2: The denominator (number to divide by)

    :returns: The quotient of the division, or an error string
    :rtype: float or str
    """
    try:
        answer = num1 / num2
        return answer
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."