list_cities = [
    {
        "name": "Москва",
        "population": 12 * 10 ** 6,
    },
    {
        "name": "Санкт-Петербург",
        "population": 5 * 10 ** 6,
    },
    {
        "name": "Ижевск",
        "population": 0.6 * 10 ** 6,
    },
]

filter_population = 10 ** 6

population_new = [item for item in list_cities if item["population"] > filter_population]
print(population_new)