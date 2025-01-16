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
        name = response.css("h1.page-header__title::text").get().split(" (")[0].strip().replace(" ", "")
    
        yield {
            'name': response.css("h1.page-header__title::text").get().split(" (")[0].strip(),
            'image_url': response.css(".pi-image-thumbnail::attr(src)").get(),
            'armure': response.css(f"#Armor_{name}::text").get(),
            'health': response.css(f"#Health_{name}::text").get(),
            'health regeneration (5s)': response.css(f"#HealthRegen_{name}::text").get(),
            'damage': response.css(f"#AttackDamage_{name}::text").get(),
        }

