import time

def countDown(t):

    while t>= 0:
        mins , secs = divmod(t , 60)
        print("{} : {}".format(mins,secs))
        time.sleep(1)
        t -= 1
    print("Sayaç Bitti")
value = input("Bir Değer Giriniz: ")
countDown(int(value))



