import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup, Comment


class Parser(ABC):
    def __init__(self, src: str):
        self._src: str = src
        self._buffer: str = ""

    @property
    def source(self):
        return self._src

    @property
    def buffer(self):
        return self._buffer

    @property
    @abstractmethod
    def content(self) -> str:
        pass


class TextParser(Parser):
    @property
    def content(self) -> str:
        return self._src


class WebsiteParser(Parser):
    def __init__(self, src: str):
        super().__init__(src)
        self._status_code: int

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def content(self) -> str | None:
        if self._buffer is not None and self._status_code == 200:
            return self._buffer
        status_code: int = self.__parse()
        if status_code != 200:
            raise Exception(f"Request error: status_code = {status_code}")
        return self._buffer

    def __parse(self) -> int:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) '
                          'Gecko/20100101 Firefox/24.0'
        }
        response = requests.get(self._src, headers=headers)
        self._status_code = response.status_code
        self._buffer = self.__text_from_html(response.text)
        return self._status_code

    @staticmethod
    def __filter_visible(element) -> bool:
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def __text_from_html(self, html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        texts = soup.find_all(text=True)
        visible_texts = filter(self.__filter_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)
