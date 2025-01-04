import datetime
import smtplib
import random
import pandas
import LunarSolar
import os

SENDER = os.environ.get("SENDER")
PASSWORD = os.environ.get("PASSWORD")
RECEIVER1 = os.environ.get("RECEIVER1")
RECEIVER2 = os.environ.get("RECEIVER2")


now = datetime.datetime.now()
solar_day = now.day
solar_month = now.month
solar_year = now.year

lunar = LunarSolar.solar_to_lunar(solar_day,solar_month,solar_year)
lunar_day = lunar[0]
lunar_month = lunar[1]

email_sent = False
data = pandas.read_csv("ancestor.csv")
for index,row in data.iterrows():
    if lunar_day == row.day and lunar_month == row.month:
        email_sent = True
        chosen_name = row.person

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER, password=PASSWORD)
            if row.day - int(lunar_day) !=0:
                connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER1, msg=f"Subject:Thong Bao Ngay GIo Cu {chosen_name}\n\nCon {row.day - int(lunar_day)} Ngay Nua La Toi Ngay GIo Cua Cu {chosen_name}. \nMong Moi Nguoi Kip Chuan Bi Day Du!")
                connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER2,
                                    msg=f"Subject:Thong Bao Ngay Gio Cu {chosen_name}\n\nCon {row.day - int(lunar_day)} Ngay Nua La Toi Ngay Gio Cua Cu {chosen_name}. \nMong Moi Nguoi Kip Chuan Bi Day Du!")
            else:
                connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER1, msg=f"Subject:Thong Bao Ngay Gio Cu {chosen_name}\n\nHom Nay La Ngay GIo Cua Cu {chosen_name}. \nMong Moi Nguoi Kip Chuan Bi Day Du!")
                connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER2,
                                    msg=f"Subject:Thong Bao Ngay Gio Cu {chosen_name}\n\nHom Nay La Ngay Gio Cua Cu {chosen_name}. \nMong Moi Nguoi Kip Chuan Bi Day Du!")


if email_sent:
    print("Email sent")
else:
    print("No email sent")