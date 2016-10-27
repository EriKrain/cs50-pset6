def countEvenPos(cardN):
    summ = 0
    while cardN != 0:
        num = cardN % 10
        num *= 2
        if num // 10 != 0:
            num1 = num % 10
            num = num // 10
            num += num1
        summ = summ + num
        cardN = cardN // 100
    return summ

def countUnevenPos(cardN):
    summ = 0
    while cardN != 0:
        num = cardN % 10
        summ += num
        cardN = cardN // 100
    return summ

def getAmount(n):
    amount = 0
    while n > 1: 
        amount = amount + 1
        n = n / 10
    return amount
    
def getCardNumber():
    print("Number: ", end="")
    cardNumber = (int)(input())
    cardNumberAmount = getAmount(cardNumber)
    if cardNumberAmount < 13 or cardNumberAmount > 16 or cardNumberAmount == 14:
        print("INVALID")
        return 0
    return cardNumber
    
def getTotalSum(amt, cn):
    totalSum = 0
    totalSum = countEvenPos(cn // 10) + countUnevenPos(cn)
    return totalSum

def check(cd, pos):
    a = True
    while a:
        cd = cd // 10
        if pos == 1:
            if cd // 10 == 0:
                a = False
                return cd
        if pos == 2:
            if cd // 100 == 0:
                a = False
                return cd
    
def main():
    cardNumber = getCardNumber()
    amount = getAmount(cardNumber)
    totalSum = getTotalSum(amount, cardNumber)
    if totalSum % 10 != 0:
        print("INVALID")
    else:
        if amount == 13:
            if check(cardNumber, 1) == 4:
                print("VISA")
                return 0
        elif amount == 15:
            if check(cardNumber, 2) == 34 or check(cardNumber, 2) == 37:
                print("AMEX")
                return 0
        elif amount == 16:
            if check(cardNumber, 1) == 4:
                print("VISA")
                return 0
            if check(cardNumber, 2) >= 51 and check(cardNumber, 2) <= 55:
                print("MASTERCARD")
                return 0
        else:
            print("INVALID")
    return 0
    
if __name__ == "__main__":
    main()