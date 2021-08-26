from calendar import isleap, monthcalendar, monthrange
from datetime import datetime, timedelta
from types import MethodType
from typing import Union
from dateutil.parser import parse as date_parser
from dateutil.relativedelta import relativedelta
from dateutil.tz import tzutc

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6


class Carbon:
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
    def createFromFormat(format_string: str, date_string: str) -> 'Carbon':
        return Carbon(datetime.strptime(date_string, format_string))

    ##############
    # Properties #
    ##############

    @property
    def timestamp(self) -> float:
        return self.getTimestamp()

    @property
    def micro(self) -> int:
        return self.getMicro()

    ###########
    # Getters #
    ###########

    def getYear(self) -> int:
        return self._date.year

    def getMonth(self) -> int:
        return self._date.month

    def getDay(self) -> int:
        return self._date.day

    def getHour(self) -> int:
        return self._date.hour

    def getMinute(self) -> int:
        return self._date.minute

    def getSecond(self) -> int:
        return self._date.second

    def getMicro(self) -> int:
        return self._date.microsecond

    def getTimestamp(self) -> float:
        return datetime.timestamp(self._date)

    def getDayOfWeek(self) -> int:
        return self._date.weekday()

    def getDayOfYear(self) -> int:
        return self._date.timetuple().tm_yday

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

    def setYear(self, year: int) -> 'Carbon':
        return Carbon(self._date.replace(year=year))

    def setMonth(self, month: int) -> 'Carbon':
        return Carbon(self._date.replace(month=month))

    def setHour(self, hour: int) -> 'Carbon':
        return Carbon(self._date.replace(hour=hour))

    def setMinute(self, minute: int) -> 'Carbon':
        return Carbon(self._date.replace(minute=minute))

    def setSecond(self, second: int) -> 'Carbon':
        return Carbon(self._date.replace(second=second))

    ##############
    # Formatting #
    ##############

    def format(self, format_string: str) -> str:
        return self._date.strftime(format_string)

    def toDateTimeString(self, with_milliseconds: bool = False) -> str:
        return self.format('%Y-%m-%d %H:%M:%S.%f' if with_milliseconds else '%Y-%m-%d %H:%M:%S')

    def toDateString(self) -> str:
        return self.format('%Y-%m-%d')

    def toTimeString(self) -> str:
        return self.format('%H:%M:%S')

    def toDatetime(self) -> datetime:
        return self._date

    def toCookieString(self) -> str:
        tz = self._date.tzname()

        if tz is None:
            raise ValueError('Timzone is not set. Use Carbon.utcnow() instead')

        return self.format('%a, %d-%b-%Y %T ') + tz

    def toISOString(self) -> str:
        return self.format('%Y-%m-%dT%H:%M:%S.%fZ')

    ##############
    # Comparison #
    ##############

    def equalTo(self, carbon: 'Carbon') -> bool:
        return self._date.year == carbon.year \
            and self._date.month == carbon.month \
            and self._date.day == carbon.day \
            and self._date.hour == carbon.hour \
            and self._date.minute == carbon.minute \
            and self._date.second == carbon.second \
            and self._date.microsecond == carbon.microsecond

    def notEqualTo(self, carbon: 'Carbon') -> bool:
        return not self.equalTo(carbon)

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

    def isLeapYear(self) -> bool:
        return isleap(self.getYear())

    def isWeekend(self) -> bool:
        return self._date.weekday() in [SATURDAY, SUNDAY]

    def isDayOfWeek(self, weekday: int) -> bool:
        return self._date.weekday() == weekday

    def isLastDayOfMonth(self) -> bool:
        return self.getDay() == monthrange(self.getDay(), self.getMonth())[1]

    ############################
    # Addition and Subtraction #
    ############################

    def _add_or_sub(self, prefix: str, amount: int, unit: str) -> 'Carbon':
        method = getattr(self, (prefix + unit.capitalize()))
        return method(amount)

    def add(self, amount: int, unit: str) -> 'Carbon':
        return self._add_or_sub('add', amount, unit)

    def addSeconds(self, seconds: int) -> 'Carbon':
        return Carbon(self._date + timedelta(seconds=seconds))

    def addMinutes(self, minutes: int) -> 'Carbon':
        return Carbon(self._date + timedelta(minutes=minutes))

    def addHours(self, hours: int) -> 'Carbon':
        return Carbon(self._date + timedelta(hours=hours))

    def addDays(self, days: int) -> 'Carbon':
        return Carbon(self._date + timedelta(days=days))

    def addWeeks(self, weeks: int) -> 'Carbon':
        return Carbon(self._date + timedelta(weeks=weeks))

    def addYears(self, years: int) -> 'Carbon':
        return Carbon(
            self.toDatetime().replace(year=(self.getYear() + years))
        )

    def sub(self, amount: int, unit: str) -> 'Carbon':
        return self._add_or_sub('sub', amount, unit)

    def subSeconds(self, seconds: int) -> 'Carbon':
        return Carbon(self._date - timedelta(seconds=seconds))

    def subMinutes(self, minutes: int) -> 'Carbon':
        return Carbon(self._date - timedelta(minutes=minutes))

    def subHours(self, hours: int) -> 'Carbon':
        return Carbon(self._date - timedelta(hours=hours))

    def subDays(self, days: int) -> 'Carbon':
        return Carbon(self._date - timedelta(days=days))

    def subWeeks(self, weeks: int) -> 'Carbon':
        return Carbon(self._date - timedelta(weeks=weeks))

    def subYears(self, years: int) -> 'Carbon':
        return Carbon(
            self.toDatetime().replace(year=(self.getYear() - years))
        )

    ##############
    # Difference #
    ##############

    def difference(self, carbon: 'Carbon') -> dict:
        delta = relativedelta(self._date, carbon.toDatetime())

        return {key: getattr(delta, key) for key in ['years', 'months', 'days', 'leapdays', 'hours', 'minutes', 'seconds', 'microseconds']}

    def diffIn(self, unit: str, carbon: 'Carbon') -> int:
        method = getattr(self, ('diffIn' + unit.capitalize()))
        return method(carbon)

    def diffInMicroseconds(self, carbon: 'Carbon') -> int:
        return self.diffInSeconds(carbon) * 1000

    def diffInSeconds(self, carbon: 'Carbon') -> int:
        return self.diffInMinutes(carbon) * 60

    def diffInMinutes(self, carbon: 'Carbon') -> int:
        return self.diffInHours(carbon) * 60

    def diffInHours(self, carbon: 'Carbon') -> int:
        return self.diffInDays(carbon) * 24

    def diffInDays(self, carbon: 'Carbon') -> int:
        return (self._date - carbon.toDatetime()).days

    def diffInWeeks(self, carbon: 'Carbon') -> float:
        return self.diffInDays(carbon) / 7

    def diffInMonths(self, carbon: 'Carbon') -> int:
        return self.difference(carbon)['months'] \
            + self.diffInYears(carbon) * 12

    def diffInYears(self, carbon: 'Carbon') -> int:
        return self.difference(carbon)['years']

    #########################
    # Difference for humans #
    #########################

    # TODO: Difference for humans

    #############
    # Modifiers #
    #############

    def _start_or_end(self, prefix: str, unit: str) -> 'Carbon':
        method = getattr(self, (prefix + 'Of' + unit.capitalize()))
        return method()

    def startOf(self, unit: str) -> 'Carbon':
        return self._start_or_end('start', unit)

    def endOf(self, unit: str) -> 'Carbon':
        return self._start_or_end('end', unit)

    def startOfSecond(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                microsecond=0
            )
        )

    def endOfSecond(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                microsecond=999999
            )
        )

    def startOfMinute(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                second=0,
                microsecond=0
            )
        )

    def endOfMinute(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                second=59,
                microsecond=999999
            )
        )

    def startOfHour(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                minute=0,
                second=0,
                microsecond=0
            )
        )

    def endOfHour(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                minute=59,
                second=59,
                microsecond=999999
            )
        )

    def startOfDay(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
        )

    def endOfDay(self) -> 'Carbon':
        return Carbon(
            self._date.replace(
                hour=23,
                minute=59,
                second=59,
                microsecond=999999
            )
        )

    def startOfWeek(self) -> 'Carbon':
        return Carbon(
            (self._date - timedelta(days=self._date.weekday())).replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
        )

    def endOfWeek(self) -> 'Carbon':
        return Carbon(
            self.startOfWeek().addDays(6).toDatetime().replace(
                hour=23,
                minute=59,
                second=59,
                microsecond=999999
            )
        )

    def startOfMonth(self) -> 'Carbon':
        return Carbon(
            self.startOfWeek().addDays(6).toDatetime().replace(
                day=1,
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
        )

    def endOfMonth(self) -> 'Carbon':
        return Carbon(
            self.startOfWeek().addDays(6).toDatetime().replace(
                day=self.getDaysInMonth(),
                hour=23,
                minute=59,
                second=59,
                microsecond=999999
            )
        )

    def startOfYear(self) -> 'Carbon':
        return Carbon(
            self.startOfWeek().addDays(6).toDatetime().replace(
                month=1,
                day=1,
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
        )

    def endOfYear(self) -> 'Carbon':
        return Carbon(
            self.startOfWeek().addDays(6).toDatetime().replace(
                month=12,
                day=31,
                hour=23,
                minute=59,
                second=59,
                microsecond=999999
            )
        )

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
