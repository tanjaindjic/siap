# from googlemaps import GoogleMaps
#
# gmaps = GoogleMaps('AIzaSyBfAColFj5kqMuSa8WG7NJ2WJZte3O4x8Y')
# lat, lng = gmaps.address_to_latlng("Italy - Sicily & Sardinia")
# print("lat: "+str(lat))
# print("lng: "+str(lng))



# import requests
# url = 'https://maps.googleapis.com/maps/api/geocode/json?address=Italy+Sicily+Sardinia&key=AIzaSyBfAColFj5kqMuSa8WG7NJ2WJZte3O4x8Y'
# response = requests.post(url, data=None)
# print(response.text)
#
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
# location = geolocator.geocode("Sicily, Italy")
# print(location.longitude)
#######################################################
#EMBEDDING: DOC 2 VEC --> create model
# import json
# from gensim.models.doc2vec import Doc2Vec, TaggedDocument
# from nltk.tokenize import word_tokenize
#
# with open('winemag-data-130k-v2.json') as f:
#     data = json.load(f)
# najboljaVina = []
# for d0 in data:
#     if (int(d0['points']) > 96):
#         najboljaVina.append(d0['description'])
# documents = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(najboljaVina)]
# max_epochs = 20
# vec_size = 1
# alpha = 0.01
#
# model = Doc2Vec(vector_size=vec_size,
#                 alpha=alpha,
#                 min_alpha=0.00025,
#                 min_count=1,
#                 dm=1)
#
# model.build_vocab(documents)
#
# for epoch in range(max_epochs):
#     print('iteration {0}'.format(epoch))
#     model.train(documents,
#                 total_examples=model.corpus_count,
#                 epochs=model.iter)
#     # decrease the learning rate
#     model.alpha -= 0.0002
#     # fix the learning rate, no decay
#     model.min_alpha = model.alpha
#
# model.save("d2v.model")
# print("Model Saved")
#######################################################
#EMBEDDING: DOC 2 VEC --> make numbers
# from gensim.models.doc2vec import Doc2Vec
# from nltk.tokenize import word_tokenize
# import json
# import numpy as np
#
# model= Doc2Vec.load("d2v.model")
#
# with open('winemag-data-130k-v2.json') as f:
#     data = json.load(f)
# for d0 in data[:20]:
#     test_data = word_tokenize(d0['description'].lower())
#     v1 = model.infer_vector(test_data)
#     print("V1_infer", v1)
#
# # to find most similar doc using tags
# similar_doc = model.docvecs.most_similar('1')
# print(similar_doc)
#
#
# #to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
# print(model.docvecs['1'])