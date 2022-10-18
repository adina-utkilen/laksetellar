antallLaks = int(input("Hvor mange lakser vil du ha?"))

def laksefunksjon(x):
    if x == 1:
        print("1 laks")
    elif x > 1:
        print("1 laks")
        for x in range(2, x+1):
            print(x, "laksar")

laksefunksjon(antallLaks)