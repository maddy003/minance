# https: // www.nseindia.com / content / historical / EQUITIES / 2017 / MAY / cm05MAY2017bhav.csv.zip
# https://www.nseindia.com/content/historical/EQUITIES/{year}/{month in captial letters}/cm{date}{month in captial letters}{year}bhav.csv.zip

from datetime import date, timedelta
import time
import webbrowser
import os


def browser_close():
    os.system("killall -9 'Safari'")

def download(url):
    webbrowser.open(url, new=0, autoraise=True)


def start_year(current_year):
    return current_year - 1


def month_in_letters(month):
    switcher = {
        1: "JAN",
        2: "FEB",
        3: "MAR",
        4: "APR",
        5: "MAY",
        6: "JUN",
        7: "JUL",
        8: "AUG",
        9: "SEP",
        10: "OCT",
        11: "NOV",
        12: "DEC"
    }
    return switcher.get(month, "Invalid month")


def main():
    today = date.today()
    startyear = start_year(today.year)

    start_date = date(startyear, today.month, today.day)
    end_date = date(today.year, today.month, today.day)
    delta = timedelta(days=1)
    while start_date <= end_date:
        month = month_in_letters(start_date.month)
        year = str(start_date.year)
        if start_date.day < 10:
            day = "0" + str(start_date.day)
        else:
            day = str(start_date.day)

        url_string1 = "https://www.nseindia.com/content/historical/EQUITIES/"
        url_string2 = year + "/" + month + "/cm" + day + month + year + "bhav.csv.zip"
        url_string = url_string1 + url_string2
        download(url_string)
        time.sleep(.2)
        start_date += delta

    time.sleep(5)
    browser_close()


main()
