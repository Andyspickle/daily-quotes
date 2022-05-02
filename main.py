import random
import smtplib
import datetime as dt
from secret import USERNAME, PASSWORD


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs=USERNAME,
            msg=f"Subject: Today's Quote! \n\n {message}.",
        )


def get_daily_quote():
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
    return random.choice(quotes)


def main():
    now = dt.datetime.now()
    weekday = now.weekday()
    daily_quote = get_daily_quote()
    send_email(daily_quote)


if __name__ == "__main__":
    main()