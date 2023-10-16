class Country:
    __country_name: str = "no name"
    __continent_name: str = "no name"
    __citizens_number: int = 0
    __tel_code: str = "000"
    __capital_name: str = "no name"
    __cities = []

    def __init__(self, country_name, continent_name, citizens_number, tel_code, capital_name, cities):
        self.set_country_name(country_name)
        self.set_continent_name(continent_name)
        self.set_citizens_number(citizens_number)
        self.set_tel_code(tel_code)
        self.set_capital_name(capital_name)
        self.set_cities(cities)

    def set_country_name(self, country_name):
        if 1 < len(country_name) < 50:
            self.__country_name = country_name
        else:
            print("Incorrect country name length!")

    def get_country_name(self):
        return self.__country_name

    def set_continent_name(self, continent_name):
        if 5 < len(continent_name) < 20:
            self.__continent_name = continent_name
        else:
            print("Incorrect continent name length!")

    def get_continent_name(self):
        return self.__continent_name

    def set_citizens_number(self, citizens_number):
        if 500 < citizens_number < 10000000000000:
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

    def set_capital_name(self, capital_name):
        if 2 < len(capital_name) < 50:
            self.__capital_name = capital_name
        else:
            print("Incorrect capital name length!")

    def get_capital_name(self):
        return self.__capital_name

    def set_cities(self, cities):
        for city in cities:
            self.__cities.append(city)

    def get_cities(self):
        return self.__cities

    def show_info(self):
        print(
            f"Country name: {self.__country_name}, continent: {self.__continent_name}, citizens number: {self.__citizens_number},"
            f" tel code: {self.__tel_code}, capital: {self.__capital_name}, cities: {self.__cities}")


country = Country("Ukraine", "Europe", 52000, "+380",
                  "Kyiv", ["Kyiv", "Dnepro", "Lviv"])
country.show_info()
