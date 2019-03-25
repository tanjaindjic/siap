import jsonpickle
from json import JSONEncoder
class Vino(JSONEncoder):
    def default(self, o):
        return o.__dict__
    def __init__(self):
        pass
    def initialize(self, country, description, points, price, province, taster_name, title, variety, winery, descNum ):
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
        data['descNum'] = self.descNum
        return data

    def __str__(self):
        return "Vino country is %s, description is %s, tittle is %s" % (self.country, self.description, self.title)

    def transform(v):
        return jsonpickle.encode(v, unpicklable=False)