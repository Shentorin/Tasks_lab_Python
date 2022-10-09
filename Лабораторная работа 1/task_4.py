class GreenZoneIndex:
    def __init__(self, territory_name: str, territory_area: int, green_zones: list):
        """
        :param territory_name: Название территории
        :param territory_area: Площадь территории
        :param green_zones: Список площадей парков
        """

        self.territory_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones

        self.green_index = None  # индекс озеленения
        self.green_index = self.calculate_green_index()

    def calculate_green_index(self):
        calculate_green_index = sum(self.green_zones) / self.territory_area * 100
        return round(calculate_green_index, 2)


list_territories = [
    {
        "territory_name": "Пушкин",
        "territory_area": 28676,
        "green_zones": [302, 487, 420, 325, 471, 363, 404]
    },
    {
        "territory_name": "Павловск",
        "territory_area": 21025,
        "green_zones": [360, 375, 223, 258, 345, 296, 303]
    },
    {
        "territory_name": "Петергоф",
        "territory_area": 44274,
        "green_zones": [364, 447, 438, 223, 336, 431, 442]
    },
]

green_index_new_list = []

for territories in list_territories:
    territory_name = territories.get("territory_name")
    territory_area = territories.get("territory_area")
    green_zones = territories.get("green_zones")

    value = GreenZoneIndex(territory_name, territory_area, green_zones)
    value = value.green_index
    green_index_new_list.append(value)

    def filter_min_green_index(green_index_new_list, min_value = 0.1):

        counter_for_min_value = 0

        for item in green_index_new_list:
            if item > min_value:
                counter_for_min_value += 1

            return counter_for_min_value

    print(filter_min_green_index(green_index_new_list))