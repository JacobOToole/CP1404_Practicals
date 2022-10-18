"""

"""


def main():
    champions = read_champions()
    champion_countries = read_champion_countries()
    display_champions(champions, champion_countries)


def read_champions():
    champions_list = []
    with open('wimbledon.csv', "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            detail_list = line.split(',')
            champions_list.append(detail_list[2])
            champions = {i: champions_list.count(i) for i in champions_list}
        champions.pop("Champion")
        return champions


def read_champion_countries():
    champion_country_set = set()
    with open('wimbledon.csv', "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            detail_list = line.split(',')
            champion_country_set.add(detail_list[3])
    champion_country_set.remove('Country')
    sorted(champion_country_set)
    return champion_country_set


def display_champions(champions, champion_countries):
    print("Wimbledon Champions:")
    for champion in champions:
        print(f"{champion} {champions[champion]}")
    print(f"These {len(champion_countries)} countries have won Wimbledon:")
    print(", ".join(champion_countries))


main()
