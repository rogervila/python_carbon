# Carbon

<p align="center"><img src="https://i.ibb.co/QHSzYBs/python-carbon.png" alt="rogervila/python_carbon" /></p>

[![PyPI version](https://badge.fury.io/py/python-carbon.svg)](https://badge.fury.io/py/python-carbon)
![PyPI - Downloads](https://img.shields.io/pypi/dm/python-carbon)

PHP [Carbon](https://carbon.nesbot.com/docs/) library adapted for Python.

A fluent, immutable-style wrapper around Python's `datetime` that provides a rich, expressive API for creating, comparing, manipulating, and formatting dates and times.

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Class Constants](#class-constants)
- [Instantiation](#instantiation)
  - [Constructor](#constructor)
  - [Carbon.parse()](#carbonparsedate_string)
  - [Carbon.now()](#carbonnow)
  - [Carbon.utcnow()](#carbonutcnow)
  - [Carbon.yesterday()](#carbonyesterday)
  - [Carbon.utcyesterday()](#carbonutcyesterday)
  - [Carbon.tomorrow()](#carbontomorrow)
  - [Carbon.utctomorrow()](#carbonutctomorrow)
  - [Carbon.createFromFormat()](#carboncreatefromformatformat_string-date_string)
  - [Carbon.createFromTimestamp()](#carboncreatefromtimestamptimestamp)
- [Properties](#properties)
  - [timestamp](#timestamp)
  - [micro](#micro)
- [Getters](#getters)
  - [getYear()](#getyear)
  - [getMonth()](#getmonth)
  - [getDay()](#getday)
  - [getHour()](#gethour)
  - [getMinute()](#getminute)
  - [getSecond()](#getsecond)
  - [getMicro()](#getmicro)
  - [getTimestamp()](#gettimestamp)
  - [getDayOfWeek()](#getdayofweek)
  - [getDayOfYear()](#getdayofyear)
  - [getWeekOfMonth()](#getweekofmonthstart0)
  - [getWeekOfYear()](#getweekofyear)
  - [getQuarter()](#getquarterstart1)
  - [getQuarters()](#getquartersstart1)
  - [getDaysInMonth()](#getdaysinmonth)
  - [getMonthFirstWeekDay()](#getmonthfirstweekday)
- [Setters](#setters)
  - [setYear()](#setyearyear)
  - [setMonth()](#setmonthmonth)
  - [setDay()](#setdayday)
  - [setHour()](#sethourhour)
  - [setMinute()](#setminuteminute)
  - [setSecond()](#setsecondsecond)
  - [setMicroSecond()](#setmicrosecondmicrosecond)
- [Formatting](#formatting)
  - [format()](#formatformat_string)
  - [toDateTimeString()](#todatetimestringwith_millisecondsfalse)
  - [toDateString()](#todatestring)
  - [toTimeString()](#totimestring)
  - [toDatetime()](#todatetime)
  - [toCookieString()](#tocookiestring)
  - [toISOString()](#toisostring)
- [Comparison](#comparison)
  - [equalTo()](#equaltocarbon)
  - [notEqualTo()](#notequaltocarbon)
  - [greaterThan()](#greaterthancarbon)
  - [greaterThanOrEqualTo()](#greaterthanorequaltocarbon)
  - [lessThan()](#lessthancarbon)
  - [lessThanOrEqualTo()](#lessthanorequaltocarbon)
  - [between()](#betweenlow-high-includedtrue)
  - [betweenIncluded()](#betweenincludedlow-high)
  - [betweenExcluded()](#betweenexcludedlow-high)
  - [isSameMinute()](#issameminutecarbon-match_datetrue)
  - [isSameHour()](#issamehourcarbon-match_datetrue)
  - [isSameDay()](#issamedaycarbon-match_datetrue)
  - [isSameWeek()](#issameweekcarbon)
  - [isSameMonth()](#issamemonthcarbon-match_datetrue)
  - [isSameYear()](#issameyearcarbon)
  - [isSameQuarter()](#issamequartercarbon-match_datetrue)
- [Checks](#checks)
  - [isNextYear()](#isnextyear)
  - [isLastYear()](#islastyear)
  - [isNextMonth()](#isnextmonth)
  - [isLastMonth()](#islastmonth)
  - [isStartOfDay()](#isstartofday)
  - [isEndOfDay()](#isendofday)
  - [isFuture()](#isfuture)
  - [isPast()](#ispast)
  - [isMonday()](#ismonday)
  - [isTuesday()](#istuesday)
  - [isWednesday()](#iswednesday)
  - [isThursday()](#isthursday)
  - [isFriday()](#isfriday)
  - [isSaturday()](#issaturday)
  - [isSunday()](#issunday)
  - [isLeapYear()](#isleapyear)
  - [isWeekend()](#isweekend)
  - [isDayOfWeek()](#isdayofweekweekday)
  - [isLastDayOfMonth()](#islastdayofmonth)
  - [isFirstDayOfMonth()](#isfirstdayofmonth)
- [Addition and Subtraction](#addition-and-subtraction)
  - [add()](#addamount-unit)
  - [addMicroSeconds()](#addmicrosecondsmicroseconds1)
  - [addSeconds()](#addsecondsseconds1)
  - [addMinutes()](#addminutesminutes1)
  - [addHours()](#addhourshours1)
  - [addDays()](#adddaysdays1)
  - [addWeeks()](#addweeksweeks1)
  - [addMonths()](#addmonthsmonths1)
  - [addYears()](#addyearsyears1)
  - [sub()](#subamount-unit)
  - [subMicroSeconds()](#submicrosecondsmicroseconds1)
  - [subSeconds()](#subsecondsseconds1)
  - [subMinutes()](#subminutesminutes1)
  - [subHours()](#subhourshours1)
  - [subDays()](#subdaysdays1)
  - [subWeeks()](#subweeksweeks1)
  - [subMonths()](#submonthsmonths1)
  - [subYears()](#subyearsyears1)
- [Difference](#difference)
  - [difference()](#differencecarbon)
  - [diffIn()](#diffinunit-carbon)
  - [diffInMicroseconds()](#diffinmicrosecondscarbon)
  - [diffInSeconds()](#diffinsecondscarbon)
  - [diffInMinutes()](#diffinminutescarbon)
  - [diffInHours()](#diffinhourscarbon)
  - [diffInDays()](#diffindayscarbon)
  - [diffInWeeks()](#diffinweekscarbon)
  - [diffInMonths()](#diffinmonthscarbon)
  - [diffInYears()](#diffinyearscarbon)
- [Converters](#converters)
  - [utc()](#utc)
- [Modifiers](#modifiers)
  - [startOf() / endOf()](#startofunit--endofunit)
  - [startOfSecond() / endOfSecond()](#startofsecond--endofsecond)
  - [startOfMinute() / endOfMinute()](#startofminute--endofminute)
  - [startOfHour() / endOfHour()](#startofhour--endofhour)
  - [startOfDay() / endOfDay()](#startofday--endofday)
  - [startOfWeek() / endOfWeek()](#startofweek--endofweek)
  - [startOfMonth() / endOfMonth()](#startofmonth--endofmonth)
  - [startOfYear() / endOfYear()](#startofyear--endofyear)
- [Next Weekday](#next-weekday)
  - [next()](#nextweekdaynone)
  - [nextMonday() … nextSunday()](#nextmonday--nextsunday)
- [datetime and timedelta Proxies](#datetime-and-timedelta-proxies)
- [Proxy Attributes and Methods](#proxy-attributes-and-methods)
- [License](#license)

---

## Installation

```bash
pip install python-carbon
```

## Requirements

- Python 3.9+
- [`python-dateutil`](https://pypi.org/project/python-dateutil/) >= 2

## Quick Start

```python
from python_carbon import Carbon

# Current date and time
now = Carbon.now()
print(now.toDateTimeString())  # e.g. '2026-03-04 14:30:00'

# Parse a date string
dt = Carbon.parse('2025-12-25 10:00:00')
print(dt.toDateString())  # '2025-12-25'

# Fluent manipulation (each call returns a new Carbon instance)
future = Carbon.now().addDays(30).addHours(2).setMinute(0)
print(future.toDateTimeString())

# Comparison
yesterday = Carbon.yesterday()
tomorrow = Carbon.tomorrow()
print(now.between(yesterday, tomorrow))  # True

# Difference
earlier = Carbon.parse('2025-01-01')
later = Carbon.parse('2025-06-15')
print(later.diffInDays(earlier))  # ≈ 165.0
```

> **Note:** Every mutating method returns a **new** `Carbon` instance — the original is never modified.

---

## Class Constants

Day-of-week constants follow Python's `datetime.weekday()` convention (Monday = 0):

| Constant           | Value |
|--------------------|-------|
| `Carbon.MONDAY`    | `0`   |
| `Carbon.TUESDAY`   | `1`   |
| `Carbon.WEDNESDAY` | `2`   |
| `Carbon.THURSDAY`  | `3`   |
| `Carbon.FRIDAY`    | `4`   |
| `Carbon.SATURDAY`  | `5`   |
| `Carbon.SUNDAY`    | `6`   |

---

## Instantiation

### Constructor

```python
Carbon(now: Union[Carbon, datetime, None] = None) -> Carbon
```

Creates a new `Carbon` instance.

| Argument | Type | Description |
|----------|------|-------------|
| `now` | `Carbon`, `datetime`, or `None` | The date to wrap. Defaults to the current date/time when `None`. |

```python
from datetime import datetime
from python_carbon import Carbon

# Current date/time (equivalent to Carbon.now())
c = Carbon()

# From a datetime object
c = Carbon(datetime(2025, 6, 15, 10, 30, 0))

# From another Carbon instance (copy)
c2 = Carbon(c)
```

Raises `ValueError` if an unsupported type is passed.

---

### `Carbon.parse(date_string)`

```python
@staticmethod
Carbon.parse(date_string: str) -> Carbon
```

Parses a human-readable date string into a `Carbon` instance. Internally uses [`dateutil.parser.parse`](https://dateutil.readthedocs.io/en/stable/parser.html), so it supports a wide variety of formats.

```python
Carbon.parse('2025-12-25')
Carbon.parse('December 25, 2025 3:30 PM')
Carbon.parse('2025-12-25T15:30:00+02:00')
```

---

### `Carbon.now()`

```python
@staticmethod
Carbon.now() -> Carbon
```

Returns a `Carbon` instance set to the current local date and time.

```python
now = Carbon.now()
print(now.toDateTimeString())  # e.g. '2026-03-04 14:52:35'
```

---

### `Carbon.utcnow()`

```python
@staticmethod
Carbon.utcnow() -> Carbon
```

Returns a `Carbon` instance set to the current UTC date and time (timezone-aware).

```python
utc = Carbon.utcnow()
print(utc.toDatetime().tzname())  # 'UTC'
```

---

### `Carbon.yesterday()`

```python
@staticmethod
Carbon.yesterday() -> Carbon
```

Returns a `Carbon` instance set to yesterday's local date and time (current time minus 1 day).

```python
y = Carbon.yesterday()
```

---

### `Carbon.utcyesterday()`

```python
@staticmethod
Carbon.utcyesterday() -> Carbon
```

Returns a `Carbon` instance set to yesterday's UTC date and time.

---

### `Carbon.tomorrow()`

```python
@staticmethod
Carbon.tomorrow() -> Carbon
```

Returns a `Carbon` instance set to tomorrow's local date and time (current time plus 1 day).

```python
t = Carbon.tomorrow()
```

---

### `Carbon.utctomorrow()`

```python
@staticmethod
Carbon.utctomorrow() -> Carbon
```

Returns a `Carbon` instance set to tomorrow's UTC date and time.

---

### `Carbon.createFromFormat(format_string, date_string)`

```python
@staticmethod
Carbon.createFromFormat(format_string: str, date_string: str) -> Carbon
```

Creates a `Carbon` instance from a date string matching the given format. Uses Python's [`strptime` format codes](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior).

| Argument | Type | Description |
|----------|------|-------------|
| `format_string` | `str` | A `strptime`-compatible format string (e.g. `'%Y-%m-%d'`). |
| `date_string` | `str` | The date string to parse. |

```python
dt = Carbon.createFromFormat('%Y-%m-%d', '2025-08-18')
dt = Carbon.createFromFormat('%d/%m/%Y %H:%M', '18/08/2025 14:30')
```

---

### `Carbon.createFromTimestamp(timestamp)`

```python
@staticmethod
Carbon.createFromTimestamp(timestamp: int) -> Carbon
```

Creates a `Carbon` instance from a Unix timestamp (seconds since epoch).

| Argument | Type | Description |
|----------|------|-------------|
| `timestamp` | `int` | A Unix timestamp. |

```python
dt = Carbon.createFromTimestamp(1629244800)
print(dt.toDateString())  # '2021-08-18'
```

---

## Properties

### `timestamp`

```python
@property
timestamp -> float
```

Returns the Unix timestamp as a `float`. Shorthand for `getTimestamp()`.

```python
ts = Carbon.now().timestamp
```

---

### `micro`

```python
@property
micro -> int
```

Returns the microsecond component as an `int`. Shorthand for `getMicro()`.

```python
us = Carbon.now().micro
```

---

## Getters

### `getYear()`

```python
getYear() -> int
```

Returns the year component.

```python
Carbon.parse('2025-06-15').getYear()  # 2025
```

---

### `getMonth()`

```python
getMonth() -> int
```

Returns the month component (1–12).

```python
Carbon.parse('2025-06-15').getMonth()  # 6
```

---

### `getDay()`

```python
getDay() -> int
```

Returns the day-of-month component (1–31).

```python
Carbon.parse('2025-06-15').getDay()  # 15
```

---

### `getHour()`

```python
getHour() -> int
```

Returns the hour component (0–23).

```python
Carbon.parse('2025-06-15 14:30:00').getHour()  # 14
```

---

### `getMinute()`

```python
getMinute() -> int
```

Returns the minute component (0–59).

```python
Carbon.parse('2025-06-15 14:30:00').getMinute()  # 30
```

---

### `getSecond()`

```python
getSecond() -> int
```

Returns the second component (0–59).

```python
Carbon.parse('2025-06-15 14:30:45').getSecond()  # 45
```

---

### `getMicro()`

```python
getMicro() -> int
```

Returns the microsecond component (0–999999).

```python
Carbon.parse('2025-06-15 14:30:45.123456').getMicro()  # 123456
```

---

### `getTimestamp()`

```python
getTimestamp() -> float
```

Returns the Unix timestamp as a `float`.

```python
ts = Carbon.parse('2025-01-01 00:00:00').getTimestamp()
```

---

### `getDayOfWeek()`

```python
getDayOfWeek() -> int
```

Returns the day of the week as an integer (Monday = 0, Sunday = 6), using Python's `datetime.weekday()` convention.

```python
Carbon.parse('2021-08-18').getDayOfWeek()  # 2 (Wednesday)
```

---

### `getDayOfYear()`

```python
getDayOfYear() -> int
```

Returns the day of the year (1–366).

```python
Carbon.parse('2022-01-02').getDayOfYear()  # 2
```

---

### `getWeekOfMonth(start=0)`

```python
getWeekOfMonth(start: int = 0) -> int
```

Returns the week number within the current month.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `start` | `int` | `0` | Starting index for week numbering. |

```python
Carbon.parse('2025-03-15').getWeekOfMonth()    # 0-indexed week number
Carbon.parse('2025-03-15').getWeekOfMonth(1)   # 1-indexed week number
```

---

### `getWeekOfYear()`

```python
getWeekOfYear() -> int
```

Returns the week number within the year, using `strftime('%W')` (weeks start on Monday, first week starts at 0).

```python
Carbon.parse('2022-01-01').getWeekOfYear()  # 0
```

---

### `getQuarter(start=1)`

```python
getQuarter(start: int = 1) -> int
```

Returns the zero-indexed quarter of the year for the current month.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `start` | `int` | `1` | The month that starts the first quarter (e.g. `1` for Jan, `4` for fiscal years starting in April). |

```python
Carbon.parse('2025-03-15').getQuarter()   # 0 (Q1: Jan–Mar)
Carbon.parse('2025-05-15').getQuarter()   # 1 (Q2: Apr–Jun)
```

---

### `getQuarters(start=1)`

```python
getQuarters(start: int = 1) -> list
```

Returns a list of four lists, each containing three month numbers, representing the quarters of the year.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `start` | `int` | `1` | The month that starts the first quarter. |

```python
Carbon.now().getQuarters()
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

Carbon.now().getQuarters(4)
# [[4, 5, 6], [7, 8, 9], [10, 11, 12], [1, 2, 3]]
```

---

### `getDaysInMonth()`

```python
getDaysInMonth() -> int
```

Returns the number of days in the current month.

```python
Carbon.parse('2025-02-10').getDaysInMonth()  # 28
Carbon.parse('2024-02-10').getDaysInMonth()  # 29 (leap year)
```

---

### `getMonthFirstWeekDay()`

```python
getMonthFirstWeekDay() -> int
```

Returns the weekday of the first day of the current month (Monday = 0, Sunday = 6).

```python
Carbon.parse('2025-03-15').getMonthFirstWeekDay()  # weekday of March 1, 2025
```

---

## Setters

All setters return a **new** `Carbon` instance — the original is not modified.

### `setYear(year)`

```python
setYear(year: int) -> Carbon
```

Returns a new `Carbon` with the year replaced.

```python
Carbon.parse('2025-06-15').setYear(2030).toDateString()  # '2030-06-15'
```

---

### `setMonth(month)`

```python
setMonth(month: int) -> Carbon
```

Returns a new `Carbon` with the month replaced (1–12).

```python
Carbon.parse('2025-06-15').setMonth(1).toDateString()  # '2025-01-15'
```

---

### `setDay(day)`

```python
setDay(day: int) -> Carbon
```

Returns a new `Carbon` with the day replaced (1–31).

```python
Carbon.parse('2025-06-15').setDay(1).toDateString()  # '2025-06-01'
```

---

### `setHour(hour)`

```python
setHour(hour: int) -> Carbon
```

Returns a new `Carbon` with the hour replaced (0–23).

```python
Carbon.parse('2025-06-15 14:30:00').setHour(8).toTimeString()  # '08:30:00'
```

---

### `setMinute(minute)`

```python
setMinute(minute: int) -> Carbon
```

Returns a new `Carbon` with the minute replaced (0–59).

```python
Carbon.parse('2025-06-15 14:30:00').setMinute(0).toTimeString()  # '14:00:00'
```

---

### `setSecond(second)`

```python
setSecond(second: int) -> Carbon
```

Returns a new `Carbon` with the second replaced (0–59).

```python
Carbon.parse('2025-06-15 14:30:45').setSecond(0).toTimeString()  # '14:30:00'
```

---

### `setMicroSecond(microsecond)`

```python
setMicroSecond(microsecond: int) -> Carbon
```

Returns a new `Carbon` with the microsecond replaced (0–999999).

```python
Carbon.parse('2025-06-15 14:30:45.123456').setMicroSecond(0).getMicro()  # 0
```

---

## Formatting

### `format(format_string)`

```python
format(format_string: str) -> str
```

Formats the date using Python's [`strftime` format codes](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior).

| Argument | Type | Description |
|----------|------|-------------|
| `format_string` | `str` | A `strftime`-compatible format string. |

```python
Carbon.parse('2025-06-15 14:30:00').format('%Y-%m-%d')      # '2025-06-15'
Carbon.parse('2025-06-15 14:30:00').format('%d/%m/%Y %H:%M') # '15/06/2025 14:30'
```

---

### `toDateTimeString(with_milliseconds=False)`

```python
toDateTimeString(with_milliseconds: bool = False) -> str
```

Returns the date and time as a string in `YYYY-MM-DD HH:MM:SS` format. If `with_milliseconds` is `True`, microseconds are included.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `with_milliseconds` | `bool` | `False` | Include microseconds in the output. |

```python
dt = Carbon.parse('2025-06-15 14:30:45.123456')

dt.toDateTimeString()                       # '2025-06-15 14:30:45'
dt.toDateTimeString(with_milliseconds=True) # '2025-06-15 14:30:45.123456'
```

---

### `toDateString()`

```python
toDateString() -> str
```

Returns the date as a string in `YYYY-MM-DD` format.

```python
Carbon.parse('2025-06-15 14:30:00').toDateString()  # '2025-06-15'
```

---

### `toTimeString()`

```python
toTimeString() -> str
```

Returns the time as a string in `HH:MM:SS` format.

```python
Carbon.parse('2025-06-15 14:30:45').toTimeString()  # '14:30:45'
```

---

### `toDatetime()`

```python
toDatetime() -> datetime
```

Returns the underlying Python `datetime` object.

```python
dt = Carbon.parse('2025-06-15').toDatetime()
isinstance(dt, datetime)  # True
```

---

### `toCookieString()`

```python
toCookieString() -> str
```

Returns the date formatted as a cookie-style string (e.g. `'Wed, 18-Aug-2021 00:00:00 UTC'`).

> **Important:** The Carbon instance must be timezone-aware. Use `Carbon.utcnow()` or convert with `.utc()` first, otherwise a `ValueError` is raised.

```python
Carbon.utcnow().toCookieString()  # e.g. 'Tue, 04-Mar-2026 13:52:35 UTC'
```

---

### `toISOString()`

```python
toISOString() -> str
```

Returns the date in ISO 8601-like format: `YYYY-MM-DDTHH:MM:SS.ffffffZ`.

```python
Carbon.parse('2025-06-15 14:30:00').toISOString()
# '2025-06-15T14:30:00.000000Z'
```

---

## Comparison

All comparison methods accept another `Carbon` instance and return a `bool`.

### `equalTo(carbon)`

```python
equalTo(carbon: Carbon) -> bool
```

Returns `True` if both instances represent exactly the same date and time (down to microseconds).

```python
a = Carbon.parse('2025-01-01 00:00:00')
b = Carbon.parse('2025-01-01 00:00:00')
a.equalTo(b)  # True
```

---

### `notEqualTo(carbon)`

```python
notEqualTo(carbon: Carbon) -> bool
```

Returns `True` if the two instances differ in any component.

```python
a = Carbon.parse('2025-01-01')
b = Carbon.parse('2025-01-02')
a.notEqualTo(b)  # True
```

---

### `greaterThan(carbon)`

```python
greaterThan(carbon: Carbon) -> bool
```

Returns `True` if this instance is **after** the other (by timestamp).

```python
later = Carbon.parse('2025-06-15')
earlier = Carbon.parse('2025-01-01')
later.greaterThan(earlier)  # True
```

---

### `greaterThanOrEqualTo(carbon)`

```python
greaterThanOrEqualTo(carbon: Carbon) -> bool
```

Returns `True` if this instance is **after or at the same time** as the other.

---

### `lessThan(carbon)`

```python
lessThan(carbon: Carbon) -> bool
```

Returns `True` if this instance is **before** the other.

---

### `lessThanOrEqualTo(carbon)`

```python
lessThanOrEqualTo(carbon: Carbon) -> bool
```

Returns `True` if this instance is **before or at the same time** as the other.

---

### `between(low, high, included=True)`

```python
between(low: Carbon, high: Carbon, included: bool = True) -> bool
```

Returns `True` if this instance falls between `low` and `high`.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `low` | `Carbon` | — | Lower bound. |
| `high` | `Carbon` | — | Upper bound. |
| `included` | `bool` | `True` | If `True`, the bounds are inclusive (`>=` / `<=`). If `False`, exclusive (`>` / `<`). |

```python
now = Carbon.now()
now.between(Carbon.yesterday(), Carbon.tomorrow())            # True (inclusive)
now.between(Carbon.yesterday(), Carbon.tomorrow(), False)     # True (exclusive)

Carbon.yesterday().between(Carbon.yesterday(), Carbon.tomorrow(), False)  # False
```

---

### `betweenIncluded(low, high)`

```python
betweenIncluded(low: Carbon, high: Carbon) -> bool
```

Returns `True` if this instance is `>= low` and `<= high` (inclusive bounds).

---

### `betweenExcluded(low, high)`

```python
betweenExcluded(low: Carbon, high: Carbon) -> bool
```

Returns `True` if this instance is `> low` and `< high` (exclusive bounds).

---

### `isSameMinute(carbon, match_date=True)`

```python
isSameMinute(carbon: Carbon, match_date: bool = True) -> bool
```

Checks if both instances share the same minute.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `carbon` | `Carbon` | — | The instance to compare. |
| `match_date` | `bool` | `True` | If `True`, the full date and hour must also match. If `False`, only the minute component is compared. |

```python
a = Carbon.parse('2025-06-15 14:30:00')
b = Carbon.parse('2025-06-15 14:30:59')
a.isSameMinute(b)  # True

c = Carbon.parse('2026-01-01 08:30:00')
a.isSameMinute(c, match_date=False)  # True (both minute == 30)
```

---

### `isSameHour(carbon, match_date=True)`

```python
isSameHour(carbon: Carbon, match_date: bool = True) -> bool
```

Checks if both instances share the same hour.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `carbon` | `Carbon` | — | The instance to compare. |
| `match_date` | `bool` | `True` | If `True`, the full date must also match. If `False`, only the hour component is compared. |

---

### `isSameDay(carbon, match_date=True)`

```python
isSameDay(carbon: Carbon, match_date: bool = True) -> bool
```

Checks if both instances share the same day.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `carbon` | `Carbon` | — | The instance to compare. |
| `match_date` | `bool` | `True` | If `True`, year and month must also match. If `False`, only the day number is compared. |

---

### `isSameWeek(carbon)`

```python
isSameWeek(carbon: Carbon) -> bool
```

Returns `True` if both instances fall in the same week of the month.

---

### `isSameMonth(carbon, match_date=True)`

```python
isSameMonth(carbon: Carbon, match_date: bool = True) -> bool
```

Checks if both instances share the same month.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `carbon` | `Carbon` | — | The instance to compare. |
| `match_date` | `bool` | `True` | If `True`, the year must also match. If `False`, only the month number is compared. |

---

### `isSameYear(carbon)`

```python
isSameYear(carbon: Carbon) -> bool
```

Returns `True` if both instances share the same year.

---

### `isSameQuarter(carbon, match_date=True)`

```python
isSameQuarter(carbon: Carbon, match_date: bool = True) -> bool
```

Checks if both instances fall in the same quarter.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `carbon` | `Carbon` | — | The instance to compare. |
| `match_date` | `bool` | `True` | If `True`, the year must also match. If `False`, only the quarter number is compared. |

---

## Checks

Boolean methods to test characteristics of the current date.

### `isNextYear()`

```python
isNextYear() -> bool
```

Returns `True` if the instance's year equals `current year + 1`.

---

### `isLastYear()`

```python
isLastYear() -> bool
```

Returns `True` if the instance's year equals `current year - 1`.

---

### `isNextMonth()`

```python
isNextMonth() -> bool
```

Returns `True` if the instance's month equals `current month + 1`.

---

### `isLastMonth()`

```python
isLastMonth() -> bool
```

Returns `True` if the instance's month equals `current month - 1`.

---

### `isStartOfDay()`

```python
isStartOfDay() -> bool
```

Returns `True` if the time is exactly `00:00:00`.

```python
Carbon.parse('2025-06-15 00:00:00').isStartOfDay()  # True
Carbon.parse('2025-06-15 00:00:01').isStartOfDay()  # False
```

---

### `isEndOfDay()`

```python
isEndOfDay() -> bool
```

Returns `True` if the time is exactly `23:59:59`.

```python
Carbon.parse('2025-06-15 23:59:59').isEndOfDay()  # True
```

---

### `isFuture()`

```python
isFuture() -> bool
```

Returns `True` if the instance is in the future (timestamp > now).

```python
Carbon.tomorrow().isFuture()   # True
Carbon.yesterday().isFuture()  # False
```

---

### `isPast()`

```python
isPast() -> bool
```

Returns `True` if the instance is in the past (timestamp < now).

```python
Carbon.yesterday().isPast()  # True
Carbon.tomorrow().isPast()   # False
```

---

### `isMonday()`

```python
isMonday() -> bool
```

Returns `True` if the instance falls on a Monday.

---

### `isTuesday()`

```python
isTuesday() -> bool
```

Returns `True` if the instance falls on a Tuesday.

---

### `isWednesday()`

```python
isWednesday() -> bool
```

Returns `True` if the instance falls on a Wednesday.

```python
Carbon.parse('2021-08-18').isWednesday()  # True
```

---

### `isThursday()`

```python
isThursday() -> bool
```

Returns `True` if the instance falls on a Thursday.

---

### `isFriday()`

```python
isFriday() -> bool
```

Returns `True` if the instance falls on a Friday.

---

### `isSaturday()`

```python
isSaturday() -> bool
```

Returns `True` if the instance falls on a Saturday.

---

### `isSunday()`

```python
isSunday() -> bool
```

Returns `True` if the instance falls on a Sunday.

---

### `isLeapYear()`

```python
isLeapYear() -> bool
```

Returns `True` if the instance's year is a leap year.

```python
Carbon.parse('2024-01-01').isLeapYear()  # True
Carbon.parse('2025-01-01').isLeapYear()  # False
```

---

### `isWeekend()`

```python
isWeekend() -> bool
```

Returns `True` if the instance falls on Saturday or Sunday.

---

### `isDayOfWeek(weekday)`

```python
isDayOfWeek(weekday: int) -> bool
```

Returns `True` if the instance matches the given weekday.

| Argument | Type | Description |
|----------|------|-------------|
| `weekday` | `int` | The weekday to check (use `Carbon.MONDAY` through `Carbon.SUNDAY`). |

```python
Carbon.parse('2021-08-18').isDayOfWeek(Carbon.WEDNESDAY)  # True
```

---

### `isLastDayOfMonth()`

```python
isLastDayOfMonth() -> bool
```

Returns `True` if the instance's day is the last day of its month.

```python
Carbon.parse('2025-02-28').isLastDayOfMonth()  # True
Carbon.parse('2024-02-28').isLastDayOfMonth()  # False (2024 is a leap year → 29 days)
Carbon.parse('2021-08-31').isLastDayOfMonth()  # True
```

---

### `isFirstDayOfMonth()`

```python
isFirstDayOfMonth() -> bool
```

Returns `True` if the instance's day is `1`.

```python
Carbon.parse('2025-03-01').isFirstDayOfMonth()  # True
```

---

## Addition and Subtraction

All methods return a **new** `Carbon` instance.

### `add(amount, unit)`

```python
add(amount: int, unit: str) -> Carbon
```

A generic addition method. Internally delegates to the matching `add{Unit}()` method.

| Argument | Type | Description |
|----------|------|-------------|
| `amount` | `int` | The amount to add. |
| `unit` | `str` | The time unit: `'microSeconds'`, `'seconds'`, `'minutes'`, `'hours'`, `'days'`, `'weeks'`, `'months'`, or `'years'`. |

```python
Carbon.now().add(10, 'years')   # same as addYears(10)
Carbon.now().add(3, 'months')   # same as addMonths(3)
```

---

### `addMicroSeconds(microseconds=1)`

```python
addMicroSeconds(microseconds: int = 1) -> Carbon
```

Adds the given number of microseconds.

---

### `addSeconds(seconds=1)`

```python
addSeconds(seconds: int = 1) -> Carbon
```

Adds the given number of seconds.

---

### `addMinutes(minutes=1)`

```python
addMinutes(minutes: int = 1) -> Carbon
```

Adds the given number of minutes.

---

### `addHours(hours=1)`

```python
addHours(hours: int = 1) -> Carbon
```

Adds the given number of hours.

---

### `addDays(days=1)`

```python
addDays(days: int = 1) -> Carbon
```

Adds the given number of days.

```python
Carbon.parse('2025-01-30').addDays(5).toDateString()  # '2025-02-04'
```

---

### `addWeeks(weeks=1)`

```python
addWeeks(weeks: int = 1) -> Carbon
```

Adds the given number of weeks.

---

### `addMonths(months=1)`

```python
addMonths(months: int = 1) -> Carbon
```

Adds the given number of months using `dateutil.relativedelta`, which correctly handles varying month lengths.

```python
Carbon.parse('2025-01-31').addMonths(1).toDateString()  # '2025-02-28'
```

---

### `addYears(years=1)`

```python
addYears(years: int = 1) -> Carbon
```

Adds the given number of years using `dateutil.relativedelta`.

```python
Carbon.parse('2024-02-29').addYears(1).toDateString()  # '2025-02-28'
```

---

### `sub(amount, unit)`

```python
sub(amount: int, unit: str) -> Carbon
```

A generic subtraction method. Internally delegates to the matching `sub{Unit}()` method.

| Argument | Type | Description |
|----------|------|-------------|
| `amount` | `int` | The amount to subtract. |
| `unit` | `str` | The time unit (same options as `add()`). |

```python
Carbon.now().sub(10, 'years')   # same as subYears(10)
```

---

### `subMicroSeconds(microseconds=1)`

```python
subMicroSeconds(microseconds: int = 1) -> Carbon
```

Subtracts the given number of microseconds.

---

### `subSeconds(seconds=1)`

```python
subSeconds(seconds: int = 1) -> Carbon
```

Subtracts the given number of seconds.

---

### `subMinutes(minutes=1)`

```python
subMinutes(minutes: int = 1) -> Carbon
```

Subtracts the given number of minutes.

---

### `subHours(hours=1)`

```python
subHours(hours: int = 1) -> Carbon
```

Subtracts the given number of hours.

---

### `subDays(days=1)`

```python
subDays(days: int = 1) -> Carbon
```

Subtracts the given number of days.

---

### `subWeeks(weeks=1)`

```python
subWeeks(weeks: int = 1) -> Carbon
```

Subtracts the given number of weeks.

---

### `subMonths(months=1)`

```python
subMonths(months: int = 1) -> Carbon
```

Subtracts the given number of months.

---

### `subYears(years=1)`

```python
subYears(years: int = 1) -> Carbon
```

Subtracts the given number of years.

---

## Difference

Methods to compute the difference between two `Carbon` instances.

### `difference(carbon)`

```python
difference(carbon: Carbon) -> dict
```

Returns a dictionary with a human-readable breakdown of the difference using `dateutil.relativedelta`.

**Returned keys:** `years`, `months`, `days`, `leapdays`, `hours`, `minutes`, `seconds`, `microseconds`.

```python
earlier = Carbon.parse('2021-01-01 00:00:00.000000')
later = Carbon.parse('2022-03-04 05:06:07.123456')

diff = later.difference(earlier)
# {
#     'years': 1,
#     'months': 2,
#     'days': 3,
#     'leapdays': 0,
#     'hours': 5,
#     'minutes': 6,
#     'seconds': 7,
#     'microseconds': 123456
# }
```

---

### `diffIn(unit, carbon)`

```python
diffIn(unit: str, carbon: Carbon) -> int | float
```

A generic difference method. Delegates to the matching `diffIn{Unit}()` method.

| Argument | Type | Description |
|----------|------|-------------|
| `unit` | `str` | The time unit: `'microseconds'`, `'seconds'`, `'minutes'`, `'hours'`, `'days'`, `'weeks'`, `'months'`, or `'years'`. |
| `carbon` | `Carbon` | The instance to compare against. |

```python
later.diffIn('days', earlier)    # float: total days
later.diffIn('years', earlier)   # int: 1
```

---

### `diffInMicroseconds(carbon)`

```python
diffInMicroseconds(carbon: Carbon) -> int
```

Returns the difference in microseconds as an `int`.

---

### `diffInSeconds(carbon)`

```python
diffInSeconds(carbon: Carbon) -> float
```

Returns the difference in seconds as a `float`.

---

### `diffInMinutes(carbon)`

```python
diffInMinutes(carbon: Carbon) -> float
```

Returns the difference in minutes as a `float`.

---

### `diffInHours(carbon)`

```python
diffInHours(carbon: Carbon) -> float
```

Returns the difference in hours as a `float`.

---

### `diffInDays(carbon)`

```python
diffInDays(carbon: Carbon) -> float
```

Returns the difference in days as a `float`.

```python
a = Carbon.parse('2025-01-01')
b = Carbon.parse('2025-01-10')
b.diffInDays(a)  # 9.0
```

---

### `diffInWeeks(carbon)`

```python
diffInWeeks(carbon: Carbon) -> float
```

Returns the difference in weeks as a `float`.

---

### `diffInMonths(carbon)`

```python
diffInMonths(carbon: Carbon) -> int
```

Returns the total difference in months as an `int` (years × 12 + months component from `relativedelta`).

```python
a = Carbon.parse('2021-01-01')
b = Carbon.parse('2022-03-04')
b.diffInMonths(a)  # 14
```

---

### `diffInYears(carbon)`

```python
diffInYears(carbon: Carbon) -> int
```

Returns the difference in whole years as an `int`.

---

## Converters

### `utc()`

```python
utc() -> Carbon
```

Converts the instance to UTC. The instance must already carry timezone information (e.g., from `Carbon.parse()` with timezone offset).

```python
local = Carbon.parse('2021-08-18T10:00:00+02:00')
utc = local.utc()

utc.toDateTimeString()            # '2021-08-18 08:00:00'
utc.toDatetime().tzname()         # 'UTC'
```

---

## Modifiers

Methods that move a `Carbon` instance to the boundary of a given time period. All return a **new** `Carbon` instance.

### `startOf(unit)` / `endOf(unit)`

```python
startOf(unit: str) -> Carbon
endOf(unit: str) -> Carbon
```

Generic boundary methods that delegate to the specific `startOf{Unit}()` / `endOf{Unit}()` methods.

| Argument | Type | Description |
|----------|------|-------------|
| `unit` | `str` | `'second'`, `'minute'`, `'hour'`, `'day'`, `'week'`, `'month'`, or `'year'`. |

```python
Carbon.now().startOf('minute')  # same as startOfMinute()
Carbon.now().endOf('day')       # same as endOfDay()
```

---

### `startOfSecond()` / `endOfSecond()`

```python
startOfSecond() -> Carbon   # microsecond set to 0
endOfSecond() -> Carbon     # microsecond set to 999999
```

---

### `startOfMinute()` / `endOfMinute()`

```python
startOfMinute() -> Carbon   # second=0, microsecond=0
endOfMinute() -> Carbon     # second=59, microsecond=999999
```

---

### `startOfHour()` / `endOfHour()`

```python
startOfHour() -> Carbon     # minute=0, second=0, microsecond=0
endOfHour() -> Carbon       # minute=59, second=59, microsecond=999999
```

---

### `startOfDay()` / `endOfDay()`

```python
startOfDay() -> Carbon      # 00:00:00.000000
endOfDay() -> Carbon        # 23:59:59.999999
```

```python
dt = Carbon.parse('2025-06-15 14:30:45')
dt.startOfDay().toDateTimeString()  # '2025-06-15 00:00:00'
dt.endOfDay().toDateTimeString()    # '2025-06-15 23:59:59'
```

---

### `startOfWeek()` / `endOfWeek()`

```python
startOfWeek() -> Carbon     # Monday 00:00:00.000000
endOfWeek() -> Carbon       # Sunday 23:59:59.999999
```

Weeks start on **Monday** (ISO convention).

```python
dt = Carbon.parse('2021-08-18 14:15:16.123456')   # Wednesday
dt.startOfWeek().toDateTimeString(True)  # '2021-08-16 00:00:00.000000' (Monday)
dt.endOfWeek().toDateTimeString(True)    # '2021-08-22 23:59:59.999999' (Sunday)
```

---

### `startOfMonth()` / `endOfMonth()`

```python
startOfMonth() -> Carbon    # 1st day of month, 00:00:00.000000
endOfMonth() -> Carbon      # last day of month, 23:59:59.999999
```

```python
dt = Carbon.parse('2025-03-15 10:00:00')
dt.startOfMonth().toDateString()  # '2025-03-01'
dt.endOfMonth().toDateString()    # '2025-03-31'
```

---

### `startOfYear()` / `endOfYear()`

```python
startOfYear() -> Carbon     # January 1, 00:00:00.000000
endOfYear() -> Carbon       # December 31, 23:59:59.999999
```

```python
dt = Carbon.parse('2021-08-18 14:15:16.123456')
dt.startOfYear().toDateTimeString(True)  # '2021-01-01 00:00:00.000000'
dt.endOfYear().toDateTimeString(True)    # '2021-12-31 23:59:59.999999'
```

---

## Next Weekday

### `next(weekday=None)`

```python
next(weekday: int = None) -> Carbon
```

Returns a `Carbon` instance advanced to the **next** occurrence of the given weekday. The time of day is preserved.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `weekday` | `int` or `None` | `None` | Target weekday (`Carbon.MONDAY` through `Carbon.SUNDAY`). Defaults to the current weekday if `None`. |

```python
base = Carbon.parse('2021-08-18 12:34:56')     # Wednesday
base.next(Carbon.MONDAY).toDateString()        # '2021-08-23'
base.next(Carbon.FRIDAY).toDateString()        # '2021-08-27'
```

---

### `nextMonday()` … `nextSunday()`

Convenience shortcuts:

```python
nextMonday() -> Carbon
nextTuesday() -> Carbon
nextWednesday() -> Carbon
nextThursday() -> Carbon
nextFriday() -> Carbon
nextSaturday() -> Carbon
nextSunday() -> Carbon
```

```python
base = Carbon.parse('2021-08-18 12:34:56')   # Wednesday
base.nextMonday().toDateTimeString()          # '2021-08-23 12:34:56'
base.nextSunday().toDateTimeString()          # '2021-08-29 12:34:56'
```

---

## datetime and timedelta Proxies

Static methods that directly expose Python's `datetime` and `timedelta` constructors for convenience.

```python
Carbon.datetime(2025, 6, 15, 10, 30)  # datetime(2025, 6, 15, 10, 30)
Carbon.timedelta(days=1)              # timedelta(days=1)
```

---

## Proxy Attributes and Methods

Carbon proxies attribute access to the underlying `datetime` object via `__getattr__`. This means you can access any `datetime` attribute or method directly on a `Carbon` instance:

```python
dt = Carbon.parse('2021-08-18')

dt.year          # 2021   (datetime attribute)
dt.month         # 8
dt.weekday()     # 2      (datetime method, via proxy)
dt.strftime('%Y-%m')  # '2021-08' (datetime method, via proxy)
```

If the requested attribute does not exist on the underlying `datetime`, an `AttributeError` is raised.

---

## License

This project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

Check the [original project](https://github.com/briannesbitt/Carbon) source for more details.
