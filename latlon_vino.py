class LLVino():
    def default(self, o):
        return o.__dict__
    def __init__(self):
        pass
    def initialize(self, description, points, price, taster_name, title, variety, winery, pointGroup, longitude, latitude):
        self.description = description
        self.points = points
        self.price = price
        self.taster_name = taster_name
        self.title = title
        self.variety = variety
        self.winery = winery
        self.pointGroup = pointGroup
        self.longitude = longitude
        self.latitude = latitude
        return self
