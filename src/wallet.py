import config.settings as settings
from util import read_file, write_file, get_text_from_xpath, get_website_content
from terminaltables import AsciiTable
from hashlib import md5


def get_cheap_wallet_table(
    url: str, wallet: list, xpath_pvp: str, xpath_dy: str, xpath_price: str
) -> list:
    price, p_vp, dy, max_price = {}, {}, {}, {}
    title = url.split("/")[3].replace("-", " ").upper()
    for wallet_item in wallet:
        url_website = str(url) + wallet_item
        cache_file = "cache/" + md5(url_website.encode("utf-8")).hexdigest() + ".cache"
        html_content = read_file(cache_file)
        if html_content is None:
            html_content = str(get_website_content(url_website))
            write_file(cache_file, html_content)

        p_vp[wallet_item] = get_text_from_xpath(html_content, xpath_pvp)
        dy[wallet_item] = get_text_from_xpath(html_content, xpath_dy)
        price[wallet_item] = get_text_from_xpath(html_content, xpath_price)
        dy_value = (float(dy[wallet_item]) / 100) * float(price[wallet_item])
        dy_expected = settings.MIN_DY_EXPECTED / 100
        max_price[wallet_item] = round((dy_value / dy_expected), 2)

    cheap_stocks = sorted(p_vp, key=p_vp.get)
    table = [tuple((title, "P/VP", "DY", "PRICE", "MAX_PRICE"))]
    for wallet_item in cheap_stocks:
        table.append(
            tuple(
                (
                    wallet_item.upper(),
                    p_vp[wallet_item],
                    dy[wallet_item] + "%",
                    "R$ " + price[wallet_item],
                    "R$ " + str(max_price[wallet_item]),
                )
            )
        )
    return table


def print_table(
    url: str, wallet: list, xpath_pvp: str, xpath_dy: str, xpath_price: str
) -> None:
    table = AsciiTable(
        get_cheap_wallet_table(url, wallet, xpath_pvp, xpath_dy, xpath_price)
    )
    print(table.table)


if __name__ == "__main__":
    wallets = [
        [
            settings.URL_STOCKS,
            settings.STOCKS,
            settings.XPATH_STOCKS_PVP,
            settings.XPATH_STOCKS_DY,
            settings.XPATH_STOCKS_PRICE,
        ],
        [
            settings.URL_FIIS,
            settings.FIIS,
            settings.XPATH_FIIS_PVP,
            settings.XPATH_FIIS_DY,
            settings.XPATH_FIIS_PRICE,
        ],
    ]
    print("Cheap wallet:")
    for w in wallets:
        url, wallet, xpath_pvp, xpath_dy, xpath_price = w
        print_table(url, wallet, xpath_pvp, xpath_dy, xpath_price)
