
class Atribut():
    def __init__(self, category_name, subcategory_name, specific_name, normalized_name):
        self.category_name = category_name
        self.subcategory_name = subcategory_name
        self.specific_name = specific_name
        self.normalized_name = normalized_name
    def __str__(self):
        return "Atribut: category_name - %s, subcategory_name - %s, specific_name - %s, normalized_name - %s" % (self.category_name, self.subcategory_name ,self.specific_name, self.normalized_name)
