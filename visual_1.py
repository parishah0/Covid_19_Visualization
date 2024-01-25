import matplotlib.pyplot as plt
import pandas as pandas

filepath = "/Users/parishah/Desktop/Python Projects/data/country_wise_latest.csv"
data = pandas.read_csv (filepath)

def plotdata (country, opendata):

    #check if the country is in the excel sheet
    check_country=data[data["Country/Region"]==country]

    #check if that data is available for that country
    #pull the data based on country
    if check_country.empty:
        print('No data available')
        return
    else:
        print ('Data available')

    #splitting the data into these 3 categories (confirmed, deaths, and recovered)
    confirmed = check_country['Confirmed'].values[0]
    deaths = check_country['Deaths'].values[0]
    recovered = check_country['Recovered'].values[0]

    #actually plot it 
    categories = ['Confirmed', 'Deaths', 'Recovered']
    values = [confirmed, deaths, recovered]
    fig, ax = plt.subplots()
    ax.bar(categories, values, color=['blue', 'red', 'green'])
    ax.set_title('Country Covid 19 Health Status')
    ax.set_xlabel('Health Status')
    ax.set_ylabel("Amount")
    plt.show()

countryname = (input ("enter a country name"))
plotdata(countryname, data)