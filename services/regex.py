import re


def match(string, pattern):
    regex_obj = re.compile(pattern)
    return regex_obj.search(string)
