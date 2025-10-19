import random
import math
nimi = input("Palun sisesta oma nimi:")
kogus = int(input("Mitu juhuslikku ujukoma-arvu soovid genereerida?"))
arvud = [random.uniform(1, 100) for _ in range(kogus)]
keskmine = math.fsum(arvud) / len(arvud)
arvud_str = ", ".join([f"{arv:.2f}" for arv in arvud])
print(f"\nTere, {nimi}!")
print(f"Genereeritud arvud: {arvud_str}")
print(f"Nende arvude keskmine on umbes {keskmine: .2F}.")