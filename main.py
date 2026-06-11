from src.scrapper import PriceScrapper


bot = PriceScrapper()

product = bot.scrape_product("https://www.kitapyurdu.com/kitap/percy-jackson-ve-olimposlular-simsek-hirsizi/657557.html?filter_name=şimşek+hırsızı&s_token=1580419f36b3bd927e7d23c54eb0c1b3479faa60eaa5c85b21ccd545aba82b28&s_time=1781214248")

print(product)
