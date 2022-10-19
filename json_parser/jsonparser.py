import json

with open ('./sample.json', 'r') as f:
    data = json.load(f)
    data = data['data']
    for i in data[:1]:
        beer_name = i['name']
        beer_desc = i['description']        
        srm = i['srm']
        beer_srmHex = srm['hex']
        glass = i['glass']