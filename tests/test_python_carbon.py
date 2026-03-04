import unittest
from datetime import timedelta
from python_carbon import Carbon


class test_python_carbon(unittest.TestCase):
    def test_carbon_methods(self) -> None:
        dt = Carbon.parse('2021-08-16 01:02:03')
        dt2 = Carbon.parse('2021-08-16 01:02:03')

        self.assertTrue(dt.equalTo(dt2))

        dt = Carbon.now()
        self.assertIsInstance(dt, Carbon)

        dt = Carbon()  # equivalent to Carbon.now()
        self.assertIsInstance(dt, Carbon)

        dt = Carbon.createFromFormat('%Y-%m-%d', '2021-08-18')
        self.assertEqual(dt.format('%Y-%m-%d'), '2021-08-18')

        self.assertEqual(dt.weekday(), Carbon.WEDNESDAY)
        self.assertEqual(dt.format('%Y-%m-%d'), '2021-08-18')
        self.assertEqual(dt.strftime('%Y-%m'), '2021-08')
        self.assertEqual(dt.toDateTimeString(), '2021-08-18 00:00:00')
        self.assertEqual(dt.addDays(1).setYear(2001).toDateTimeString(), '2001-08-19 00:00:00')
        self.assertEqual(dt.year, 2021)
        self.assertEqual(dt.getYear(), 2021)
        self.assertEqual(dt.micro, 0)
        self.assertIsInstance(dt.timestamp, float)

        dt = Carbon.now()

        start_of_week = dt.startOfWeek()
        end_of_week = dt.endOfWeek()
        start_of_day = dt.startOfDay()
        end_of_day = dt.endOfDay()
        start_of_minute = dt.startOf('minute')
        end_of_minute = dt.endOf('minute')
        start_of_hour = dt.startOfHour()
        end_of_hour = dt.endOfHour()

        self.assertEqual(start_of_week.weekday(), Carbon.MONDAY)
        self.assertTrue(start_of_week.isStartOfDay())
        self.assertEqual(end_of_week.weekday(), Carbon.SUNDAY)
        self.assertTrue(end_of_week.isEndOfDay())

        self.assertTrue(start_of_day.isStartOfDay())
        self.assertTrue(end_of_day.isEndOfDay())

        self.assertEqual(start_of_minute.second, 0)
        self.assertEqual(start_of_minute.microsecond, 0)
        self.assertEqual(end_of_minute.second, 59)
        self.assertEqual(end_of_minute.microsecond, 999999)

        self.assertEqual(start_of_hour.minute, 0)
        self.assertEqual(start_of_hour.second, 0)
        self.assertEqual(start_of_hour.microsecond, 0)
        self.assertEqual(end_of_hour.minute, 59)
        self.assertEqual(end_of_hour.second, 59)
        self.assertEqual(end_of_hour.microsecond, 999999)

        self.assertTrue(Carbon.parse('2021-08-31').isLastDayOfMonth())

        anchor = Carbon.now()
        self.assertTrue(anchor.addYears(10).equalTo(anchor.add(10, 'years')))
        self.assertTrue(anchor.subYears(10).equalTo(anchor.sub(10, 'years')))

        self.assertIsInstance(Carbon.timedelta(days=1), timedelta)

        reference = Carbon.parse('1992-04-17 17:00:00')
        now = Carbon.now()

        diff = now.difference(reference)
        self.assertIsInstance(diff, dict)
        self.assertEqual(
            set(diff.keys()),
            {'years', 'months', 'days', 'leapdays', 'hours', 'minutes', 'seconds', 'microseconds'}
        )

        diff_years = now.diffIn('years', reference)
        diff_months = now.diffIn('months', reference)
        diff_weeks = now.diffIn('weeks', reference)
        diff_days = now.diffIn('days', reference)
        diff_hours = now.diffIn('hours', reference)
        diff_minutes = now.diffIn('minutes', reference)
        diff_seconds = now.diffIn('seconds', reference)
        diff_microseconds = now.diffIn('microseconds', reference)

        self.assertGreater(diff_years, 0)
        self.assertEqual(diff_months, now.difference(reference)['months'] + diff_years * 12)
        self.assertEqual(diff_weeks, diff_days / 7)
        self.assertEqual(diff_hours, diff_days * 24)
        self.assertEqual(diff_minutes, diff_hours * 60)
        self.assertEqual(diff_seconds, diff_minutes * 60)
        self.assertEqual(diff_microseconds, diff_seconds * 1000)

        cookie_string = Carbon.utcnow().toCookieString()
        self.assertIsInstance(cookie_string, str)
        self.assertIn('UTC', cookie_string)

        iso_string = Carbon.now().toISOString()
        self.assertRegex(iso_string, r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$')

        self.assertIn(Carbon.now().getDayOfYear(), range(1, 367))
        self.assertEqual(Carbon.parse('2022-01-02').getDayOfYear(), 2)
        self.assertEqual(Carbon.parse('2022-01-01').getWeekOfYear(), 0)

        week_of_month = Carbon.now().getWeekOfMonth()
        self.assertIn(week_of_month, range(0, 7))

        start_of_month = Carbon.now().startOfMonth()
        end_of_month = Carbon.now().endOfMonth()
        start_of_year = Carbon.now().startOfYear()
        end_of_year = Carbon.now().endOfYear()

        self.assertRegex(start_of_month.toDateTimeString(with_milliseconds=True), r'^\d{4}-\d{2}-01 00:00:00\.\d{6}$')
        self.assertRegex(end_of_month.toDateTimeString(with_milliseconds=True), r'^\d{4}-\d{2}-\d{2} 23:59:59\.\d{6}$')
        self.assertRegex(start_of_year.toDateTimeString(with_milliseconds=True), r'^\d{4}-01-01 00:00:00\.\d{6}$')
        self.assertRegex(end_of_year.toDateTimeString(with_milliseconds=True), r'^\d{4}-12-31 23:59:59\.\d{6}$')

        quarters = Carbon.now().getQuarters()
        quarter = Carbon.now().getQuarter()
        self.assertEqual(len(quarters), 4)
        self.assertTrue(all(len(q) == 3 for q in quarters))
        self.assertIn(quarter, range(0, 4))

        current = Carbon.now()
        yesterday = Carbon.yesterday()
        tomorrow = Carbon.tomorrow()
        self.assertTrue(current.betweenIncluded(yesterday, tomorrow))
        self.assertTrue(current.betweenExcluded(yesterday, tomorrow))
        self.assertTrue(yesterday.betweenIncluded(yesterday, tomorrow))
        self.assertFalse(yesterday.betweenExcluded(yesterday, tomorrow))


if __name__ == '__main__':
    unittest.main()
