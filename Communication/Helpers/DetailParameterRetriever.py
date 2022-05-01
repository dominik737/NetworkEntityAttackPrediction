from Exceptions.UnknownFormatException import UnknownFormatException

magnitudes = {"KiB": 10, "MiB": 20, "GiB": 30, "TiB": 40, "PiB": 50, "EiB": 60}


def retrieve(size: str) -> float:
    (success, num) = try_parse_float(size)
    if success:
        return num
    elif contains_magnitude(size):
        (number, magnitude) = get_number_and_magnitude(size)
        return number * get_magnitude_as_int(magnitude)
    else:
        raise UnknownFormatException("Unknown security event detail parameter format:" + size)


def contains_magnitude(s: str) -> bool:
    for magnitude_key in magnitudes.keys():
        if magnitude_key in s:
            return True
    return False


def get_number_and_magnitude(size: str) -> (float, str):
    for magnitude_key in magnitudes.keys():
        if magnitude_key in size:
            return float(size.replace(magnitude_key, "")), magnitude_key


def get_magnitude_as_int(magnitude: str) -> int:
    if magnitude in magnitudes.keys():
        return pow(2, magnitudes[magnitude])
    else:
        raise Exception("Don't know unit of size: " + magnitude)


def try_parse_float(s: str) -> (bool, float):
    try:
        return True, float(s)
    except ValueError:
        return False, None
