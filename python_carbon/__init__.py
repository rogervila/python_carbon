import locale
from calendar import isleap, monthcalendar, monthrange
from datetime import datetime, timedelta
from types import MethodType
from typing import Union
from dateutil.parser import parse as date_parser
from dateutil.relativedelta import relativedelta
from dateutil.tz import tzutc


class Carbon:

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    def __init__(self, now: Union['Carbon', datetime, None] = None):
        self._date = None  # type: datetime

        if now is None:
            self._date = datetime.now()
            return

        if isinstance(now, datetime):
            self._date = now
            return

        if isinstance(now, Carbon):
            self._date = now.toDatetime()
            return

        raise ValueError

    #################
    # Instantiation #
    #################

    @staticmethod
    def parse(date_string: str) -> 'Carbon':
        return Carbon(date_parser(date_string))

    @staticmethod
    def now() -> 'Carbon':
        return Carbon(datetime.now())

    @staticmethod
    def utcnow() -> 'Carbon':
        return Carbon(datetime.now(tzutc()))

    @staticmethod
    def yesterday() -> 'Carbon':
        return Carbon.now().subDays(1)

    @staticmethod
    def utcyesterday() -> 'Carbon':
        return Carbon.utcnow().subDays(1)

    @staticmethod
    def tomorrow() -> 'Carbon':
        return Carbon.now().addDays(1)

    @staticmethod
    def utctomorrow() -> 'Carbon':
        return Carbon.utcnow().addDays(1)

    @staticmethod
    def create_from_format(format_string: str, date_string: str) -> 'Carbon':
        return Carbon(datetime.strptime(date_string, format_string))

    @staticmethod
    def create_from_timestamp(timestamp: int) -> 'Carbon':
        return Carbon(datetime.fromtimestamp(timestamp))

    @staticmethod
    def create_from_date(year: int, month: int, day: int) -> 'Carbon':
        return Carbon(datetime.now().replace(year=year, month=month, day=day))

    @staticmethod
    def create_midnight_date(year: int, month: int, day: int) -> 'Carbon':
        return Carbon(datetime(year, month, day))

    @staticmethod
    def create_from_time(hour: int, minute: int, second: int) -> 'Carbon':
        return Carbon(datetime.now().replace(hour=hour, minute=minute, second=second))

    ##############
    # Properties #
    ##############

    @property
    def year(self) -> int:
        return self._date.year

    @property
    def month(self) -> int:
        return self._date.month

    @property
    def day(self) -> int:
        return self._date.day

    @property
    def hour(self) -> int:
        return self._date.hour

    @property
    def minute(self) -> int:
        return self._date.minute

    @property
    def second(self) -> int:
        return self._date.second

    @property
    def micro(self) -> int:
        return self._date.microsecond

    @property
    def timestamp(self) -> float:
        return datetime.timestamp(self._date)

    @property
    def day_of_week(self) -> int:
        return self._date.weekday()

    @property
    def day_of_week_iso(self) -> int:
        return self._date.isoweekday()

    @property
    def english_day_of_week(self) -> str:
        return self.locale('en_US').day_name

    @property
    def short_english_day_of_week(self) -> str:
        return self.locale('en_US').short_day_name

    @property
    def day_name(self) -> str:
        return self.strftime('%A')

    @property
    def short_day_name(self) -> str:
        return self.strftime('%a')

    @property
    def month_name(self) -> str:
        return self.strftime('%B')

    @property
    def short_month_name(self) -> str:
        return self.strftime('%b')

    @property
    def day_of_year(self) -> int:
        return int(self.strftime('%j'))

    def getWeekOfMonth(self, start: int = 0) -> int:
        weeks = monthcalendar(self.getYear(), self.getMonth())
        day = self.getDay()

        for key, week in enumerate(weeks, start=start):
            if day in week:
                return key

        raise ValueError

    def getWeekOfYear(self) -> int:
        return int(self.format('%W'))

    def getQuarter(self, start: int = 1) -> int:
        quarters = self.getQuarters(start)
        month = self.getMonth()

        for key, quarter in enumerate(quarters):
            if month in quarter:
                return key

        raise ValueError

    def getQuarters(self, start: int = 1) -> list:
        months_amount = 12
        quarter_months_amount = 3

        months = []
        quarters = []

        for i in range(months_amount):
            month = start + i
            if month > months_amount:
                month = month - months_amount

            months.append(month)

        for i in range(0, months_amount, quarter_months_amount):
            quarters.append(months[i:i+quarter_months_amount])

        return quarters

    def getDaysInMonth(self) -> int:
        return monthrange(self.getDay(), self.getMonth())[1]

    def getMonthFirstWeekDay(self) -> int:
        return monthrange(self.getDay(), self.getMonth())[0]

    ###########
    # Setters #
    ###########

    def set_year(self, year: int) -> 'Carbon':
        return Carbon(self._date.replace(year=year))

    def set_month(self, month: int) -> 'Carbon':
        return Carbon(self._date.replace(month=month))

    def set_day(self, day: int) -> 'Carbon':
        return Carbon(self._date.replace(day=day))

    def set_hour(self, hour: int) -> 'Carbon':
        return Carbon(self._date.replace(hour=hour))

    def set_minute(self, minute: int) -> 'Carbon':
        return Carbon(self._date.replace(minute=minute))

    def set_second(self, second: int) -> 'Carbon':
        return Carbon(self._date.replace(second=second))

    def set_microsecond(self, microsecond: int) -> 'Carbon':
        return Carbon(self._date.replace(microsecond=microsecond))

    ##############
    # Formatting #
    ##############

    def format(self, format_string: str) -> str:
        return self._date.strftime(format_string)

    def to_date_time_string(self, with_milliseconds: bool = False) -> str:
        return self.format('%Y-%m-%d %H:%M:%S.%f' if with_milliseconds else '%Y-%m-%d %H:%M:%S')

    def to_date_string(self) -> str:
        return self.format('%Y-%m-%d')

    def to_time_string(self) -> str:
        return self.format('%H:%M:%S')

    def to_datetime(self) -> datetime:
        return self._date

    def to_cookie_string(self) -> str:
        tz = self._date.tzname()

        if tz is None:
            raise ValueError('Timzone is not set. Use Carbon.utcnow() instead')

        return self.format('%a, %d-%b-%Y %T ') + tz

    def to_iso_string(self) -> str:
        return self.format('%Y-%m-%dT%H:%M:%S.%fZ')

    ##############
    # Comparison #
    ##############

    def equal_to(self, carbon: 'Carbon') -> bool:
        return self._date.year == carbon.year \
            and self._date.month == carbon.month \
            and self._date.day == carbon.day \
            and self._date.hour == carbon.hour \
            and self._date.minute == carbon.minute \
            and self._date.second == carbon.second \
            and self._date.microsecond == carbon.microsecond

    def notEqualTo(self, carbon: 'Carbon') -> bool:
        return not self.equal_to(carbon)

    def greaterThan(self, carbon: 'Carbon') -> bool:
        return self.getTimestamp() > carbon.getTimestamp()

    def greaterThanOrEqualTo(self, carbon: 'Carbon') -> bool:
        return self.getTimestamp() >= carbon.getTimestamp()

    def lessThan(self, carbon: 'Carbon') -> bool:
        return self.getTimestamp() < carbon.getTimestamp()

    def lessThanOrEqualTo(self, carbon: 'Carbon') -> bool:
        return self.getTimestamp() <= carbon.getTimestamp()

    def between(self, low: 'Carbon', high: 'Carbon', included: bool = True) -> bool:
        return self.betweenIncluded(low, high) if included else self.betweenExcluded(low, high)

    def betweenIncluded(self, low: 'Carbon', high: 'Carbon') -> bool:
        return self.getTimestamp() >= low.getTimestamp() and self.getTimestamp() <= high.getTimestamp()

    def betweenExcluded(self, low: 'Carbon', high: 'Carbon') -> bool:
        return self.getTimestamp() > low.getTimestamp() and self.getTimestamp() < high.getTimestamp()

    def isSameMinute(self, carbon: 'Carbon', match_date: bool = True) -> bool:
        return (self.getMinute() == carbon.getMinute()) if not match_date else (
            self.getYear() == carbon.getYear()
            and self.getMonth() == carbon.getMonth()
            and self.getDay() == carbon.getDay()
            and self.getHour() == carbon.getHour()
            and self.getMinute() == carbon.getMinute()
        )

    def isSameHour(self, carbon: 'Carbon', match_date: bool = True) -> bool:
        return (self.getHour() == carbon.getHour()) if not match_date else (
            self.getYear() == carbon.getYear()
            and self.getMonth() == carbon.getMonth()
            and self.getDay() == carbon.getDay()
            and self.getHour() == carbon.getHour()
        )

    def isSameDay(self, carbon: 'Carbon', match_date: bool = True) -> bool:
        return (self.getDay() == carbon.getDay()) if not match_date else (
            self.getYear() == carbon.getYear()
            and self.getMonth() == carbon.getMonth()
            and self.getDay() == carbon.getDay()
        )

    def isSameWeek(self, carbon: 'Carbon') -> bool:
        return self.getWeekOfMonth() == carbon.getWeekOfMonth()

    def isSameMonth(self, carbon: 'Carbon', match_date: bool = True) -> bool:
        return (self.getMonth() == carbon.getMonth()) if not match_date else (
            self.getYear() == carbon.getYear()
            and self.getMonth() == carbon.getMonth()
        )

    def isSameYear(self, carbon: 'Carbon') -> bool:
        return self.getYear() == carbon.getYear()

    def isSameQuarter(self, carbon: 'Carbon', match_date: bool = True) -> bool:
        return (self.getQuarter() == carbon.getQuarter()) if not match_date else (
            self.getYear() == carbon.getYear()
            and self.getQuarter() == carbon.getQuarter()
        )

    ##########
    # Checks #
    ##########
    def isNextYear(self) -> bool:
        return self._date.year == datetime.now().year + 1

    def isLastYear(self) -> bool:
        return self._date.year == datetime.now().year - 1

    def isNextMonth(self) -> bool:
        return self._date.month == datetime.now().month + 1

    def isLastMonth(self) -> bool:
        return self._date.month == datetime.now().month - 1

    def isStartOfDay(self) -> bool:
        return self._date.hour == 0 and self._date.minute == 0 and self._date.second == 0

    def isEndOfDay(self) -> bool:
        return self._date.hour == 23 and self._date.minute == 59 and self._date.second == 59

    def isFuture(self) -> bool:
        return self.getTimestamp() > datetime.now().timestamp()

    def isPast(self) -> bool:
        return self.getTimestamp() < datetime.now().timestamp()

    def isMonday(self) -> bool:
        return self._date.weekday() == self.MONDAY

    def isTuesday(self) -> bool:
        return self._date.weekday() == self.TUESDAY

    def isWednesday(self) -> bool:
        return self._date.weekday() == self.WEDNESDAY

    def isThursday(self) -> bool:
        return self._date.weekday() == self.THURSDAY

    def isFriday(self) -> bool:
        return self._date.weekday() == self.FRIDAY

    def is_saturday(self) -> bool:
        return self._date.weekday() == self.SATURDAY

    def is_sunday(self) -> bool:
        return self._date.weekday() == self.SUNDAY

    def is_leap_year(self) -> bool:
        return isleap(self.getYear())

    def is_weekend(self) -> bool:
        return self._date.weekday() in [self.SATURDAY, self.SUNDAY]

    def is_day_of_week(self, weekday: int) -> bool:
        return self._date.weekday() == weekday

    def is_last_day_of_month(self) -> bool:
        return self.getDay() == monthrange(self.getDay(), self.getMonth())[1]

    def is_first_day_of_month(self) -> bool:
        return self.getDay() == 1

    ############################
    # Addition and Subtraction #
    ############################

    def _add_or_sub(self, prefix: str, amount: int, unit: str) -> 'Carbon':
        method = getattr(self, (prefix + '_' + unit.lower()))
        return method(amount)

    def add(self, amount: int, unit: str) -> 'Carbon':
        return self._add_or_sub('add', amount, unit)

    def add_microseconds(self, microseconds: int = 1) -> 'Carbon':
        return Carbon(self._date + timedelta(microseconds=microseconds))

    def add_seconds(self, seconds: int = 1) -> 'Carbon':
        return Carbon(self._date + timedelta(seconds=seconds))

    def add_minutes(self, minutes: int = 1) -> 'Carbon':
        return Carbon(self._date + timedelta(minutes=minutes))

    def add_hours(self, hours: int = 1) -> 'Carbon':
        return Carbon(self._date + timedelta(hours=hours))

    def add_days(self, days: int = 1) -> 'Carbon':
        return Carbon(self._date + timedelta(days=days))

    def add_weeks(self, weeks: int = 1) -> 'Carbon':
        return Carbon(self._date + timedelta(weeks=weeks))

    def add_months(self, months: int = 1) -> 'Carbon':
        return Carbon(self._date + relativedelta(months=months))

    def add_years(self, years: int = 1) -> 'Carbon':
        return Carbon(self._date + relativedelta(years=years))

    def sub(self, amount: int, unit: str) -> 'Carbon':
        return self._add_or_sub('sub', amount, unit)

    def sub_microseconds(self, microseconds: int = 1) -> 'Carbon':
        return Carbon(self._date - timedelta(microseconds=microseconds))

    def sub_seconds(self, seconds: int = 1) -> 'Carbon':
        return Carbon(self._date - timedelta(seconds=seconds))

    def sub_minutes(self, minutes: int = 1) -> 'Carbon':
        return Carbon(self._date - timedelta(minutes=minutes))

    def sub_hours(self, hours: int = 1) -> 'Carbon':
        return Carbon(self._date - timedelta(hours=hours))

    def sub_days(self, days: int = 1) -> 'Carbon':
        return Carbon(self._date - timedelta(days=days))

    def sub_weeks(self, weeks: int = 1) -> 'Carbon':
        return Carbon(self._date - timedelta(weeks=weeks))

    def sub_months(self, months: int = 1) -> 'Carbon':
        return Carbon(self._date - relativedelta(months=months))

    def sub_years(self, years: int = 1) -> 'Carbon':
        return Carbon(self._date - relativedelta(years=years))

    ##############
    # Difference #
    ##############

    def difference(self, carbon: 'Carbon') -> dict:
        delta = relativedelta(self._date, carbon.toDatetime())

        return {key: getattr(delta, key) for key in ['years', 'months', 'days', 'leapdays', 'hours', 'minutes', 'seconds', 'microseconds']}

    def diff_in(self, unit: str, carbon: 'Carbon') -> int:
        method = getattr(self, ('diff_in_' + unit.lower()))
        return method(carbon)

    def diff_in_microseconds(self, carbon: 'Carbon') -> int:
        return self.diffInSeconds(carbon) * 1000

    def diff_in_seconds(self, carbon: 'Carbon') -> int:
        return self.diffInMinutes(carbon) * 60

    def diff_in_minutes(self, carbon: 'Carbon') -> int:
        return self.diffInHours(carbon) * 60

    def diff_in_hours(self, carbon: 'Carbon') -> int:
        return self.diffInDays(carbon) * 24

    def diff_in_days(self, carbon: 'Carbon') -> int:
        return (self._date - carbon.toDatetime()).days

    def diff_in_weeks(self, carbon: 'Carbon') -> float:
        return self.diffInDays(carbon) / 7

    def diff_in_months(self, carbon: 'Carbon') -> int:
        return self.difference(carbon)['months'] \
            + self.diffInYears(carbon) * 12

    def diff_in_years(self, carbon: 'Carbon') -> int:
        return self.difference(carbon)['years']

    #########################
    # Difference for humans #
    #########################

    # TODO: Difference for humans

    #############
    # Modifiers #
    #############

    def _start_or_end(self, prefix: str, unit: str) -> 'Carbon':
        method = getattr(self, (prefix.lower() + '_of_' + unit.lower()))
        return method()

    def start_of(self, unit: str) -> 'Carbon':
        return self._start_or_end('start', unit)

    def end_of(self, unit: str) -> 'Carbon':
        return self._start_or_end('end', unit)

    def start_of_second(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                microsecond=0
            )
        )

    def end_of_second(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                microsecond=999999
            )
        )

    def start_of_minute(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                second=0,
                microsecond=0
            )
        )

    def end_of_minute(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                second=59,
                microsecond=999999
            )
        )

    def start_of_hour(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                minute=0,
                second=0,
                microsecond=0
            )
        )

    def end_of_hour(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                minute=59,
                second=59,
                microsecond=999999
            )
        )

    def start_of_day(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
        )

    def end_of_day(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                hour=23,
                minute=59,
                second=59,
                microsecond=999999
            )
        )

    def start_of_week(self) -> 'Carbon':
        return Carbon(
            (self._date - timedelta(days=self._date.weekday())).replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
        )

    def end_of_week(self) -> 'Carbon':
        return Carbon(
            self.startOfWeek().addDays(6).toDatetime().replace(
                hour=23,
                minute=59,
                second=59,
                microsecond=999999
            )
        )

    def start_of_month(self) -> 'Carbon':
        return Carbon(
            self.now().toDatetime().replace(
                day=1,
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
        )

    def end_of_month(self) -> 'Carbon':
        return Carbon(
            self.now().toDatetime().replace(
                day=self.getDaysInMonth(),
                hour=23,
                minute=59,
                second=59,
                microsecond=999999
            )
        )

    def start_of_year(self) -> 'Carbon':
        return Carbon(
            self.now().toDatetime().replace(
                month=1,
                day=1,
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
        )

    def end_of_year(self) -> 'Carbon':
        return Carbon(
            self.now().toDatetime().replace(
                month=12,
                day=31,
                hour=23,
                minute=59,
                second=59,
                microsecond=999999
            )
        )

    def next(self, weekday: int = None) -> 'Carbon':
        weekday = weekday if weekday is not None else datetime.now().weekday()
        return Carbon(self._date + timedelta(days=weekday - self._date.weekday() + 7))

    def locale(self, loc: str) -> 'Carbon':
        locale.setlocale(locale.LC_TIME, loc)
        return Carbon(self._date)

    ##########################
    # datetime and timedelta #
    ##########################

    @staticmethod
    def datetime(*args, **kwargs) -> datetime:
        return datetime(*args, **kwargs)

    @staticmethod
    def timedelta(*args, **kwargs) -> timedelta:
        return timedelta(*args, **kwargs)

    ################################
    # Proxy attributes and methods #
    ################################

    def __getattr__(self, name):
        if not hasattr(self._date, name):
            raise AttributeError(name)

        attribute = getattr(self._date, name)

        if not isinstance(attribute, MethodType):
            return attribute

        def method(*args, **kwargs):
            return attribute(*args, **kwargs)

        return method()
