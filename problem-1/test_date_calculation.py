import unittest

from freezegun import freeze_time

from date_calculation import next_draw


class TestDateCalculation(unittest.TestCase):
    def test_next_draw_in_weedsneday_with_specific_date(self):
        msg = next_draw('2017-05-23 12:00')
        self.assertEqual(msg, 'Next draw will be at: 24, May 2017 at 8:00PM')

    def test_next_draw_in_saturday_with_specific_date(self):
        msg = next_draw('2017-05-25 12:00')
        self.assertEqual(msg, 'Next draw will be at: 27, May 2017 at 8:00PM')

    @freeze_time('2016-05-23 12:00')
    def test_next_draw_basead_on_current_date(self):
        msg = next_draw()
        self.assertEqual(msg, 'Next draw will be at: 25, May 2016 at 8:00PM')

    def test_next_draw_in_the_same_day_before_time(self):
        msg = next_draw('2017-05-24 12:00')
        self.assertEqual(msg, 'Next draw will be at: 24, May 2017 at 8:00PM')

    def test_next_draw_in_the_same_day_after_time(self):
        msg = next_draw('2017-05-24 20:01')
        self.assertEqual(msg, 'Next draw will be at: 27, May 2017 at 8:00PM')
