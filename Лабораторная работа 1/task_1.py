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


territory_name = "Пушкин"
territory_area = 28676
green_zones = [302, 487, 420, 325, 471, 363, 404]
value = GreenZoneIndex(territory_name, territory_area, green_zones)
value.green_index
print(f"Индекс озеленения территории {value.territory_name} равен {value.green_index}%")