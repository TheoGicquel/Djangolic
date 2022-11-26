import json
from icecream import ic
import os
os.system('clear')

class Glass:
    def __init__(self,id="",name=""):
        self.id = id
        self.name = name
    def __str__(self):
        return "id:" + str(self.id) + " name:" + str(self.name) + ")"
    
    
class Brewery:
    def __init__(self,id:int,name:str,location:str):
        self.id = id
        self.name = name
class Beer:
    def __init__(self,id="TBD", name:str="",desc:str="",srm:hex="",glass:Glass=Glass(),ibu="",abv="",style_name="",style_group="",taste="",label_icon="",label_medium="",label_large=""):
        self.id = id
        self.name = name
        self.desc = desc
        self.srm = srm
        self.Glass = glass
        self.abv = abv
        self.ibu = ibu
        self.style_name = style_name
        self.style_group = style_group
        self.desc_taste = taste

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
        for i in data[:50]:
            # meta info
            # skipping beer if no set name
            if('name' in i):    
                beer_name = i['name']
                pass
            
            if('description' in i):    
                beer_desc = i['description']        
            else:
                beer_desc = ""
                
            # color (srm)
            if('srm' in i):
                srm = i['srm']
                beer_srm = srm['hex']
            else:
                beer_srm = ""
            
            # glass
            if('glass' in i):    
                glass = i['glass']
                glass_name = glass['name']
                glass_id = glass['id']
                o_glass = Glass(glass_id,glass_name)
            else:
                o_glass = Glass()
            # chemical
            if('abv' in i):    
                beer_abv = i['abv']
            else:
                beer_abv = ""
            if('ibu' in i):    
                beer_ibu = i['ibu']
            else:
                beer_ibu = ""
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
                name=beer_name,
                desc=beer_desc,
                srm=beer_srm,
                glass=o_glass,
                abv=beer_abv,
                ibu=beer_ibu,
                style_name= style_name_full,
                style_group=style_name_short,
                taste=taste,
                label_icon=label_icon,
                label_medium=label_medium,
                label_large=label_large
            )
            
            desc = o_beer.ibu
            print(len(desc))
            #ic(data[:1])
    
            
            
            
json_open_file('./beer_1.json')