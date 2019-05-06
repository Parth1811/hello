def per (n, count = 1):
    if len(n) == 1:
        print "total count = " + str(count)
        print "Done"
        return

    result = 1
    for i in n:
        result *= int(i)

    per(str(result), count + 1)

if __name__ == '__main__':
    n = raw_input()
    while n != 'c':
        n = raw_input()
        per(n)
