n = int(input())
t0 = 0
t1 = 1
t2 = 2
tn = 1000000000000
if n < int(0):
    print ('BLAD')
elif n != int (n):
    print ('BLAD')
for n in range (0, int(n)):
    x = int(input())
    if x < int(0):
        print ('BLAD')
    else:
        if x == t0:
            print (x, '\t', 'TAK')
        else:
            for i in range (t2, tn):
                wynik = t0 + t1 + t2
                if x == wynik:
                    print (x, '\t', 'TAK')
                    break
                elif x > wynik:
                    print (x, '\t', 'NIE')
                    break
                else:
                    t0 = t1
                    t1 = t2
                    t2 = wynik
                    wynik = t0 + t1 + t2
