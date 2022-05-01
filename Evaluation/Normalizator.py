from SecurityEventSubType import SecurityEventSubType
from SecurityEventType import SecurityEventType
from Configuration.Helpers import MaxParameterReader
from Communication.Helpers import DetailParameterRetriever
from Exceptions.UnsharableTypeException import UnsharableTypeException
import sys


def get_security_event_type(type_str: str) -> int:
    return SecurityEventType[type_str].value


def get_security_event_sub_type(sub_type_str: str) -> int:
    if sub_type_str is not None:
        try:
            return SecurityEventSubType[sub_type_str].value
        except KeyError:
            return SecurityEventSubType["_" + sub_type_str].value


def get_security_event_volume(detail: str, event_type: int, sub_type: int) -> float:
    (info_key, max_volume) = get_info_key_and_max_volume(event_type, sub_type)
    if max_volume == 0:
        raise UnsharableTypeException("Subtype " + SecurityEventSubType(sub_type).name + " of type " + SecurityEventType(event_type).name + "is not sharable")
    volume_str = get_detail_info(detail, info_key)
    try:
        volume = DetailParameterRetriever.retrieve(volume_str)
    except ValueError as e:
        volume = 0
        sys.stderr.write(f"Parsing of event volume failed. Event volume set to 0.Event type: {event_type}, event sub type: {sub_type}, detail: {detail}. Exception: {e} \n")
        f = open("wrongpasing.txt", "a")
        f.write(f"Parsing of event volume failed. Event volume set to 0.Event type: {event_type}, event sub type: {sub_type}, detail: {detail}. Exception: {e}")  # TODO: Smazat !
        f.close()
    return get_volume(volume, max_volume)


def get_info_key_and_max_volume(event_type: int, sub_type: int) -> (str, float):
    (event_type_string, sub_type_string) = get_type_and_sub_type_strings(event_type, sub_type)
    return MaxParameterReader.get_info_key_and_max_volume(event_type_string, sub_type_string)


def get_type_and_sub_type_strings(event_type: int, sub_type: int) -> (str, str):
    return SecurityEventType(event_type).name, get_sub_type_string(sub_type)


def get_sub_type_string(sub_type: int) -> str:
    enum_str = SecurityEventSubType(sub_type).name
    if enum_str[0] == "_":
        enum_str = enum_str[1::]
    return enum_str


def get_detail_info(detail: str, info_key: str) -> str:
    i = detail.find(info_key) + len(info_key)
    info = ""
    while i < len(detail):
        char = detail[i]
        if char == "," or (char == "." and i == len(detail) - 1):
            break
        if char == " " or char == ":":
            i += 1
            continue
        info += char
        i += 1
    return info


def get_volume(volume: float, max_volume: float) -> float:
    if volume > max_volume:
        return 1
    else:
        return volume / max_volume


def get_security_event_weight(event_type: int, sub_type: int) -> float:
    (event_type_string, sub_type_string) = get_type_and_sub_type_strings(event_type, sub_type)
    return MaxParameterReader.get_weight(event_type_string, sub_type_string)
