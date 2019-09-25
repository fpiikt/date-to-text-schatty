"""
  Author: Kuznetsov Igor, P3355
"""

from name_data import months_names, month_date_names, times_minute_names, \
    times_hours_names, years_ending_names, hundreds_names, hundreds_names_standalone


class DateToTextTransformer(object):
    def __init__(self):
        pass

    def transform(self, date):
        """
        Transforms date in numerical format into russian next.

        Args:
            date (str): for example 25.09.2019 08:17:59

        Returns (str): russian text
        """
        date_str, time_str = date.split(" ")
        dd, MM, yy = list(map(int, date_str.split(".")))
        hh, mm, ss = list(map(int, time_str.split(":")))

        s = f"{month_date_names[dd]} {months_names[MM]} {self._year2text(yy)} года" \
            f" {times_hours_names[hh]} час{self._hour_postfix(hh)} " \
            f"{times_minute_names[mm]} минут{self._second_minute_postfix(mm)} " \
            f"{times_minute_names[ss]} секунд{self._second_minute_postfix(ss)}"

        return s.strip()

    def _hour_postfix(self, hh):
        if hh % 10 in [2, 3, 4]:
            return "а"
        if hh % 10 in [0, 5, 6, 7, 8, 9]:
            return "ов"
        return ""

    def _second_minute_postfix(self, mm):
        if mm % 10 == 1 and mm != 11:
            return "а"
        if mm % 10 in [2, 3, 4] and mm//10 != 1:
            return "ы"
        return ""

    def _year2text(self, yy):
        s = ""

        # Edge case
        if yy == 2000:
            return "двухтысячного"

        if yy // 1000 == 1:
            s += "одна тысяча "
            if yy % 100 == 0:
                print(yy%1000//100)
                s += hundreds_names_standalone[yy%1000//100]
            else:
                s += hundreds_names[yy%1000//100] + " "
        else:
            s += "две тысячи "

        if yy%100 != 0:
            s += years_ending_names[yy%100]
        return s


if __name__ == "__main__":
    transormer = DateToTextTransformer()

    s = "25.09.2019 08:17:59"
    text = transormer.transform(s)
    print(text)