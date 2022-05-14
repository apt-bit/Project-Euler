def addfib(L):
    L.append(L[-1]+L[-2])

def main():
    fib = [1,2]
    while fib[-1] < 4000000:
        addfib(fib)
    print(sum([x for x in fib if x%2==0]))

if __name__ == '__main__':
    main()
