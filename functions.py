import re
from typing import Generator, Any


def filter_query(param: str, data: Generator) -> list:
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data: Generator) -> list:
    col_number = int(param)
    return list(map(lambda x: x.split(' ')[col_number], data))


def unique_query(data: list, *args: Any, **kwargs: Any) -> list:
    return list(set(data))


def sort_query(param: str, data: Generator) -> list:
    reverse = False if param == "asc" else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: Generator) -> list:
    limit = int(param)
    return list(data)[:limit]


def regex_filter(param: str, data: Generator) -> list:
    regex = re.compile(param)
    s = [x for x in data if regex.findall(x)]
    return s

