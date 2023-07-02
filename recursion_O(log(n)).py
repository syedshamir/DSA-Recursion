def TestRecursion(n):
    i = 1
    if(n>0):
        while i<n:
            print("/n", n)
            i*=2
        TestRecursion(n-1)
if __name__ == "__main__":
    TestRecursion(6)