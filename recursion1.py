def TestRecursion(n):
    if(n>0):
        print("/n", n)
        TestRecursion(n-1)

if __name__ == "__main__":
    TestRecursion(3)