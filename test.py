import unittest

from converter import DateToTextTransformer


class TestsConversion(unittest.TestCase):

    def test_new_dates(self):
        transformer = DateToTextTransformer()
        self.assertEqual(transformer.transform("25.09.2019 08:17:59"),
                         "двадцать пятое сентября две тысячи девятнадцатого года восемь часов семнадцать минут пятьдесят девять секунд")
        self.assertEqual(transformer.transform("14.06.2000 00:05:00"),
                         "четырнадцатое июня двухтысячного года ноль часов пять минут ноль секунд")
        self.assertEqual(transformer.transform("01.01.2001 01:01:01"),
                         "первое января две тысячи первого года один час одна минута одна секунда")

    def test_old_dates(self):
        transformer = DateToTextTransformer()
        self.assertEqual(transformer.transform("12.12.1945 04:21:23"),
                         "двенадцатое декабря одна тысяча девятьсот сорок пятого года четыре часа двадцать одна минута двадцать три секунды")
        self.assertEqual(transformer.transform("01.08.1800 23:23:23"),
                         "первое августа одна тысяча восьмисотого года двадцать три часа двадцать три минуты двадцать три секунды")
        self.assertEqual(transformer.transform("10.11.1999 10:11:12"),
                         "десятое ноября одна тысяча девятьсот девяносто девятого года десять часов одиннадцать минут двенадцать секунд")