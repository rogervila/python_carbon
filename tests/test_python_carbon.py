import unittest
from python_carbon import Carbon


class test_python_carbon(unittest.TestCase):
    def test_todo(self):
        self.assertTrue(True)

        print('\n----\nTEST\n----\n')

        print(Carbon.now().addYears(2).toDateString())
        exit()

        dt = Carbon.parse('2021-08-16 01:02:03')
        dt2 = Carbon.parse('2021-08-16 01:02:03')

        print(
            dt.equalTo(dt2)
        )

        dt = Carbon.now()
        dt = Carbon()  # equivalent to Carbon.now()

        dt = Carbon.createFromFormat('%Y-%m-%d', '2021-08-18')

        print(
            dt.getTimestamp()
        )

        print(
            dt.weekday()
        )

        print(
            dt.format('%Y-%m-%d')
        )

        print(
            dt.strftime('%Y-%m')
        )

        print(
            dt.toDateTimeString()
        )

        print(
            dt.addDays(1).setYear(2001).toDateTimeString()
        )

        print(
            dt.year
        )

        print(
            dt.getYear()
        )

        print(
            dt.micro
        )

        print(
            dt.timestamp
        )

        dt = Carbon.now()

        print(
            dt.startOfWeek().format('%Y-%m-%d %H:%M:%S.%f')
        )

        print(
            dt.endOfWeek().format('%Y-%m-%d %H:%M:%S.%f')
        )

        print(
            dt.startOfDay().format('%Y-%m-%d %H:%M:%S.%f')
        )

        print(
            dt.endOfDay().format('%Y-%m-%d %H:%M:%S.%f')
        )

        print(
            dt.startOf('minute').format('%Y-%m-%d %H:%M:%S.%f')
        )

        print(
            dt.endOf('minute').format('%Y-%m-%d %H:%M:%S.%f')
        )

        print(
            dt.startOfHour().format('%Y-%m-%d %H:%M:%S.%f')
        )

        print(
            dt.endOfHour().format('%Y-%m-%d %H:%M:%S.%f')
        )

        print(
            Carbon.parse('2021-08-31').isLastDayOfMonth()
        )

        print(
            Carbon.now().addYears(10).toDateTimeString()
        )

        print(
            Carbon.now().add(10, 'years').toDateTimeString()
        )

        print(
            Carbon.now().subYears(10).toDateTimeString()
        )

        print(
            Carbon.now().sub(10, 'years').toDateTimeString()
        )

        print(type(Carbon.timedelta(days=1)))

        # print(dt.microseconds)
        # print(dt.micro)

        print(
            Carbon.now().difference(Carbon.parse('1992-04-17 17:00:00'))
        )

        print(
            Carbon.now().diffIn('years', Carbon.parse('1992-04-17 17:00:00'))
        )

        print(
            Carbon.now().diffIn('months', Carbon.parse('1992-04-17 17:00:00'))
        )

        print(
            Carbon.now().diffIn('weeks', Carbon.parse('1992-04-17 17:00:00'))
        )

        print(
            Carbon.now().diffIn('days', Carbon.parse('1992-04-17 17:00:00'))
        )

        print(
            Carbon.now().diffIn('hours', Carbon.parse('1992-04-17 17:00:00'))
        )

        print(
            Carbon.now().diffIn('minutes', Carbon.parse('1992-04-17 17:00:00'))
        )

        print(
            Carbon.now().diffIn('seconds', Carbon.parse('1992-04-17 17:00:00'))
        )

        print(
            Carbon.now().diffIn('microseconds', Carbon.parse('1992-04-17 17:00:00'))
        )

        print(
            Carbon.utcnow().toCookieString()
        )

        print(
            Carbon.now().toISOString()
        )

        print(
            Carbon.now().getDayOfYear()
        )

        print(
            Carbon.parse('2022-01-02').getDayOfYear()
        )

        print(
            Carbon.parse('2022-01-01').getWeekOfYear()
        )

        print(
            Carbon.now().getWeekOfMonth()
        )

        print(
            Carbon.now().startOfMonth().toDateTimeString(with_milliseconds=True)
        )

        print(
            Carbon.now().endOfMonth().toDateTimeString(with_milliseconds=True)
        )

        print(
            Carbon.now().startOfYear().toDateTimeString(with_milliseconds=True)
        )

        print(
            Carbon.now().endOfYear().toDateTimeString(with_milliseconds=True)
        )

        print(
            Carbon.now().getQuarters()
        )

        print(
            Carbon.now().getQuarter()
        )

        print(
            Carbon.now().betweenIncluded(Carbon.yesterday(), Carbon.tomorrow())
        )

        print(
            Carbon.now().betweenExcluded(Carbon.yesterday(), Carbon.tomorrow())
        )

        print(
            Carbon.yesterday().betweenIncluded(Carbon.yesterday(), Carbon.tomorrow())
        )

        print(
            Carbon.yesterday().betweenExcluded(Carbon.yesterday(), Carbon.tomorrow())
        )

        print('\n---\nEND\n---\n')


if __name__ == '__main__':
    unittest.main()
