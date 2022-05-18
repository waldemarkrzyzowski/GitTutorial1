krotka1 = (3,4,5)
krotka2 = (1,2,3,4,5,6,7,8,9)

def fun(kr1,kr2):
    for i in kr1:
        if i in kr2:
            continue
        else:
            print("Elementy krotki pierwszej nie znajdują się w krotce drugiej")
            break
    else:
        print("Elementy krotki pierwszej znajdują się w krotce drugiej")

fun(krotka1,krotka2)
