# function to calculate simple interest

def simple_interest(principal, rate, time):

    interest = (principal * rate * time) / 100

    return interest


# function to calculate compound interest

def compound_interest(principal, rate, time):

    amount = principal * (pow((1 + rate / 100), time))

    interest = amount - principal

    return interest