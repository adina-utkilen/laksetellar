antallLaks =ut("Hvor mange lakser vil du ha?"))

def laksefunksjon(x):
    if antallLaks == 1:
        print("1 laks")
    elif antallLaks > 1:
        print("1 laks")
        for x in range(2, antallLaks+1):
            print(x, "laksar")

laksefunksjon(antallLaks)