def evenoddChecker():
    num = int(input("Enter a number : "))
    result = "even" if (num % 2 == 0) else "odd"
    print(result)


def tempCheck():
    temp = int(input("Enter temprature"))

    result = "Very hot" if (temp > 30 )else "warm" if(temp > 20) else "cool" if (temp > 10) else "cold" if (temp > 0) else "freez"
    print(result)

tempCheck()