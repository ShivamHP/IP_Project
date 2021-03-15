#Libraries imported:
import matplotlib.pyplot as pl
import pandas as pd
import numpy as np


##This project is made by Shivam Pachchigar for the purpose of IP project for the 2020-2021 session.
##The data is taken from the website: https://prsindia.org/covid-19/cases


#Taking in csv file:
dfindia = pd.read_csv("COVID-19 Cases(15-03-2021).csv") #dfindia contains info of all over India


#Taking data from csv file:
def assign(df):
    date = df["Date"].to_numpy()
    confirmed_cases = df["Confirmed Cases"].to_numpy()
    active_cases = df["Active Cases"].to_numpy()
    cured = df["Cured/Discharged"].to_numpy()
    death = df["Death"].to_numpy()
    plotter(date, confirmed_cases, active_cases, cured, death)

#Plotting graph:      #I am going to call this in assign function.
def plotter(date, confirmed_cases, active_cases, cured, death):
    pl.plot(date, confirmed_cases)
    pl.xlabel("Date")
    pl.ylabel("Number of cases")
    pl.legend("Confirmed cases")
    pl.show()

assign(dfindia)
