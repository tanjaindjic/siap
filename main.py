from sklearn.metrics import jaccard_similarity_score
import formData
atributi = []
allCategs = []
zaPoredjenje = []
noveTezine = []

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
    dataSetic = formData.convertFromJson()
    for ds in dataSetic:
        print(ds['title'])

nadjiTitlove()