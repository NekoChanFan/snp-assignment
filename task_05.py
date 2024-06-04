import datetime


def date_in_future(integer):
    if not isinstance(integer, int):
        return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    else:
        return (datetime.datetime.now() + datetime.timedelta(days=integer)).strftime("%d-%m-%Y %H:%M:%S")


if __name__ == "__main__":
    print(date_in_future([]))
    print(date_in_future(2))
