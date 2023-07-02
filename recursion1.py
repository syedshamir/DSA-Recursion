def TestRecursion(n):
    if(n>0):
        print("/n", n)
        TestRecursion(n-1)

if __name__ == "__main__":
    TestRecursion(3)

#time complexity is n +1 i.e 3 + 1 = 4
# https://www.geeksforgeeks.org/how-to-analyse-loops-for-complexity-analysis-of-algorithms/
