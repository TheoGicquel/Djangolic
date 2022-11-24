import json
from icecream import ic
import os
os.system('clear')

class Glass:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __str__(self):
        return "id:" + str(self.id) + " name:" + str(self.name) + ")"
    
    
class Brewery:
    def __init__(self,id:int,name:str,location:str):
        self.id = id
        self.name = name
class Beer:
    def __init__(self,id:int, name:str,desc:str,srm:hex,glass:Glass,ibu,abv,style_name,style_group,taste,label_icon,label_medium,label_large):
        self.id = "TBD"
        self.name = name
        self.desc = desc[0:30]+"....(shortened for display)"
        self.srm = srm
        self.Glass = glass
        self.abv = abv
        self.ibu = ibu
        self.style_name = style_name
        self.style_group = style_group
        self.desc_taste = taste[0:30]+"...(shortened for display)"

        self.label_icon = label_icon
        self.label_medium = label_medium
        self.label_large = label_large

    def __str__(self):
        out='beer{'
        for attr, value in self.__dict__.items():
            out+=("\n\t"+str(attr) + ": " + str(value))
        out+='\n}'
        return out

    def __set_brewery__(self,brewery:Brewery):
        self.brewery = brewery

def json_open_file(path):
    with open (path, 'r') as f:
        data = json.loads(f.read())
        data = data['data']
        #ic(data)
        for i in data[:2]:
            # meta info
            beer_name = i['name']
            beer_desc = i['description']        
            
            # color (srm)
            srm = i['srm']
            beer_srm = srm['hex']
            
            # glass
            glass = i['glass']
            glass_name = glass['name']
            glass_id = glass['id']
            o_glass = Glass(glass_id,glass_name)
            
            # chemical
            beer_abv = i['abv']
            beer_ibu = i['ibu']
            
            # style
            style = i['style']
            style_name_full = style['shortName']
            
            # get last word of style name
            style_name_short = style_name_full.split()[-1]
            
            # taste
            taste = style['description']
            
            # labels
            labels = i['labels']
            label_icon = labels["contentAwareIcon"]
            label_medium = labels["contentAwareMedium"]
            label_large = labels["contentAwareLarge"]
            
            # class object
            o_beer = Beer(
                0,
                beer_name,
                beer_desc,
                beer_srm,
                o_glass,
                beer_abv,
                beer_ibu,
                style_name_full,
                style_name_short,
                taste,
                label_icon,
                label_medium,
                label_large
            )
            
            
            
            print(o_beer)
            #ic(data[:1])
    
            
            
            
json_open_file('./sample.json')