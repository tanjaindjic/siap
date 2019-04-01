from sklearn.metrics import jaccard_similarity_score
import formData
from vino import Vino
atributi = []
allCategs = []
zaPoredjenje = []
noveTezine = []
treningSet = []

def get_word_vec(sentence):
    vec = []
    kategorije = []
    sentence = sentence.upper();
    for a in atributi:
        word = a.__getattribute__('normalized')
        if(word in sentence):
            str = a.__getattribute__('category') + " " +  a.__getattribute__('subcategory') + " " +  a.__getattribute__('specific')
            if str not in kategorije:
                kategorije.append(str)
    for c in allCategs:
        if(c in kategorije):
            vec.append(1)
        else:
            vec.append(0)
    return vec
def nadjiDescNum(description):
    y_pred = get_word_vec(description)
   # y_pred = list(map(lambda x,y:x*y,y_pred,noveTezine))
    ret = jaccard_similarity_score(zaPoredjenje, y_pred, True, noveTezine)
   # print('description --> '+str(ret))
    return ret
def nadjiTitlove():
    dataSetic = formData.convertFromJson("trening")
    for ds in dataSetic:
        print(ds['title'])
def loadTreningSet():
    data = formData.convertFromJson("test")
    for v in data:
        treningSet.append(Vino.initialize(Vino(), v['country'], v['description'], v['points'], v['price'], v['province'],
                                v['taster_name'], v['title'], v['variety'], v['winery'], 0))
def processTreningSet():
    countries = []
    provinces = []
    varieties = []
    wineries = []
    taster_names = []
    titles = []
    # print("length: "+str(len(treningSet)))
    for v in treningSet:
        if v.__getattribute__('country') not in countries:
            countries.append(v.__getattribute__('country'))
        if v.__getattribute__('province') not in provinces:
            provinces.append(v.__getattribute__('province'))
        if v.__getattribute__('variety') not in varieties:
            varieties.append(v.__getattribute__('variety'))
        if v.__getattribute__('winery') not in wineries:
            wineries.append(v.__getattribute__('winery'))
        if v.__getattribute__('taster_name') not in taster_names:
            taster_names.append(v.__getattribute__('taster_name'))
        if v.__getattribute__('title') not in titles:
            titles.append(v.__getattribute__('title'))
            #print(v.__getattribute__('title'))
    # print("countries: "+str(len(countries)))
    # print("provinces: "+str(len(provinces)))
    # print("varieties: "+str(len(varieties)))
    # print("wineries: "+str(len(wineries)))
    # print("taster_names: "+str(len(taster_names)))
    # print("titles: "+str(len(titles)))
    len_countries = len(countries)
    len_provinces = len(provinces)
    len_varieties = len(varieties)
    len_wineries = len(wineries)
    len_taster_names = len(taster_names)
    len_title = len(titles)
    for v in treningSet:
        country_index = countries.index(v.__getattribute__('country'))+1
        value_country = (1/len_countries)*country_index
        v.__setattr__('country', value_country)


        province_index = provinces.index(v.__getattribute__('province'))+1
        value_province = (1/len_provinces)*province_index
        v.__setattr__('province', value_province)

        variety_index = varieties.index(v.__getattribute__('variety')) + 1
        value_variety = (1 / len_varieties) * variety_index
        v.__setattr__('variety', value_variety)


        winery_index = wineries.index(v.__getattribute__('winery')) + 1
        value_winery = (1 / len_wineries) * winery_index
        v.__setattr__('winery', value_winery)

        taster_name_index = taster_names.index(v.__getattribute__('taster_name')) + 1
        value_taster_name = (1 / len_taster_names) * taster_name_index
        v.__setattr__('taster_name', value_taster_name)

        title_index = titles.index(v.__getattribute__('title')) + 1
        value_title = (1 / len_title) * title_index
        v.__setattr__('title', value_title)

loadTreningSet()
processTreningSet()
