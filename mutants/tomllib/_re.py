# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2021 Taneli Hukkinen
# Licensed to PSF under a Contributor Agreement.

from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone, tzinfo
from functools import lru_cache
import re

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any, Final

    from ._types import ParseFloat

_TIME_RE_STR: Final = r"""
([01][0-9]|2[0-3])             # hours
:([0-5][0-9])                  # minutes
(?:
    :([0-5][0-9])              # optional seconds
    (?:\.([0-9]{1,6})[0-9]*)?  # optional fractions of a second
)?
"""

RE_NUMBER: Final = re.compile(
    r"""
0
(?:
    x[0-9A-Fa-f](?:_?[0-9A-Fa-f])*   # hex
    |
    b[01](?:_?[01])*                 # bin
    |
    o[0-7](?:_?[0-7])*               # oct
)
|
[+-]?(?:0|[1-9](?:_?[0-9])*)         # dec, integer part
(?P<floatpart>
    (?:\.[0-9](?:_?[0-9])*)?         # optional fractional part
    (?:[eE][+-]?[0-9](?:_?[0-9])*)?  # optional exponent part
)
""",
    flags=re.VERBOSE,
)
RE_LOCALTIME: Final = re.compile(_TIME_RE_STR, flags=re.VERBOSE)
RE_DATETIME: Final = re.compile(
    rf"""
([0-9]{{4}})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])  # date, e.g. 1988-10-27
(?:
    [Tt ]
    {_TIME_RE_STR}
    (?:([Zz])|([+-])([01][0-9]|2[0-3]):([0-5][0-9]))?  # optional time offset
)?
""",
    flags=re.VERBOSE,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_match_to_datetime__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_match_to_datetime__mutmut)
def match_to_datetime(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_orig(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_1(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = None
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_2(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = None
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_3(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(None), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_4(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(None), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_5(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(None)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_6(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is not None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_7(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(None, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_8(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, None, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_9(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, None)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_10(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_11(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_12(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, )
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_13(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = None
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_14(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(None), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_15(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(None)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_16(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = None
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_17(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if (sec_str) and False else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_18(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if (sec_str) or True else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_19(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(None) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_20(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 1
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_21(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = None
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_22(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if (micros_str) and False else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_23(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if (micros_str) or True else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_24(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(None) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_25(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(None, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_26(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, None)) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_27(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust("0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_28(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, )) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_29(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.rjust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_30(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(7, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_31(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "XX0XX")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_32(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 1
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_33(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = None
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_34(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            None, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_35(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, None, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_36(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, None
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_37(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_38(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_39(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_40(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = None
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_41(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = ""
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_42(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(None, month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_43(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, None, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_44(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, None, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_45(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, None, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_46(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, None, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_47(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, None, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_48(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, None, tzinfo=tz)


def x_match_to_datetime__mutmut_49(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, tzinfo=None)


def x_match_to_datetime__mutmut_50(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(month, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_51(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, day, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_52(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, hour, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_53(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, minute, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_54(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, sec, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_55(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, micros, tzinfo=tz)


def x_match_to_datetime__mutmut_56(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, tzinfo=tz)


def x_match_to_datetime__mutmut_57(match: re.Match[str]) -> datetime | date:
    """Convert a `RE_DATETIME` match to `datetime.datetime` or `datetime.date`.

    Raises ValueError if the match does not correspond to a valid date
    or datetime.
    """
    (
        year_str,
        month_str,
        day_str,
        hour_str,
        minute_str,
        sec_str,
        micros_str,
        zulu_time,
        offset_sign_str,
        offset_hour_str,
        offset_minute_str,
    ) = match.groups()
    year, month, day = int(year_str), int(month_str), int(day_str)
    if hour_str is None:
        return date(year, month, day)
    hour, minute = int(hour_str), int(minute_str)
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    if offset_sign_str:
        tz: tzinfo | None = cached_tz(
            offset_hour_str, offset_minute_str, offset_sign_str
        )
    elif zulu_time:
        tz = timezone.utc
    else:  # local date-time
        tz = None
    return datetime(year, month, day, hour, minute, sec, micros, )

mutants_x_match_to_datetime__mutmut['_mutmut_orig'] = x_match_to_datetime__mutmut_orig # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_1'] = x_match_to_datetime__mutmut_1 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_2'] = x_match_to_datetime__mutmut_2 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_3'] = x_match_to_datetime__mutmut_3 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_4'] = x_match_to_datetime__mutmut_4 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_5'] = x_match_to_datetime__mutmut_5 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_6'] = x_match_to_datetime__mutmut_6 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_7'] = x_match_to_datetime__mutmut_7 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_8'] = x_match_to_datetime__mutmut_8 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_9'] = x_match_to_datetime__mutmut_9 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_10'] = x_match_to_datetime__mutmut_10 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_11'] = x_match_to_datetime__mutmut_11 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_12'] = x_match_to_datetime__mutmut_12 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_13'] = x_match_to_datetime__mutmut_13 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_14'] = x_match_to_datetime__mutmut_14 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_15'] = x_match_to_datetime__mutmut_15 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_16'] = x_match_to_datetime__mutmut_16 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_17'] = x_match_to_datetime__mutmut_17 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_18'] = x_match_to_datetime__mutmut_18 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_19'] = x_match_to_datetime__mutmut_19 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_20'] = x_match_to_datetime__mutmut_20 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_21'] = x_match_to_datetime__mutmut_21 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_22'] = x_match_to_datetime__mutmut_22 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_23'] = x_match_to_datetime__mutmut_23 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_24'] = x_match_to_datetime__mutmut_24 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_25'] = x_match_to_datetime__mutmut_25 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_26'] = x_match_to_datetime__mutmut_26 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_27'] = x_match_to_datetime__mutmut_27 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_28'] = x_match_to_datetime__mutmut_28 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_29'] = x_match_to_datetime__mutmut_29 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_30'] = x_match_to_datetime__mutmut_30 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_31'] = x_match_to_datetime__mutmut_31 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_32'] = x_match_to_datetime__mutmut_32 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_33'] = x_match_to_datetime__mutmut_33 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_34'] = x_match_to_datetime__mutmut_34 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_35'] = x_match_to_datetime__mutmut_35 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_36'] = x_match_to_datetime__mutmut_36 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_37'] = x_match_to_datetime__mutmut_37 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_38'] = x_match_to_datetime__mutmut_38 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_39'] = x_match_to_datetime__mutmut_39 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_40'] = x_match_to_datetime__mutmut_40 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_41'] = x_match_to_datetime__mutmut_41 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_42'] = x_match_to_datetime__mutmut_42 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_43'] = x_match_to_datetime__mutmut_43 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_44'] = x_match_to_datetime__mutmut_44 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_45'] = x_match_to_datetime__mutmut_45 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_46'] = x_match_to_datetime__mutmut_46 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_47'] = x_match_to_datetime__mutmut_47 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_48'] = x_match_to_datetime__mutmut_48 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_49'] = x_match_to_datetime__mutmut_49 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_50'] = x_match_to_datetime__mutmut_50 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_51'] = x_match_to_datetime__mutmut_51 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_52'] = x_match_to_datetime__mutmut_52 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_53'] = x_match_to_datetime__mutmut_53 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_54'] = x_match_to_datetime__mutmut_54 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_55'] = x_match_to_datetime__mutmut_55 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_56'] = x_match_to_datetime__mutmut_56 # type: ignore # mutmut generated
mutants_x_match_to_datetime__mutmut['x_match_to_datetime__mutmut_57'] = x_match_to_datetime__mutmut_57 # type: ignore # mutmut generated


# No need to limit cache size. This is only ever called on input
# that matched RE_DATETIME, so there is an implicit bound of
# 24 (hours) * 60 (minutes) * 2 (offset direction) = 2880.
@lru_cache(maxsize=None)
def cached_tz(hour_str: str, minute_str: str, sign_str: str) -> timezone:
    sign = 1 if sign_str == "+" else -1
    return timezone(
        timedelta(
            hours=sign * int(hour_str),
            minutes=sign * int(minute_str),
        )
    )
mutants_x_match_to_localtime__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_match_to_localtime__mutmut)
def match_to_localtime(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_orig(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_1(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = None
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_2(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = None
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_3(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if (sec_str) and False else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_4(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if (sec_str) or True else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_5(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(None) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_6(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 1
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_7(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = None
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_8(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if (micros_str) and False else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_9(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if (micros_str) or True else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_10(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(None) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_11(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(None, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_12(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, None)) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_13(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust("0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_14(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, )) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_15(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.rjust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_16(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(7, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_17(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "XX0XX")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_18(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 1
    return time(int(hour_str), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_19(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(None, int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_20(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), None, sec, micros)


def x_match_to_localtime__mutmut_21(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), None, micros)


def x_match_to_localtime__mutmut_22(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, None)


def x_match_to_localtime__mutmut_23(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_24(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), sec, micros)


def x_match_to_localtime__mutmut_25(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), micros)


def x_match_to_localtime__mutmut_26(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(minute_str), sec, )


def x_match_to_localtime__mutmut_27(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(None), int(minute_str), sec, micros)


def x_match_to_localtime__mutmut_28(match: re.Match[str]) -> time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    sec = int(sec_str) if sec_str else 0
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return time(int(hour_str), int(None), sec, micros)

mutants_x_match_to_localtime__mutmut['_mutmut_orig'] = x_match_to_localtime__mutmut_orig # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_1'] = x_match_to_localtime__mutmut_1 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_2'] = x_match_to_localtime__mutmut_2 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_3'] = x_match_to_localtime__mutmut_3 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_4'] = x_match_to_localtime__mutmut_4 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_5'] = x_match_to_localtime__mutmut_5 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_6'] = x_match_to_localtime__mutmut_6 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_7'] = x_match_to_localtime__mutmut_7 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_8'] = x_match_to_localtime__mutmut_8 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_9'] = x_match_to_localtime__mutmut_9 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_10'] = x_match_to_localtime__mutmut_10 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_11'] = x_match_to_localtime__mutmut_11 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_12'] = x_match_to_localtime__mutmut_12 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_13'] = x_match_to_localtime__mutmut_13 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_14'] = x_match_to_localtime__mutmut_14 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_15'] = x_match_to_localtime__mutmut_15 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_16'] = x_match_to_localtime__mutmut_16 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_17'] = x_match_to_localtime__mutmut_17 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_18'] = x_match_to_localtime__mutmut_18 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_19'] = x_match_to_localtime__mutmut_19 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_20'] = x_match_to_localtime__mutmut_20 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_21'] = x_match_to_localtime__mutmut_21 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_22'] = x_match_to_localtime__mutmut_22 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_23'] = x_match_to_localtime__mutmut_23 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_24'] = x_match_to_localtime__mutmut_24 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_25'] = x_match_to_localtime__mutmut_25 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_26'] = x_match_to_localtime__mutmut_26 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_27'] = x_match_to_localtime__mutmut_27 # type: ignore # mutmut generated
mutants_x_match_to_localtime__mutmut['x_match_to_localtime__mutmut_28'] = x_match_to_localtime__mutmut_28 # type: ignore # mutmut generated
mutants_x_match_to_number__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_match_to_number__mutmut)
def match_to_number(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group("floatpart"):
        return parse_float(match.group())
    return int(match.group(), 0)


def x_match_to_number__mutmut_orig(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group("floatpart"):
        return parse_float(match.group())
    return int(match.group(), 0)


def x_match_to_number__mutmut_1(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group(None):
        return parse_float(match.group())
    return int(match.group(), 0)


def x_match_to_number__mutmut_2(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group("XXfloatpartXX"):
        return parse_float(match.group())
    return int(match.group(), 0)


def x_match_to_number__mutmut_3(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group("FLOATPART"):
        return parse_float(match.group())
    return int(match.group(), 0)


def x_match_to_number__mutmut_4(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group("floatpart"):
        return parse_float(None)
    return int(match.group(), 0)


def x_match_to_number__mutmut_5(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group("floatpart"):
        return parse_float(match.group())
    return int(None, 0)


def x_match_to_number__mutmut_6(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group("floatpart"):
        return parse_float(match.group())
    return int(match.group(), None)


def x_match_to_number__mutmut_7(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group("floatpart"):
        return parse_float(match.group())
    return int(0)


def x_match_to_number__mutmut_8(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group("floatpart"):
        return parse_float(match.group())
    return int(match.group(), )


def x_match_to_number__mutmut_9(match: re.Match[str], parse_float: ParseFloat) -> Any:
    if match.group("floatpart"):
        return parse_float(match.group())
    return int(match.group(), 1)

mutants_x_match_to_number__mutmut['_mutmut_orig'] = x_match_to_number__mutmut_orig # type: ignore # mutmut generated
mutants_x_match_to_number__mutmut['x_match_to_number__mutmut_1'] = x_match_to_number__mutmut_1 # type: ignore # mutmut generated
mutants_x_match_to_number__mutmut['x_match_to_number__mutmut_2'] = x_match_to_number__mutmut_2 # type: ignore # mutmut generated
mutants_x_match_to_number__mutmut['x_match_to_number__mutmut_3'] = x_match_to_number__mutmut_3 # type: ignore # mutmut generated
mutants_x_match_to_number__mutmut['x_match_to_number__mutmut_4'] = x_match_to_number__mutmut_4 # type: ignore # mutmut generated
mutants_x_match_to_number__mutmut['x_match_to_number__mutmut_5'] = x_match_to_number__mutmut_5 # type: ignore # mutmut generated
mutants_x_match_to_number__mutmut['x_match_to_number__mutmut_6'] = x_match_to_number__mutmut_6 # type: ignore # mutmut generated
mutants_x_match_to_number__mutmut['x_match_to_number__mutmut_7'] = x_match_to_number__mutmut_7 # type: ignore # mutmut generated
mutants_x_match_to_number__mutmut['x_match_to_number__mutmut_8'] = x_match_to_number__mutmut_8 # type: ignore # mutmut generated
mutants_x_match_to_number__mutmut['x_match_to_number__mutmut_9'] = x_match_to_number__mutmut_9 # type: ignore # mutmut generated
