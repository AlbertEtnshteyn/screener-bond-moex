from lib import moex
import json
# import datetime
# import click

def main():
    # bonds = moex.get_bonds(1, 100)
    # print(bonds)
    # limit = 10
    # page = 1
    # bonds = moex.query("securities", group_by="group", group_by_filter="stock_bonds", limit=limit, start=(page-1)*limit)
    # print(type(bonds))

    bonds = dict

    for p in range(1, 1000):
        temp = moex.get_bonds(p, 100)
        if p == 1:
            bonds = temp
            print(bonds[0])
        else:
            print(type(temp['securities']['data']))
            # for list in temp['securities']['data']:
            #     bonds['securities']['data'] = temp['securities']['data']

        if len(bonds) < 1:
            print(f"Закончила обновлять список облигаций на стр. № {p}")
            break

    with open('bonds.json', 'w') as file:
        json.dump(bonds, file)

if __name__ == '__main__':
    main()
