def Ticket_Pricing(n: int) -> int:
    if n < 5:
        print("Free")
    elif 5 <= n <= 17:
         print(10)
    elif 18 <= n <= 64:
         print(20)
    else:
         print(15)

if __name__ == '__main__':
    n = int(input())
    print(Ticket_Pricing(n))
