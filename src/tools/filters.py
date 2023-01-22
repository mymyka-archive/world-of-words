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
    def filter(self, string: str) -> str:
        return string


class UppercaseStringFilter(StringFilter):
    def __init__(self, f: StringFilter):
        self.__filter = f

    def filter(self, string: str) -> str:
        string = self.__filter.filter(string)
        string = string.lower()
        return string


class RegExStringFilter(RegExFilter, StringFilter):
    __REGEX_PATTERN = ""

    def filter(self, string: str) -> str:
        return string

    @property
    def regex(self) -> str:
        return self.__REGEX_PATTERN


class NumberRegExStringFilter(RegExStringFilter):
    __REGEX_PATTERN = "[0-9]"

    def __init__(self, f: RegExFilter):
        self.__filter = f

    def filter(self, string: str) -> str:
        regex = f'{self.__filter.regex}|{self.__REGEX_PATTERN}'
        string = re.sub(regex, '', string)
        return string

    @property
    def regex(self) -> str:
        return f'{self.__filter.regex}|{self.__REGEX_PATTERN}'


class SpecialCharsRegExStringFilter(RegExStringFilter):
    __REGEX_PATTERN = "[^a-zA-Z0-9\s]"

    def __init__(self, f: RegExFilter):
        self.__filter = f

    def filter(self, string: str) -> str:
        regex = f'{self.__filter.regex}|{self.__REGEX_PATTERN}'
        string = re.sub(regex, '', string)
        return string

    @property
    def regex(self) -> str:
        return f'{self.__filter.regex}|{self.__REGEX_PATTERN}'
