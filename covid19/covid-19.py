#!/usr/bin/python3

from selenium import webdriver
import smtplib
from datetime import datetime, timedelta
from threading import Timer

class Covid19():
    def __init__(self):
        self.browser = webdriver.Firefox()

    def get_data(self):
        #try:
        self.browser.get('https://www.worldometers.info/coronavirus/')
        table = self.browser.find_element_by_xpath('//*[@id="main_table_countries_today"]')
        country = table.find_element_by_xpath("//td[contains(text(), 'Brazil')]")
        row = country.find_element_by_xpath("./..")
        data = row.text.split(' ')
        total_cases = data[1]
        new_cases = data[2]
        total_deaths = data[3]
        new_deaths = data[4]
        active_cases = data[5]
        total_recovered = data[6]
        serious_critical = data[7]
        cfr = str(float(total_deaths)/float(total_cases) * 100)

        print("Country: " + country.text)
        print("Total cases: " + total_cases)
        print("New cases: " + new_cases)
        print("Total deaths: " + total_deaths)
        print("New deaths: " + new_deaths)
        print("Active cases: " + active_cases)
        print("Total recovered: " + total_recovered)
        print("Serious, critical cases: " + serious_critical)
        print('CFR: '+ cfr)

        send_mail(country.text, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical, cfr)

        self.browser.close()
        #except:
        #    print('Data not found!')
        #    self.browser.quit()

def send_mail(country, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical, cfr):
    #with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp = smtplib.SMTP('smtp.gmail.com', 587)    
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('joaopadua@id.uff.br', 'ppmbqwivmhcojxyz')

    subject = 'Covid-19 numbers in Brazil today'

    body = 'Today in ' + country + '\
    \nThere is new data on coronavirus:\
    \nTotal cases: ' + total_cases +'\
    \nNew cases: ' + new_cases + '\
    \nTotal deaths: ' + total_deaths + '\
    \nNew deaths: ' + new_deaths + '\
    \nActive cases: ' + active_cases + '\
    \nTotal recovered: ' + total_recovered + '\
    \nSerious, critical cases: ' + serious_critical  + '\
    \nCFR: ' + cfr + '\
    \nCheck the link: https://www.worldometers.info/coronavirus/'

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail('Covid-19','joaopadua@id.uff.br', msg)
    smtp.quit()
    print('Hey, Email has been sent!')

bot = Covid19()
bot.get_data()

#x = datetime.today()
#y = x.replace(day=x.day, hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)
#delta_t = y-x
#secs = delta_t.seconds+1
#t = Timer(secs, bot.get_data())
#t.start()

