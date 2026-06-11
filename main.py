from src.scrapper import PriceScrapper
from src.database import DatabaseManager

# bot = PriceScrapper()

# product = bot.scrape_product("https://www.kitapyurdu.com/kitap/percy-jackson-ve-olimposlular-simsek-hirsizi/657557.html?filter_name=şimşek+hırsızı&s_token=1580419f36b3bd927e7d23c54eb0c1b3479faa60eaa5c85b21ccd545aba82b28&s_time=1781214248")

# product_data = DatabaseManager()

# product_data.insert_price()


def main():
    bot = PriceScrapper()
    db = DatabaseManager()

    product_info = bot.scrape_product("https://www.kitapyurdu.com/kitap/percy-jackson-ve-olimposlular-simsek-hirsizi/657557.html?filter_name=şimşek+hırsızı&s_token=1580419f36b3bd927e7d23c54eb0c1b3479faa60eaa5c85b21ccd545aba82b28&s_time=1781214248")

    if product_info:
        db.insert_price(product_info["title"], product_info["price"])
        print("Veri başarıyla kazındı, veritabanına kaydedildi")
    else:
        print("Hata var")

main()