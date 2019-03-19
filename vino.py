class Vino:
    def __init__(self, country, description, points, price, province, taster_name, title, variety, winery, descNum ):
        self.country = country
        self.description = description
        self.points = points
        self.price = price
        self.province = province
        self.taster_name = taster_name
        self.title = title
        self.variety = variety
        self.winery = winery
        self.descNum = descNum

    def __str__(self):
        return "Vino country is %s, description is %s, tittle is %s" % (self.country, self.description, self.title)
