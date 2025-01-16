import scrapy

class ChampionspiderSpider(scrapy.Spider):
    name = "championspider"
    allowed_domains = ["leagueoflegends.fandom.com"]
    start_urls = ["https://leagueoflegends.fandom.com/wiki/List_of_champions"]

    def parse(self, response):
        champions = response.css(".champion-icon a::attr(href)").getall()
        for link in champions:
            yield response.follow(link, self.parse_champion)

    def parse_champion(self, response):
        yield {
            'name': response.css("h1.page-header__title::text").get().split(" (")[0].strip(),
            'image_url': response.css(".pi-image-thumbnail::attr(src)").get(),
            # 'position': response.css(".pi-item[data-source='position'] .pi-data-value::text").get(),
            # 'role': response.css(".pi-item[data-source='class'] .pi-data-value::text").get(),
            # 'damage_type': response.css(".pi-item[data-source='damage'] .pi-data-value::text").get(),
            # 'resource': response.css(".pi-item[data-source='resource'] .pi-data-value::text").get(),
            # 'health':response.css(".pi-smart-data-value pi-data-value pi-font pi-item-spacing pi-border-color::text").get()
        }
