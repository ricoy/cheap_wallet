import requests
from typing import Optional
from lxml import html


def read_file(filename: str) -> Optional[str]:
    try:
        with open(filename, "r") as file:
            return file.read()
    except IOError:
        return None


def write_file(filename: str, content: str) -> None:
    with open(filename, "w") as file:
        file.write(content)


def get_website_content(url: str) -> str:
    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError("invalid url")
    return response.text


def get_text_from_xpath(hml_content: str, xpath: str) -> str:
    xpath_result = html.fromstring(hml_content).xpath(xpath)
    if len(xpath_result) > 0:
        return str(xpath_result[0].text).replace(",", ".").replace("%", "")
    return ""
