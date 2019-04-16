from json import JSONEncoder
class LLVino(JSONEncoder):
    def default(self, o):
        return o.__dict__
    def __init__(self):
        pass
    def initialize(self, longitude, description, points, price, latitude, taster_name, title, variety, winery, pointGroup ):
        self.longitude = longitude
        self.description = description
        self.points = points
        self.price = price
        self.latitude = latitude
        self.taster_name = taster_name
        self.title = title
        self.variety = variety
        self.winery = winery
        self.pointGroup = pointGroup

        return self

    def to_dict(self):
        data = {}
        data['longitude'] = self.longitude
        data['description'] = self.description
        data['points'] = self.points
        data['price'] = self.price
        data['latitude'] = self.latitude
        data['taster_name'] = self.taster_name
        data['title'] = self.title
        data['variety'] = self.variety
        data['winery'] = self.winery
        data['pointGroup'] = self.pointGroup
        return data

    def __str__(self):
        return "Vino longitude is %s, description is %s, tittle is %s" % (self.longitude, self.description, self.title)
