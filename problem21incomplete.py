def d(n):
    return sum([i for i in range(1,int(n/2)+1) if n%i == 0])

def test():
    return [i for i in range(1,10000) if i == d(d(i))]

if __name__ == '__main__':
    print(sum(test()))
