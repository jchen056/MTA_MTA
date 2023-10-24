# MTA, at Your Service

## Ideation

We love MTA for its 24-7 and we hate it for its delays and crowded trains. With that being said, we want to leverage data to help MTA improve their services while generating profits.

## EDA

![](https://github.com/jchen056/MTA_MTA/blob/main/visualizations/time_spatial.gif)

- Understand complaints about MTA: commendation vs complaint ratio, major complaints(~~text analysis~~)
- Understand demands for public transportation based on days, hours, and geography: time series analysis and geos-spatial analysis

## ML

Build a ML model to predict demands

## Solution and its impact: Dynamic Pricing

- case studies: Washing DC and Shanghi & Beijing, China
- dynamic pricing
- impact

## Team Members

- [Jiale (Jerry) Chen](https://www.linkedin.com/in/jiale-jerry-chen/)
- [Nossaiba Kheiri](https://www.linkedin.com/in/nossaibakheiri/)
- [Yihan (Shane) Luo](https://www.linkedin.com/in/yihanluo1228/)
- [Sifan (Emily) Tao](https://www.linkedin.com/in/sifan-tao-58360b236/)
- [Yan (Felicity) Zhu](https://www.linkedin.com/in/yanzhu9/)

## Tools used

- [plotly](https://plotly.com/python/plotly-express/#overview)
- [bokeh](https://docs.bokeh.org/en/latest/docs/first_steps.html#first-steps)
- [folium](https://python-visualization.github.io/folium/latest/getting_started.html)

```
pip install bokeh
pip install folium
```

## Datasets

Due to their large size, some datasets are not included in our Github Repositoty. If you want to duplicate our work, please download data from the following websites:

1. [MTA Subway Hourly Ridership: Beginning February 2022](https://data.ny.gov/Transportation/MTA-Subway-Hourly-Ridership-Beginning-February-202/wujg-7c2s): this dataset provides subway ridership estimates on an hourly basis.
2. [Fare Card History for Metropolitan Transportation Authority (MTA)](https://data.ny.gov/Transportation/Fare-Card-History-for-Metropolitan-Transportation-/v7qc-gwpn): these files show the number of MetroCard swipes made each week by customers entering each station of the New York City Subway, PATH, AirTrain JFK and the Roosevelt Island Tram, broken out to show the relative popularity of the various types of MetroCards.
3. [MTA Customer Feedback Data](https://data.ny.gov/Transportation/MTA-Customer-Feedback-Data-Beginning-2014/tppa-s6t6):This dataset is generated from the Customer Relationship Management System. This system allows the public to correspond to the MTA about complaints or commendations in a variety of categories.
