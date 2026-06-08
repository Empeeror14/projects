import datetime as dt
import random
import smtplib
import pandas as pd
import os



email = "ikehobi@gmail.com"
password = "adjt yxso cisu cukw"

now =dt.datetime.now()
today =now.weekday()

if today in [0,1,2,3,4,5,6]:
    
    contacts = pd.read_csv("/Users/victoriamadedor/Desktop/Stan's projects/Birthday Wisher (Day 32) start/contacts.csv")
    
    with open("/Users/victoriamadedor/Desktop/Stan's projects/Birthday Wisher (Day 32) start/quotes.txt") as data:
        all_quotes = data.readlines()
        random_quote = random.choice(all_quotes).strip()
        
    print(random_quote)
    
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        for index, row in contacts.iterrows():
            name = row["name"]
            recipient = row["email"]
            try:
                connection.sendmail(from_addr=email, to_addrs=recipient, msg= f"""
                                    Subject:Motivation for today\n\n
                                    Hi {name},\n\n
                                    {random_quote}
                                    Keep pushing forward and have a great day!
                                    Best regards,
                                Stan""")
                print(f"Email sent to {name}")
            except Exception as e:
                print(f"Failed to send email to {row['name']}: {e}")
        
    
    