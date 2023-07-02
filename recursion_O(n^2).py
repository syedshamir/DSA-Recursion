def TestRecursion(n):
    if(n>0):
        for i in range(0,n):
            print("/n", n)
        TestRecursion(n-1)
if __name__ == "__main__":
    TestRecursion(3)

#time complexity is n*n    