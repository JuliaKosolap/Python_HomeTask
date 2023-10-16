class City:
    __city_name: str = "no name"
    __region_name: str = "no name"
    __country_name: str = "no name"
    __citizens_number: int = 0
    __postal_code: int = 0
    __tel_code: str = "000"

    def __init__(self, city_name, region_name, country_name, citizens_number, postal_code, tel_code):
        self.set_city_name(city_name)
        self.set_region_name(region_name)
        self.set_country_name(country_name)
        self.set_citizens_number(citizens_number)
        self.set_postal_code(postal_code)
        self.set_tel_code(tel_code)

    def set_city_name(self, city_name):
        if 1 < len(city_name) < 50:
            self.__city_name = city_name
        else:
            print("Incorrect city name length!")

    def get_city_name(self):
        return self.__city_name

    def set_region_name(self, region_name):
        if 2 < len(region_name) < 50:
            self.__region_name = region_name
        else:
            print("Incorrect region city name length!")

    def get_region_name(self):
        return self.__region_name

    def set_country_name(self, country_name):
        if 2 < len(country_name) < 50:
            self.__country_name = country_name
        else:
            print("Incorrect country name length")

    def get_country_name(self):
        return self.__country_name

    def set_citizens_number(self, citizens_number):
        if 20 < citizens_number < 100000000:
            self.__citizens_number = citizens_number
        else:
            print("Invalid citizens number!")

    def get_citizens_number(self):
        return self.__citizens_number

    def set_postal_code(self, postal_code):
        if 0 <= postal_code < 100000:
            self.__postal_code = postal_code
        else:
            print("Invalid postal code!")

    def get_postal_code(self):
        return self.__postal_code

    def set_tel_code(self, tel_code):
        if 2 < len(tel_code) < 5:
            self.__tel_code = tel_code
        else:
            print("Invalid tel code!")

    def get_tel_code(self):
        return self.__tel_code

    def show_info(self):
        print(f"City name: {self.__city_name}, region: {self.__region_name}, country: {self.__country_name},"
              f" citizens number: {self.__citizens_number}, postal code: {self.__postal_code}, tel code: {self.__tel_code}")


city = City("Kyiv", "Kyiv region", "Ukraine",
            2952000, 0, "044")
city.show_info()
