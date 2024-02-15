## Table of Contents

  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Functionality](#functionality)
  - [Changes for Efficiency](#changes-for-efficiency)

## Introduction

The country wise data set consists of Covid-19 related data for countries all over the world. It contains the amount of confirmed cases, amount of deaths, and amount recovered. The aim of this code is to allow a user to input a country name and recieve a visual bar graph that shows the number of cases, number of deaths, and number recovered for that country. "No data available" will appear if that country is not in the data set.

## Requirements

- Python 3.x
- Matplotlib
- Pandas

## Installation 

Import myplotlib.pyplot as plt and import pandas as pandas.

## Usage

Download the COVID-19 dataset in CSV format and update the filepath variable in the script with the correct file path.

Use the file path to load the data set, which can be found using ls and cd functions in terminal. In this case, filepath = "/Users/parishah/Desktop/Python Projects/data/country_wise_latest.csv". 

**Run the script and enter the name of the country when prompted.**

## Functionality

The script defines a function plotdata that takes a country name and the COVID-19 dataset as parameters. It then checks if the provided country exists in the dataset and prints whether data is available or not. If data is available, it extracts and plots the number of confirmed cases, deaths, and recoveries for the specified country.

## Changes for Efficiency

If you plan to reuse this script with different datasets, consider parameterizing the file path or accepting it as a command-line argument. This makes the script more flexible.

```
import sys

def plotdata(country, data):
    # ... (rest of the code)

if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

filepath = sys.argv[1]
data = pandas.read_csv(filepath)

countryname = input("Enter a country name: ")
plotdata(countryname, data)
```
