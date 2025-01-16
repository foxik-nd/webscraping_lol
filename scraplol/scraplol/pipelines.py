import re

class ScraplolPipeline:
    def process_item(self, item, spider):
        if not item['armure']:
            item['armure'] = "Erreur de valeur"
        else:
            try:
                item['armure'] = int(item['armure']) 
            except ValueError:
                item['armure'] = "Erreur de valeur"
        

        if not item['health']:
            item['health'] = "Erreur de valeur"
        else:
            try:
                item['health'] = int(item['health'])
            except ValueError:
                item['health'] = "Erreur de valeur"

        if not item['health_regeneration_5s']:
            item['health_regeneration_5s'] = 0.0
        else:
            try:
                item['health_regeneration_5s'] = float(item['health_regeneration_5s']) 
            except ValueError:
                item['health_regeneration_5s'] = "Erreur de valeur"

        if not item['damage']:
            item['damage'] = 0.0
        else:
            try:
                item['damage'] = float(item['damage'])
            except ValueError:
                item['damage'] = "Erreur de valeur"

        if not item['image_url']:
            item['image_url'] = "URL image manquante"

        else:
            item['image_url'] = re.sub(r'\.png.*$', '.png', item['image_url'])
        
        
        return item