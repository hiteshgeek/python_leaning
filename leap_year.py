def is_leap_year(year):
    """
    Docstrings
    Check if the year is leap year or not
    """
    return (year%4 == 0 and year%100 != 0) or year%400 == 0
        
        
if is_leap_year(2400):
    print("Leap")
else:
    print("Not Leap")

if is_leap_year(1989):
    print("Leap")
else:
    print("Not Leap")
