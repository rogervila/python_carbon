import unittest
from datetime import datetime, timedelta
from python_carbon import Carbon


class test_python_carbon(unittest.TestCase):
    def test_parse_and_equality(self) -> None:
        dt = Carbon.parse('2021-08-16 01:02:03')
        dt2 = Carbon.parse('2021-08-16 01:02:03')

        self.assertTrue(dt.equalTo(dt2))

    def test_instantiation_now_and_constructor(self) -> None:
        dt = Carbon.now()
        self.assertIsInstance(dt, Carbon)

        dt = Carbon()  # equivalent to Carbon.now()
        self.assertIsInstance(dt, Carbon)

    def test_create_format_and_getters(self) -> None:
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

    def test_start_and_end_methods(self) -> None:
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

    def test_start_end_week_and_year_exact_values(self) -> None:
        dt = Carbon.parse('2021-08-18 14:15:16.123456')

        self.assertEqual(dt.startOfWeek().toDateTimeString(with_milliseconds=True), '2021-08-16 00:00:00.000000')
        self.assertEqual(dt.endOfWeek().toDateTimeString(with_milliseconds=True), '2021-08-22 23:59:59.999999')
        self.assertEqual(dt.startOfYear().toDateTimeString(with_milliseconds=True), '2021-01-01 00:00:00.000000')
        self.assertEqual(dt.endOfYear().toDateTimeString(with_milliseconds=True), '2021-12-31 23:59:59.999999')

        sunday = Carbon.parse('2021-08-22 10:00:00')
        self.assertEqual(sunday.startOfWeek().toDateTimeString(), '2021-08-16 00:00:00')
        self.assertEqual(sunday.endOfWeek().toDateTimeString(), '2021-08-22 23:59:59')

    def test_add_sub_and_last_day_of_month(self) -> None:
        self.assertTrue(Carbon.parse('2021-08-31').isLastDayOfMonth())

        anchor = Carbon.now()
        self.assertTrue(anchor.addYears(10).equalTo(anchor.add(10, 'years')))
        self.assertTrue(anchor.subYears(10).equalTo(anchor.sub(10, 'years')))

        self.assertIsInstance(Carbon.timedelta(days=1), timedelta)

    def test_difference_and_diffin_methods(self) -> None:
        earlier = Carbon.parse('2021-01-01 00:00:00.000000')
        later = Carbon.parse('2022-03-04 05:06:07.123456')

        diff = later.difference(earlier)
        self.assertIsInstance(diff, dict)
        self.assertEqual(
            set(diff.keys()),
            {'years', 'months', 'days', 'leapdays', 'hours', 'minutes', 'seconds', 'microseconds'}
        )
        self.assertEqual(diff['years'], 1)
        self.assertEqual(diff['months'], 2)
        self.assertEqual(diff['days'], 3)
        self.assertEqual(diff['hours'], 5)
        self.assertEqual(diff['minutes'], 6)
        self.assertEqual(diff['seconds'], 7)
        self.assertEqual(diff['microseconds'], 123456)

        expected_seconds = (datetime(2022, 3, 4, 5, 6, 7, 123456) - datetime(2021, 1, 1, 0, 0, 0, 0)).total_seconds()
        expected_minutes = expected_seconds / 60
        expected_hours = expected_seconds / 3600
        expected_days = expected_seconds / 86400
        expected_weeks = expected_days / 7
        expected_microseconds = int(round(expected_seconds * 1_000_000))

        diff_years = later.diffIn('years', earlier)
        diff_months = later.diffIn('months', earlier)
        diff_weeks = later.diffIn('weeks', earlier)
        diff_days = later.diffIn('days', earlier)
        diff_hours = later.diffIn('hours', earlier)
        diff_minutes = later.diffIn('minutes', earlier)
        diff_seconds = later.diffIn('seconds', earlier)
        diff_microseconds = later.diffIn('microseconds', earlier)

        self.assertIsInstance(diff_years, int)
        self.assertIsInstance(diff_months, int)
        self.assertIsInstance(diff_weeks, float)
        self.assertIsInstance(diff_days, float)
        self.assertIsInstance(diff_hours, float)
        self.assertIsInstance(diff_minutes, float)
        self.assertIsInstance(diff_seconds, float)
        self.assertIsInstance(diff_microseconds, int)

        self.assertEqual(diff_years, 1)
        self.assertEqual(diff_months, 14)
        self.assertAlmostEqual(diff_weeks, expected_weeks, places=12)
        self.assertAlmostEqual(diff_days, expected_days, places=12)
        self.assertAlmostEqual(diff_hours, expected_hours, places=12)
        self.assertAlmostEqual(diff_minutes, expected_minutes, places=12)
        self.assertAlmostEqual(diff_seconds, expected_seconds, places=12)
        self.assertEqual(diff_microseconds, expected_microseconds)

    def test_cookie_iso_and_calendar_methods(self) -> None:
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

    def test_start_end_of_month_year_and_quarters(self) -> None:
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

    def test_between_included_and_excluded(self) -> None:
        current = Carbon.now()
        yesterday = Carbon.yesterday()
        tomorrow = Carbon.tomorrow()

        self.assertTrue(current.betweenIncluded(yesterday, tomorrow))
        self.assertTrue(current.betweenExcluded(yesterday, tomorrow))
        self.assertTrue(yesterday.betweenIncluded(yesterday, tomorrow))
        self.assertFalse(yesterday.betweenExcluded(yesterday, tomorrow))

    def test_utc_converter(self) -> None:
        local_with_offset = Carbon.parse('2021-08-18T10:00:00+02:00')
        converted = local_with_offset.utc()

        self.assertIsInstance(converted, Carbon)
        self.assertEqual(converted.toDatetime().tzname(), 'UTC')
        self.assertEqual(converted.toDateTimeString(), '2021-08-18 08:00:00')


if __name__ == '__main__':
    unittest.main()
