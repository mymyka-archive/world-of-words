from abc import ABC, abstractmethod
import re


class Filter(ABC):
    @abstractmethod
    def filter(self, obj: object) -> object:
        pass


class RegExFilter(Filter):
    @abstractmethod
    def filter(self, obj: object) -> object:
        pass

    @property
    @abstractmethod
    def regex(self) -> str:
        pass


class StringFilter(Filter):
    def filter(self, s: str) -> str:
        return s


class UppercaseStringFilter(StringFilter):
    def __init__(self, f: StringFilter):
        self.__filter = f

    def filter(self, s: str) -> str:
        s = self.__filter.filter(s)
        s = s.lower()
        return s


class RegExStringFilter(RegExFilter, StringFilter):
    __PATTERN = ""

    def filter(self, s: str) -> str:
        return s

    @property
    def regex(self) -> str:
        return self.__PATTERN


class NumberRegExStringFilter(RegExStringFilter):
    __PATTERN = "0-9"

    def __init__(self, f: RegExFilter):
        self.__filter = f

    def filter(self, s: str) -> str:
        regex = f'[^{self.regex}]'
        print(regex)
        s = re.sub(regex, '', s)
        return s

    @property
    def regex(self) -> str:
        return f'{self.__filter.regex}{self.__PATTERN}'


class SpecialCharsRegExStringFilter(RegExStringFilter):
    __PATTERN = "@#$%"

    def __init__(self, f: RegExFilter):
        self.__filter = f

    def filter(self, s: str) -> str:
        regex = f'[^{self.regex}]'
        s = re.sub(regex, '', s)
        return s

    @property
    def regex(self) -> str:
        return f'{self.__filter.regex}{self.__PATTERN}'
