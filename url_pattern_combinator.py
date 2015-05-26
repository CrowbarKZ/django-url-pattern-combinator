import itertools
import re

def extract_template(pattern):
    """Extracts a 'template' of a url pattern given a pattern
    returns a string

    Example:

    input: '^home/city
      (-(?P<city_name>bristol|bath|cardiff|swindon|oxford|reading))?$'

    output: 'home/city(-{})?'
    """

    pattern = pattern.strip('$^')
    pattern = re.sub(r'\(\?P.+?\)', '{}', pattern)

    return pattern


def extract_options(pattern):
    """Extracts 'options' of a url pattern given a pattern
    returns list of lists

    Example:

    input: '^home/city
      (-(?P<city_name>bristol|bath|cardiff|swindon|oxford|reading))?$'

    output: [[bristol, bath, cardiff, swindon, oxford, reading]]
    """
    result = [
        match.group(1).split('|')
        for match
        in re.finditer(r'\(\?P<.+?>(.+?)\)', pattern)
    ]

    return result


def make_combinations(pattern):
    """Builds a list of possible urls for a given url pattern
    returns a list of strings

    Example:

    input: '^home/city
      (-(?P<city_name>bristol|bath|cardiff|swindon|oxford|reading))?$'

    output: ['home/city(-bristol)?',
            'home/city(-bath)?',
            'home/city(-cardiff)?',
            'home/city(-bristol)?',
            ...
    """

    template = extract_template(pattern)
    options = extract_options(pattern)
    options_ordered = itertools.product(*options)

    result = [
        template.format(*option_group)
        for option_group
        in options_ordered
    ]

    return result


def handle_optionals(url_list):
    """Builds a set of urls given a list of 'pseudo-urls' with optional parts
    returns a set of strings

    WARNING: Currently correctly handles only 1 optional part per url

    Example:

    input: ['home/city(-bristol)?',
            'home/city(-bath)?',
            'home/city(-cardiff)?',
            'home/city(-bristol)?',
            ...

    output: ('home/city-bristol',
             'home/city'
             ...
    """
    result = set()

    for url in url_list:
        absent = re.sub(r'\((-.+?)\)\?', '', url)
        present = re.sub(r'\((-.+?)\)\?', r'\1', url)

        result.add(present)
        result.add(absent)

    return result


def process(pattern):
    return handle_optionals(make_combinations(pattern))


if __name__ == '__main__':
    print process(
        r'^prefix'
        '/(?P<p1>office|school|carpet|window)'
        '-(?P<p2>cleaning|cleans|cleaner|cleaners)'
        '(-(?P<p3>uk|usa|france))?$'
    )
