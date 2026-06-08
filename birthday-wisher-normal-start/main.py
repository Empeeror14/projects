##################### Normal Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib



email = "ikehobi@gmail.com"
password = "adjt yxso cisu cukw"


# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_month = today.month
today_day = today.day
today_tuple = (today_month, today_day)


# HINT 2: Use pandas to read the birthdays.csv
data = pd.read_csv("/Users/victoriamadedor/Desktop/Stan's projects/birthday-wisher-normal-start/birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if (today_month,today_day) in birthdays_dict:
    birthday_person = birthdays_dict[(today_month, today_day)]
    print(birthday_person.name)
    print(birthday_person.email)    
    
    with open(f"/Users/victoriamadedor/Desktop/Stan's projects/birthday-wisher-normal-start/letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        letter_content = letter_file.read()
        letter_content = letter_content.replace("[NAME]", birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=birthday_person.email, msg=f"Subject:Happy Birthday\n\n{letter_content}")

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



