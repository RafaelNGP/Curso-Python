#
# Example file for working with date information
#
from datetime import date, time, datetime


def main():
    # DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is ", today)

    # print out the date's individual components
    print("Date components: ", today.day, today.month, today.year)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is: ", today.weekday())
    days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
    print("Which is a: ", days[today.weekday()])
    print()

    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    today_now = datetime.now()
    print("The current date and time is: ", today_now)

    # Get the current time
    t = datetime.time(today_now)
    print(t)

    # E para recuperar apenas o dia?
    print(f"Vamos la:\n"
          f"usando today: {today_now.today()}\n"
          f"usando now: {today_now.now()}\n"
          f"usando weekday: {today_now.weekday()}\n"
          f"usando time: {today_now.time()}\n"
          f"usando date(): {today_now.date()}\n"
          f"usando date day: {today_now.date().day}\n"
          f"usando date day extenso: {days[today_now.weekday()]}\n"
          f"usando date month: {today_now.date().month}\n"
          f"usando date year: {today_now.date().year}\n")


if __name__ == "__main__":
    main()
