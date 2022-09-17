import functions
from typing import Union, Dict, Any, Generator

CMD_TO_FUNCTIONS = {
    'filter': functions.filter_query,
    'map': functions.map_query,
    'unique': functions.unique_query,
    'sort': functions.sort_query,
    'limit': functions.limit_query,
    'regex': functions.regex_filter,
}

FILEE_NAME = 'data/apache_logs.txt'


def builder_query(cmd: str, param: str, data: list) -> list:
    if data is None:
        with open(FILEE_NAME) as file:
            prepared_data = list(map(lambda x: x.strip(), file))

    else:
        prepared_data = data
    return CMD_TO_FUNCTIONS[cmd](param=param, data=prepared_data)
