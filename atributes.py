class Atribut:
    def __init__(self, category, subcategory, specific, normalized, weight):
        self.category = category
        self.subcategory = subcategory
        self.specific = specific
        self.normalized = normalized
        self.weight = weight

    def __str__(self):
        return "Atribut: category - %s, subcategory - %s, specific - %s, normalized - %s" % (self.category, self.subcategory, self.specific, self.normalized)
