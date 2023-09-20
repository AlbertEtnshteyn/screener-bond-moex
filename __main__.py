from lib import moex
import datetime
import click

def main():
    # bonds = moex.get_bonds(1, 100)
    # print(bonds)

    for p in range(1, 1000):
        bonds = moex.get_bonds(p, 100)
        print(bonds)
        if len(bonds) < 1:
            print(f"Закончила обновлять список облигаций на стр. № {p}")
            break

if __name__ == '__main__':
    main()
