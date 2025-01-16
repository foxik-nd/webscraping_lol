import scrapy


class ChampionspiderSpider(scrapy.Spider):
    name = "championspider"
    allowed_domains = ["leagueoflegends.fandom.com"]
    start_urls = ["https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki"]

    def parse(self, response):
        pass
