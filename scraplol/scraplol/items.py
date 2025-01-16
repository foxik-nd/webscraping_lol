import scrapy


class ScraplolItem(scrapy.Item):
    name = scrapy.Field()
    image_url = scrapy.Field()
    armure = scrapy.Field()
    health = scrapy.Field()
    health_regeneration_5s = scrapy.Field()
    damage = scrapy.Field()
   
