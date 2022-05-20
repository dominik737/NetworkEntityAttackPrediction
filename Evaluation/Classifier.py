import datetime
import math

from typing import List

from Database.Models.EntityModel import EntityModel
from Database.Models.SecurityEventModel import SecurityEventModel


def calculate_entity_fmp(entity: EntityModel, args) -> float:
    short_term_window_hours = args.short_window
    long_term_window_hours = args.long_window

    short_term_fmp = calculate_short_term_fmp(entity, short_term_window_hours)
    long_term_fmp = calculate_long_term_fmp(entity, long_term_window_hours)

    return (short_term_fmp * 2 + long_term_fmp) / 3


def calculate_short_term_fmp(entity: EntityModel, window: int) -> float:
    short_term_security_events = get_security_events_for_window(window, entity.security_events)
    if len(short_term_security_events) > 0:
        ewma_attack_probability = calculate_events_ewma(window, short_term_security_events)
        same_type_count = get_same_type_count(entity.security_events[-1].type, short_term_security_events)
        avg_severity = get_average_severity(short_term_security_events)

        if ewma_attack_probability > 0.4:
            if avg_severity > 0.6:
                if ewma_attack_probability > 0.7:
                    fmp_score = 1
                else:
                    fmp_score = 0.9
            else:
                if same_type_count > 5:
                    if ewma_attack_probability > 0.7:
                        fmp_score = 0.8
                    else:
                        fmp_score = 0.7
                else:
                    if avg_severity > 0.4:
                        fmp_score = 0.6
                    else:
                        fmp_score = 0.5
        else:
            if avg_severity > 0.5:
                if avg_severity > 0.8:
                    fmp_score = 0.5
                else:
                    fmp_score = 0.4
            else:
                if same_type_count > 11:
                    fmp_score = 0.3
                else:
                    if ewma_attack_probability > 0.2:
                        fmp_score = 0.2
                    else:
                        fmp_score = 0.1
    else:
        fmp_score = 0

    return fmp_score


def calculate_events_ewma(window: int, events: List[SecurityEventModel]) -> float:
    return calculate_ewma(window, select_detection_date_times_from_events(events))


def select_detection_date_times_from_events(events: List[SecurityEventModel]) -> List[datetime.datetime]:
    return list(map(lambda x: x.detection_date_time, events))


def calculate_ewma(window: int, dates: List[datetime.datetime]) -> float:
    dates_without_minutes = list(map(lambda d: get_date_time_without_minutes(d), dates))
    alpha = 2/(window + 1)  # determine alpha
    dividend = 0.0
    divisor = 0.0
    for x in range(window):  # sample each hour and determine whether there was an event
        hour = get_date_time_without_minutes(datetime.datetime.now() - datetime.timedelta(hours=x))
        event_occurred = any(date_without_minutes == hour for date_without_minutes in dates_without_minutes)
        weight = pow((1-alpha), x)
        dividend += weight * (1 if event_occurred else 0)
        divisor += weight
    return dividend / divisor if divisor > 0 else 0


def get_date_time_without_minutes(date_time: datetime.datetime) -> datetime.datetime:
    return date_time.replace(minute=0, second=0, microsecond=0)


def calculate_long_term_fmp(entity: EntityModel, window: int) -> float:
    long_term_security_events = get_security_events_for_window(window, entity.security_events)
    event_count = len(long_term_security_events)

    if event_count > 0:
        avg_severity = get_average_severity(long_term_security_events)
        same_type_count = get_same_type_count(entity.security_events[-1].type, long_term_security_events)
        event_count_log = math.log(event_count, 2)
        timedelta_from_last_event = get_timedelta_from_last_event(long_term_security_events)
        maximum_severity = get_maximum_severity(long_term_security_events)

        if maximum_severity > 0.7:
            if avg_severity > 0.5:
                if same_type_count > 2:
                    if event_count_log > 4:
                        fmp_score = 1
                    else:
                        fmp_score = 0.9
                else:
                    if timedelta_from_last_event < datetime.timedelta(hours=1):
                        fmp_score = 0.8
                    else:
                        fmp_score = 0.7
            else:
                if same_type_count > 3:
                    fmp_score = 0.6
                else:
                    fmp_score = 0.5
        else:
            if maximum_severity > 0.5:
                if avg_severity > 0.4:
                    fmp_score = 0.6
                else:
                    fmp_score = 0.5
            else:
                if event_count_log > 5:
                    if timedelta_from_last_event < datetime.timedelta(minutes=30):
                        fmp_score = 0.4
                    else:
                        fmp_score = 0.3
                else:
                    if avg_severity > 0.3:
                        fmp_score = 0.2
                    else:
                        fmp_score = 0.1
    else:
        fmp_score = 0

    return fmp_score


def get_security_events_for_window(window: int, security_events: List[SecurityEventModel]) -> List[SecurityEventModel]:
    if security_events is None or len(security_events) == 0:
        return []
    else:
        last_window_date_time = datetime.datetime.now() - datetime.timedelta(hours=window)
        events_in_window_iterator = filter(lambda x: x.detection_date_time > last_window_date_time, security_events)
        return list(events_in_window_iterator)


def get_average_severity(security_events: List[SecurityEventModel]) -> float:
    return sum(select_severity(security_events)) / len(security_events)


def get_severity(security_event: SecurityEventModel) -> float:
    return security_event.weight * security_event.volume


def get_same_type_count(event_type: int, security_events: List[SecurityEventModel]) -> int:
    return len(get_same_type_events(event_type, security_events))


def get_same_type_events(event_type: int, security_events: List[SecurityEventModel]) -> List[SecurityEventModel]:
    return list(filter(lambda x: x.type == event_type, security_events))


def get_timedelta_from_last_event(security_events: List[SecurityEventModel]) -> datetime.timedelta:
    detection_times = select_detection_date_times_from_events(security_events)
    return datetime.datetime.now() - max(detection_times)


def get_maximum_severity(security_events: List[SecurityEventModel]) -> float:
    severities = select_severity(security_events)
    return max(severities)


def select_severity(security_events: List[SecurityEventModel]) -> List[float]:
    return list(map(lambda x: get_severity(x), security_events))
