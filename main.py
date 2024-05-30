import random
import fisherman

class Lobster:
    def __init__(self, size=0, value=0):
        self.size = size
        self.value = value

def main():
    print("------Knapsack in homari------")
    centimeters = int(input("Capacitatea plasei: "))
    no_lobster = int(input("Numarul de homari: "))

    lobsters = [Lobster() for _ in range(no_lobster)]

    print("------Va rog sa introduceti (m) pentru date introduse manual, (a) pentru date alese aleatoriu------")
    while True:
        aleatoriu = input()
        if aleatoriu == 'm':
            fisherman.scan_lobster(lobsters, no_lobster)
            break
        elif aleatoriu == 'a':
            fisherman.generate_lobster(lobsters, no_lobster)
            break
        else:
            print("Caracter invalid. Va rog sa introduceti (m) pentru date introduse manual, (a) pentru date alese aleatoriu!")

    fisherman.print_lobster(lobsters, no_lobster)
    fisherman.lobster_descrete(lobsters, no_lobster, centimeters)

if __name__ == "__main__":
    main()