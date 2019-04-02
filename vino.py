from json import JSONEncoder
class Vino(JSONEncoder):
    def default(self, o):
        return o.__dict__
    def __init__(self):
        pass
    def initialize(self, country, description, points, price, province, taster_name, title, variety, winery, pointGroup ):
        self.country = country
        self.description = description
        self.points = points
        self.price = price
        self.province = province
        self.taster_name = taster_name
        self.title = title
        self.variety = variety
        self.winery = winery
        self.pointGroup = pointGroup

        return self

    def to_dict(self):
        data = {}
        data['country'] = self.country
        data['description'] = self.description
        data['points'] = self.points
        data['price'] = self.price
        data['province'] = self.province
        data['taster_name'] = self.taster_name
        data['title'] = self.title
        data['variety'] = self.variety
        data['winery'] = self.winery
        data['pointGroup'] = self.pointGroup
        return data

    def __str__(self):
        return "Vino country is %s, description is %s, tittle is %s" % (self.country, self.description, self.title)
