#!/usr/bin/env python
# coding: utf-8

# ![Cover1.jpg](attachment:Cover1.jpg)

# ![Cover3.jpg](attachment:Cover3.jpg)

# ![cover2.jpg](attachment:cover2.jpg)

# ## Question/ Problem We’re Addressing
# Beginning in the 1950s, scholars have reflected on the lack of development in low and middle-income countries. This correlation between lower income and slower growth was originally suspected to be a factor of path dependence, where a lack of wealth in the 1800s and 1900s could lead to a lack of growth in the 21st century. However, the 1980s demonstrated that lower-income countries CAN experience rapid economic growth, by a factor of more than 10% per year. In particular, the “miracle growth” countries like China, Korea, and Japan, categorized as countries with sustained economic growth of more than 6% per year, inspired further research. Still, the majority of low-income nations remained low-income. Some glaring exceptions also stood out: countries endowed with natural resources which should catalyze growth and integration into the international economy. Often, the results were counterintuitive to logic. These countries, endowed with oil, natural gas, and other high-value-added resources, experienced slower economic growth than their high-income counterparts and their low-income neighbors. In 1993, Richard Auty coined the term *resource curse* to describe this phenomenon of lower economic growth in resource-abundant countries. 

# The resource curse was inspired by another similar phenomenon, the Dutch disease. The Dutch disease suggests that increased exports of natural resources instigated a decline in national production competitiveness and created conditions for recessions. Growing natural resource markets often correlate to weakened export markets of goods and services because tradable goods become less competitive as the country becomes less specialized in its non-resource goods. Particularly for countries in the fuel industry, these changes in specialization influence how competitive countries are in the international and create unfavorable conditions for economic growth. The resource curse expands this phenomenon to include economic stagnation and stunting of growth in sectors outside of the export market. 
#     
# Our research aims to investigate this exact topic: *How does the resource curse affect low-income economies and do natural resources induce economic stagnation?*

# ## Relevance
# In 2012, the International Monetary Fund (IMF) categorized 51 nations as “resource-rich,” which account for a population of more than a billion people. A majority of these nations showed exhaustible natural resources account for at least 20% of fiscal revenue or 20% of exports. 29 of these nations have incomes that are low or lower middle class (Venables, 16). The 29 nations share the following traits: heavy reliance on natural resource wealth for taxation, exports, or both, inadequate savings rates, subpar economic performance, and highly variable resource income. 
# 
# Resources account for one of the world’s largest sectors, accounting for nearly 20% of global production. The growing influence of oil and natural gas in recent decades also increased the influence of the resources market. However, with the growing influence of green energies and increased awareness of the dangers of mineral mining, there are increasing pressures to limit the natural resource industries. Moving into the future, shifts towards renewable energy sources could threaten the already rocky stability of resource markets. Understanding the potential influences in these markets can improve their transition into new markets and avoid the negative consequences of market shifts. 

# ![AD565699-.png](attachment:AD565699-.png)

# ## Explanation of Variables
# 1) Export Centralization \
# 	As a factor of the Dutch disease, a competitive advantage in natural resources prevents development in other export industries. The “competitive hypothesis” of the resource curse argues that specialization in the resource industry can subdue growth in more diversified and stable industries, thus preventing the overall growth of the economy (Mershed and Serino, 152). In the long term, the oversaturation of the labor market can create wage stagnation, lower GDP per capita, and lower standards of living. This combination of hyperspecialized industries and low wages can subdue economic growth, even when prices for natural resources are high. \
#     For this section, we will be observing what percent of the economy is employed by the natural resource industry by observing export percentages and the strucutre of the market. We will also be comparing natural resource rents to GDP per capita. If increased exports in the resource industries is negatively correlated with economic growth, this data would suggest that natural resources are detrimental to economic growth. 

# 2) Volatility of prices \
# 	Most natural resources are roughly price inelastic on the supply and demand side, making the market highly vulnerable to small price changes. Changes in demand or supply shocks of all kinds can create large swings in prices that affect the market rapidly. As Michael Ross highlights, “the price of oil is more volatile than the price of 95 percent of all products sold in the United States,” making energy resources and other natural resources dangerous investments (Ross, 50). When governments rely on these revenues, economic growth is highly dependent on international prices. If prices dip, as they did in 2020 during the COVID pandemic, unexpected changes can create detrimental setbacks in growth. Goods and services are much less volatile, making them safer investments for growth. Resource-rich countries are therefore at the mercy of the international market for economic revenue and growth. \
#     We will tracking the trend lines between prices of oil and other nautral resources and economic growth. A positive correlation would indicate that economic growth is reliant on export prices. Thus, the volatility of the prices would be an impediment to economic growth.     
#     

# 3) Resource Rent Revenues \
# 	Overwhelmingly, a positive correlation exists between resource endowment and the size of government. These larger governments are also disproportionately dependent on revenues from natural resources, relying less on taxes than their resource-poor counterparts (Ross, 29). These disproportionately large governments rely on resource revenues and often fail to stabilize their economies due to shorter time horizons. The alternating periods of high prices tend to correlate with faster growth whereas low prices are associated with poor budgeting and high expenditures. Thus, governmental rents from resources can reveal where money is wasted or spent on consumption rather than investment.\
#     We will observe the trends between the size of government and economic growth. If there is a negative correlation, it would imply that government rents are detrimental to economic growth. 

# ## DAG
# ![image.png](attachment:image.png)

# ## Data 
# The data necessary to assess our argument is compiled into six essential pieces of data: 
# 1) Statistics of resource endowment, detailing which resource each country has and the percent of exports 
# 
# 2) GDP growth (and reductions) since exporting natural resources 
# 
# 3) GDP per capita growth (and reductions) since exporting natural resources 
# 
# 4) Prices of the natural resources before and after exportation 
# 
# 5) Government rents from natural resources and their factor of total GDP/production 
# 
# 6) Exports and Natural Resource Exports as a percentage of Total GDP

# These six factors will demonstrate how the exchange of natural resources has changed in recent years and how developing economies have responded. As outlined above, our goal is to compare the data on the total production of natural resources to GDP per capita and total GDP growth to measure whether correlations exist between the two variables. The prices of the resources and the government rents will serve as control variables, to test whether extreme variation in GDP comes from internal or external factors. Due to a large number of confounding variables, we chose two external factors (price and government rents) to measure internal and external pressure on the market at all times. 
# 
# Ultimately, these variables will address the factors of economic growth and demonstrate how resource-rich countries are at a unique disadvantage: despite an ingrained source for wealth, the countries are failing to develop or to grow. 

# ### Source of the Data
# 
# Most of our data can be sources from either OEC, the IMF, and the World Bank. However, some data is incomplete or unreliable. By using international market price and reported government rents of minerals, we hope to limit the effect of unreliable information. 

# ### Goals of Analysis 
# 
# With our data, we intend to demonstrate four main correlations. 

# 1) Demonstrate a correlation between the percent of natural resource of exports and negative (OR neutral) GDP growth 
# 
# Economic logic suggests that increase exports is linked to GDP growth. Therefore, a negative or neutral correlation between GDP growth and natural resource exports would illustrate some negative pressure from natural resources on GDP. 
# 
# We plan to run regression to determine a correlation between natural resources as a percent of exports and GDP growth both average for countries and over time. We will also run a correlation between exports and GDP per capita growth. Ideally, both will demonstrate that peaks of prices are correlated with dips in GDP (and GDPPC) growth. 

# 2) Demonstrating negative (OR neutral) correlation between price of natural resources and GDP per capita growth 
# 
# Again, economic logic would suggest that increasing GDP and increased natural resources exports would benefit the country's population. A negative or neutral correlation suggests that the increased revenues do not go to the people, but go somewhere else. If GDPPC is stagnant, this suggests limited development and growth. 
# 
# We plan to run regression between prices of natural resources and GDP growth, as well as a regression for prices and GDP per capita growth. A negative correlation for both would support our hypothesis. 

# 3) Illustrating a correlation between natural resources as a percent of exports and government rents 
# 
# Given that natural resource have a negative pressure on GDP growth and GDPPC is stagnant, where does that extra income go? Demonstrating a correlation between natural resource dependence and rents will illustrate that in some way, governments benefit from increase prices rather than the people. Therefore, government rents would be detrimental to development and growth. 
# 
# We plan to run regressions between prices of natural resources and government rent growth, as well as a regression for resource endowment as a percentage of exports and rent growth. It is crucially import to note that we plan to use region as a control variable for these regressions. Regions that are more authoritarian than others (like the Middle East) will naturally have higher resource rents than democratic regions (like Europe or Africa). However, all regions should show negative trends. Therefore, by keeping region as a control variable, we will ensure that no data is skewed by government type or regional diversity. 

# and lastly,
# 
# 4) Illustrating the general correlation between high resource endowment and GDP growth over time 
# 
# Using the data compiled previously, we hope to illustrate how resource endowment has an overwhelmingly negative impact of GDP growth and GDPPC growth. These variables demonstrate the various factors of the economy which are influenced by resource endowment and those which are negatively impacted. 
# 
# 
# Our outputs will be linear regression dynamic models and several R2 data analyses. Particularly for regressions over time, we intend to use linear regressions to show correlations between variables. 

# <div class="alert alert-block alert-warning">
#     <b> Country Selection </b> 
# 
# We chose our countries from the IMF(2012) Data set. These countries were chosen as "resource-rich" as natural resources account for 20%+ of exports or 20%+ of fiscal revenue. 
#     

# This data set is organized by GNI per capita from lowest to highest. We excluded the rising natural resource exporters due to a lack of reliable information across several data banks. Information not included in the IMF Data Set was acquired through OEC data banks. \
# Based on some of our preliminary regression, some countries are still missing information despite using multiple resources. For the final project, we hope to find some of the missing data. Otherwise, we will note which countries are missing. We speculate the some of the missing data is either due to government secrecy or inaccessibility to information in smaller or more authoritarian countries. 

# In[381]:


#Importing
# Basic Packages
from __future__ import division
import os
from datetime import datetime

# Web & file access
import requests
import io

# Import display options for showing websites
from IPython.display import IFrame, HTML
# Plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

get_ipython().run_line_magic('pylab', '--no-import-all')
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set_context("talk")

import plotly.express as px
import plotly.graph_objects as go

from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap

# Data
import pandas as pd
import numpy as np
from pandas_datareader import data, wb

# GIS & maps
import geopandas as gpd
gp = gpd
import georasters as gr
import geoplot as gplt
import geoplot.crs as gcrs
import mapclassify as mc
import textwrap
import statsmodels.api as sm
from stargazer.stargazer import Stargazer, LineLocation

# Data Munging
from itertools import product, combinations
import difflib
import pycountry
import geocoder
from geonamescache.mappers import country
mapper = country(from_key='name', to_key='iso3')
mapper2 = country(from_key='iso3', to_key='iso')
mapper3 = country(from_key='iso3', to_key='name')

# Regressions & Stats
from scipy.stats import norm
import statsmodels.formula.api as smf


# In[382]:


countryprelimdata = (['Congo, Dem. Rep', 'COD', 'Minerals & Oil', 94, 'Dependent'],
                     ['Liberia', 'LBR', 'Gold/Iron Ore', 35, 'Medium'],
                     ['Niger', 'NER', 'Gold/Oil/Uranium', 79, 'Dependent'],
                     ['Guinea', 'GIN', 'Mining Products', 93, 'Dependent'],
                     ['Mali', 'MLI', 'Gold', 75, 'High'],
                     ['Chad', 'TCD', 'Oil', 89, 'Dependent'],
                     ['Mauritania', 'MRT', 'Iron Ore', 24, 'Medium'],
                     ['Lao PDR', 'LAO', 'Copper & Gold', 57, 'High'],
                     ['Zambia', 'ZMB', 'Copper', 72, 'High'],
                     ['Vietnam', 'VNM', 'Oil', 14, 'Low'],
                     ['Yemen', 'YEM', 'Oil', 82, 'Dependent'],
                     ['Nigeria', 'NGA', 'Oil', 97, 'Dependent'],
                     ['Cameroon', 'CMR', 'Oil', 47, 'Medium'],
                     ['Papua New Guinea', 'PNG', 'Oil/Copper/Gold', 77, 'Dependent'],
                     ['Sudan', 'SDN', 'Oil', 97, 'Dependent'],
                     ['Uzbekistan', 'UZB', 'Gold/Oil', 54, 'High'],
                     ['Cote d\'Ivoire', 'CIV', 'Oil/Gold', 17, 'Low'],
                     ['Bolivia', 'BOL', 'Oil', 74, 'High'],
                     ['Mongolia', 'MNG', 'Copper', 81, 'Dependent'],
                     ['Congo, Rep. of', 'COG', 'Oil', 90, 'Dependent'],
                     ['Iraq', 'IRQ', 'Oil', 99, 'Dependent'],
                     ['Indonesia', 'IDN', 'Oil', 10, 'Low'],
                     ['Timor Leste', 'TLS', 'Oil', 99, 'Dependent'],
                     ['Syrian Arab Republic', 'SYR', 'Oil', 36, 'Medium'],
                     ['Guyana', 'GUY', 'Gold & Bauxite', 42, 'Medium'],
                     ['Turkmenistan', 'TKM', 'Oil', 91, 'Dependent'],
                     ['Angola', 'AGO', 'Oil', 95, 'Dependent'],
                     ['Gabon', 'GAB', 'Oil', 83, 'Dependent'],
                     ['Equatorial Guinea', 'GNQ', 'Oil', 99, 'Dependent'],
                     ['Ecuador', 'ECU', 'Oil', 55, 'High'],
                     ['Albania', 'ALB', 'Oil', 10, 'Low'],
                     ['Algeria', 'DZA', 'Oil', 98, 'Dependent'],
                     ['South Africa', 'ZAF', 'Minerals', 55, 'High'],
                     ['Iran', 'AZE', 'Oil', 94, 'Dependent'],
                     ['Peru', 'PER', 'Minerals', 48, 'Medium'],
                     ['Brazil', 'BRA', 'Oil/Iron', 26, 'Low'],
                     ['Azerbaijan', 'AZE', 'Oil', 94, 'Dependent'],
                     ['Botswana', 'BWA', 'Diamonds', 66, 'High'],
                     ['Kazakhstan', 'KAZ', 'Oil', 60, 'High'],
                     ['Suriname', 'SUR', 'Minerals', 11, 'Low'],
                     ['Mexico', 'MEX', 'Oil', 15, 'Low'],
                     ['Russia', 'RUS', 'Oil/Minerals', 61, 'High'],
                     ['Chile', 'CHL', 'Copper', 53, 'High'],
                     ['Venezuela', 'VEN', 'Oil', 93, 'Dependent'],
                     ['Libya', 'LBY', 'Oil', 97, 'Dependent'],
                     ['Bahrain', 'BHR', 'Oil', 96, 'Dependent'],
                     ['Brunei Darussalam', 'BRN', 'Oil', 87, 'Dependent'],
                     ['Trinidad and Tobago', 'TTO', 'Oil', 38, 'Medium'],
                     ['Saudi Arabia', 'SAU', 'Oil', 87, 'Dependent'],
                     ['Oman', 'OMN', 'Oil', 73, 'High'],
                     ['United Arab Emirates', 'UAE', 'Oil', 41, 'Medium'],
                     ['Qatar', 'QAT', 'Oil', 88, 'Dependent'],
                     ['Norway', 'NOR', 'Oil', 62, 'High'])                             

cpd = pd.DataFrame(countryprelimdata, columns=['Country Name', 'iso3c', 'Exports', 'NR_TE', 'Dependence_Deg'])
#NR_TE represents natural resources as a percentage of total exports


# In[383]:


# our list of countries and their primary exports
cpd


# <div class="alert alert-block alert-warning">
#     <b>Compilation of Data</b> Combining the IMF and OEC data set with the WDI data

# In[384]:


# Paths
pathout = './data/'

if not os.path.exists(pathout):
    os.mkdir(pathout)
    
pathgraphs = './graphs/'
if not os.path.exists(pathgraphs):
    os.mkdir(pathgraphs)


# In[385]:


currentYear = datetime.now().year
year = min(2020, currentYear-2)


# In[386]:


wbcountries = wb.get_countries()
wbcountries = wbcountries.loc[wbcountries.region.isin(['Aggregates'])==False].reset_index(drop=True)
wbcountries['name'] = wbcountries.name.str.strip()
wbcountries['incomeLevel'] = wbcountries['incomeLevel'].str.title()
wbcountries.loc[wbcountries.iso3c=='VEN', 'incomeLevel'] = 'Upper Middle Income'


# In[387]:


wdi_indicators = ['NY.GDP.MKTP.KD.ZG', 'NY.GDP.PCAP.KD.ZG', 'NY.GDP.PETR.RT.ZS', 'NE.EXP.GNFS.ZS', 'NY.GDP.TOTL.RT.ZS', 'NY.GDP.PCAP.PP.KD', 'EP.PMP.SGAS.CD']


# In[388]:


pop_vars = wb.search(string='population')
pop_vars.head()


# In[389]:


wdi = wb.download(indicator=wdi_indicators, country=wbcountries.iso2c.values, start=1950, end=year)
wdi = wdi.reset_index()
wdi['year'] = wdi.year.astype(int)
#GDP Per Capita
wdi['gdp_pc'] = wdi['NY.GDP.PCAP.PP.KD']
wdi['ln_gdppc']= wdi['gdp_pc'].apply(np.log)
#GDP growth annually
wdi['GDP_grow'] = wdi['NY.GDP.MKTP.KD.ZG']
wdi['ln_GDP_grow'] = wdi['NY.GDP.MKTP.KD.ZG'].apply(np.log)
#GPD Per Capita growth annually
wdi['GDPPC_grow'] = wdi['NY.GDP.PCAP.KD.ZG']
#Oil Rents as a percentage of GDP
wdi['OR'] = wdi['NY.GDP.PETR.RT.ZS']
wdi['ln_OR'] = wdi['OR'].apply(np.log)
#Natural resource rents as a percentage of GDP
wdi['NRR'] = wdi['NY.GDP.TOTL.RT.ZS']
wdi['ln_NRR']=wdi['NY.GDP.TOTL.RT.ZS'].apply(np.log)
#Exports as a percentage of GDP
wdi['Exports_TR'] = wdi['NE.EXP.GNFS.ZS']
#Price of Oil
wdi['POil'] = wdi['EP.PMP.SGAS.CD']
wdi['POil_chg']=wdi['POil'].pct_change()

wdi


# In[390]:


wdi = wbcountries.merge(wdi, left_on='name', right_on='country')
wdi


# In[391]:


# merging data to create one complete data set
compdat = cpd.merge(wdi, how="inner", on=["iso3c"])
compdat = compdat.drop(['iso2c', 'adminregion', 'NY.GDP.MKTP.KD.ZG',
                        'NY.GDP.PCAP.KD.ZG', 'NY.GDP.PETR.RT.ZS', 'NE.EXP.GNFS.ZS', 'NY.GDP.TOTL.RT.ZS', 
                        'latitude', 'longitude', 'name', 'capitalCity', 'lendingType', 'country', 
                        'NY.GDP.PCAP.PP.KD', 'EP.PMP.SGAS.CD'], axis=1)


# In[392]:


compdat.loc[compdat.year==2015].count()


# In[393]:


compdat.dtypes


# In[394]:


compdat


# In[395]:


#Oil Specific Data - focuses on countries with oil rents greater than 5%
oildat = cpd.merge(wdi, how="inner", on=["iso3c"])
oildat = oildat.drop(['iso2c', 'adminregion', 'NY.GDP.MKTP.KD.ZG',
                        'NY.GDP.PCAP.KD.ZG', 'NY.GDP.PETR.RT.ZS', 'NE.EXP.GNFS.ZS', 'NY.GDP.TOTL.RT.ZS', 
                        'latitude', 'longitude', 'name', 'capitalCity', 'lendingType', 'country', 
                        'NY.GDP.PCAP.PP.KD', 'EP.PMP.SGAS.CD'], axis=1)
oildat = oildat[oildat.OR > 1]
oildat


# ## Data Analysis:Regressions and Correlations Between Variables

# *Note:* Some of the data is questionable. For example, the GDP growth of Guyana is averaged at 40% and Brunei has a GDPPC higher than both Norway and the United States. When necessary, this data is emphasized as outliers. Otherwise, the data is assumed to be reliable. 
# 
# Also, each dynamic chart has a png copy beneath it for ease of reading when using the html file. 

# <div class="alert alert-block alert-warning">
# <b>Exports and GDP growth:</b>  
#     Illustrating the resource curse for both GDP and GDPPC growth

# In[396]:


dffig = compdat.loc[compdat.year==year]\
            .dropna(subset=['NR_TE', 'GDP_grow', 'gdp_pc'])\
            .sort_values(by='region').reset_index()
mod = smf.ols(formula='NR_TE ~ GDP_grow', data=dffig, missing='drop').fit()
mod.summary2()


# In[397]:


dffig2 = oildat.loc[oildat.year==year]\
            .dropna(subset=['NR_TE', 'GDP_grow', 'gdp_pc', 'OR'])\
            .sort_values(by='region').reset_index()
mod = smf.ols(formula='NR_TE ~ GDP_grow', data=dffig2, missing='drop').fit()
mod.summary2()


# Between these two data analysis, we can see that natural resources as a percent of total exports has a nul negative effect on resource rich countries in general (the slope is negative but p>.6). However, for oil rich countries, there is a negative correlation of natural resources on GDP growth. The slope is -.8 and the p value is <.005. This means there is a significant negative effect of oil exports on GDP growth. However, the data only explains about 40% of the data (R^2=.387). We will look further into the data to find other sources for a negative correlation. 

# In[398]:


symbols = ['circle', 'x', 'square', 'cross', 'diamond', 'star-diamond', 'triangle-up']
fig1 = px.scatter(dffig,
                 x="Exports_TR", 
                 y="GDP_grow", 
                 color='region',
                 symbol='region',
                 symbol_sequence=symbols,
                 hover_name='Country Name',
                 hover_data=['iso3c', 'Exports_TR', 'GDP_grow'],
                 size='gdp_pc',
                 size_max=20,
                 trendline="ols",
                 trendline_scope="overall",
                 trendline_color_override="black",
                 labels={
                     "Exports_TR": "Total Exports as a Percentage of GDP",
                     "GDP_grow": "GDP Growth",
                     "region": "WB Region",
                     "gdp_pc": "GDP Per Capita"
                 },
                 opacity=0.75,
                 height=800,
                )


# In[399]:


fig1.show()


# ![TotalExportsVSgdpgrowth.png](attachment:TotalExportsVSgdpgrowth.png)

# In[400]:


symbols = ['circle', 'x', 'square', 'cross', 'diamond', 'star-diamond', 'triangle-up']
fig2 = px.scatter(dffig,
                 x="NR_TE", 
                 y="GDP_grow", 
                 color='region',
                 symbol='region',
                 symbol_sequence=symbols,
                 hover_name='Country Name',
                 hover_data=['iso3c', 'NR_TE', 'GDP_grow'],
                 size='gdp_pc',
                 size_max=20,
                 trendline="ols",
                 trendline_scope="overall",
                 trendline_color_override="black",
                 labels={
                     "NR_TE": "Natural Resources as a Percentage of Total Exports",
                     "GDP_grow": "GDP Growth",
                     "region": "WB Region",
                     "gdp_pc": "GDP Per Capita"
                 },
                 opacity=0.75,
                 height=600,
                )


# In[401]:


fig2.show()


# ![NR_TEvsGDP_grow.png](attachment:NR_TEvsGDP_grow.png)

# In[402]:


symbols = ['circle', 'x', 'square', 'cross', 'diamond', 'star-diamond', 'triangle-up']
fig3 = px.scatter(dffig,
                 x="Exports_TR", 
                 y="GDPPC_grow", 
                 color='region',
                 symbol='region',
                 symbol_sequence=symbols,
                 hover_name='Country Name',
                 hover_data=['iso3c', 'Exports_TR', 'gdp_pc', 'GDPPC_grow'],
                 size='gdp_pc',
                 size_max=20,
                 trendline="ols",
                 trendline_scope="overall",
                 trendline_color_override="black",
                 labels={
                     "Exports_TR": "Total Exports as a Percentage of GDP",
                     "GDPPC_grow": "GDP Per Capita Growth",
                     "region": "WB Region",
                     "gdp_pc": "GDP Per Capita"
                 },
                 opacity=0.75,
                 height=600,
                )


# In[403]:


fig3.show()


# ![ExportsVSGDPPC_grow.png](attachment:ExportsVSGDPPC_grow.png)

# In[404]:


symbols = ['circle', 'x', 'square', 'cross', 'diamond', 'star-diamond', 'triangle-up']
fig4 = px.scatter(dffig,
                 x="NR_TE", 
                 y="GDPPC_grow", 
                 color='region',
                 symbol='region',
                 symbol_sequence=symbols,
                 hover_name='Country Name',
                 hover_data=['iso3c', 'NR_TE', 'GDPPC_grow', 'gdp_pc'],
                 size='gdp_pc',
                 size_max=20,
                 trendline="ols",
                 trendline_scope="overall",
                 trendline_color_override="black",
                 labels={
                     "GDPPC_grow" : 'GDP Per Capita Growth',
                     "NR_TE": "Natural Resources as a Percentage of Total Exports",
                     "GDP_grow": "GDP Growth",
                     "region": "WB Region",
                     "gdp_pc": "GDP Per Capita"
                 },
                 opacity=0.75,
                 height=800,
                )


# In[405]:


fig4.show()


# ![NR_TEvsGDP_grow.png](attachment:NR_TEvsGDP_grow.png)

# #### Analysis: 
# 
# These two graphs are crucial to demonstrate how natural resources have a negative effect on GDP growth. Fig1 shows how exports are *positively* correlated with GDP; countries with higher export levels also have higher GDP growth. Fig2 demonstrates a unique caveat: natural resources are NOT positively correlated with GDP growth. Fig2 even suggests the opposite, as natural resource exports increase, GDP growth decreases. Even excluding some extreme outliers (like Guyana with GDP growth +43% avg and Libya with GDP growth -23% avg), there is a slight negative correlation between natural resource exports and GDP growth. 
# 
# GDP per capita shows similar trends. As *total* exports increase, GDP per capita saw a slight increase. However, as natural resources exports increase, GDP per capita growth turns to a slight decrease. The visible differences between fig3 and fig 4 show that nautral resources have a negative effect on GDP growth. 

# It is also important to note that region plays a role in these effects. African and Middle Eastern countries are more negatively affected by resources, as they can be scattered around the OLS line for total exports, but as natural resource export increase, these two regions rank below the OLS. European countries are the least affected, as they consistently perform better than their regional counterparts for both GDP and GDPPC growth regardless of export specification. 
# 
# Despite the correlation being weak, the change from a distinct positive correlation between *all* exports and GDP growth and the negative or neutral correlation between *natural resource* exports and GDP growth indicates natural resources have a negative pressure on GDP growth. This section demonstrates that natural resources have a clear negative effect on growth. The next sections will attempt to explain which factors are the most influential at preventing growth. 

# <div class="alert alert-block alert-warning">
#     <b> Prices and GDP Growth: </b>   
# In this section, we will be focusing on Oil prices and exports. We chose to focus on oil due to more reliable information being available and a consistent international price is available unlike other nautral resources. In addition, the majority of our resource-rich countries export oil. 

# In[406]:


# Price of Oil from 1998 to 2016
url = 'https://data.worldbank.org/share/widget?indicators=EP.PMP.SGAS.CD'
IFrame(url, width=500, height=300)


# ![oil%20and%20history-2.jpg](attachment:oil%20and%20history-2.jpg)

# In[407]:


def my_xy_line_plot(dfin, 
                    x='year', 
                    y='GDP_grow', 
                    labelvar='iso3c', 
                    dx=0.006125, 
                    dy=0.006125, 
                    xlogscale=False, 
                    ylogscale=False,
                    xlabel='Time', 
                    ylabel='GDP Growth',
                    labels=False,
                    xpct = False,
                    ypct = False,
                    OLS=False,
                    OLSlinelabel='OLS',
                    ssline=False,
                    sslinelabel='45 Degree Line',
                    filename='time-oil-gdp-growth.pdf',
                    hue='region',
                    hue_order=['East Asia & Pacific', 'Europe & Central Asia',
                               'Latin America & Caribbean ', 'Middle East & North Africa',
                               'North America', 'South Asia', 'Sub-Saharan Africa '],
                    style='Dependence_Deg', 
                    style_order=['Dependent', 'High', 'Medium', 'Low'],
                    palette=True,
                    legend_fontsize=10,
                    label_fontsize=12,
                    loc=None,
                    save=True):
    '''
    Plot the association between x and var in dataframe using labelvar for labels. 
    '''
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_context("talk")
    df = dfin.copy()
    df = df.dropna(subset=[x, y]).reset_index(drop=True)
    # Plot
    k = 0
    fig, ax = plt.subplots()
    sns.lineplot(x=x, y=y, data=df, ax=ax, 
                    hue=hue,
                    hue_order=hue_order,
                    alpha=1, 
                    style=style, 
                    style_order=style_order,
                    palette=palette,
                )
    if OLS:
        sns.regplot(x=x, y=y, data=df, ax=ax, label=OLSlinelabel, scatter=False)
    if ssline:
        ax.plot([df[x].min()*.99, df[x].max()*1.01], [df[x].min()*.99, df[x].max()*1.01], c='r', label=sslinelabel)
    if labels:
        movex = df[x].mean() * dx
        movey = df[y].mean() * dy
        for line in range(0,df.shape[0]):
            ax.text(df[x][line]+movex, df[y][line]+movey, df[labelvar][line], horizontalalignment='left', fontsize=label_fontsize, color='black')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if xpct:
        fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
        xticks = mtick.FormatStrFormatter(fmt)
        ax.xaxis.set_major_formatter(xticks)
    if ypct:
        fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
        yticks = mtick.FormatStrFormatter(fmt)
        ax.yaxis.set_major_formatter(yticks)
    if ylogscale:
        ax.set(yscale="log")
    if xlogscale:
        ax.set(xscale="log")
    handles, labels = ax.get_legend_handles_labels()
    handles = np.array(handles)
    labels = np.array(labels)
    handles = list(handles[(labels!='region') & (labels!='incomeLevel')])
    labels = list(labels[(labels!='region') & (labels!='incomeLevel')])
    ax.legend(handles=handles, labels=labels, fontsize=legend_fontsize, loc=loc)
    if save:
        plt.savefig(pathgraphs + filename, dpi=300, bbox_inches='tight')
    return fig


# In[408]:


palette=sns.color_palette("Blues_r", oildat['Dependence_Deg'].unique().shape[0]+4)[:oildat['Dependence_Deg'].unique().shape[0]*2:2]
figtime = my_xy_line_plot(oildat, 
                x='year', 
                y='GDP_grow', 
                xlabel='Year',
                ylabel='GDP Growth',
                filename='time-gdp-grow.pdf',
                hue='Dependence_Deg',
                hue_order=['Dependent', 'High', 'Medium', 'Low'],
                palette=palette,
                OLS=False, 
                labels=False,
                legend_fontsize=16,
                loc='lower right',
                save=False)


# ![GDPgrowovertime.png](attachment:GDPgrowovertime.png)

# #### Analysis: 
# 
# This graph demonstrates how different dependencies on oil react to price changes. Two time frames demonstrate these tendendcies best: between 1970 and 1990, and 2000 onward. 
# 
# In the 1970s, many developing countries began nationlalizing their oil industries, skyrocketing the price of oil. Theoretically, oil dependent countries who now had a massive revenue increase and benefit from rising oil prices should also see a dramatic rise in GDP growth. However, figtime illustrates how GDP growth, particularly in the most dependendent countries with 75%+ of their GDP in oil revenues have dramatic rising and dips in the 1970s. We do see a rough maximum of growth in 1976 when oil prices were at their highest. However, the most dependent countries were the most erratic, bouncing between 10-20% growth and 0% growth. There is also a steady decline in GDP growth, finally resting around 0-5% for the entirety of the 1980s. This coincides with a the decline of oil prices, which reached a bottom in 1986. While we can assume that resource dependent countries roughly follow the trends of resource prices, higher levels of dependence directly correlate with GDP growth erraticism and unreliability. Countries with low dependence follow price trends well but with more steady growth and less extremes. 

# These hypotheses are further corroborated by the 2000s onward. As seen on the World Bank and FRED graph, the price of oil has been extremely erratic, on a steady rise until 2014, then rising again from 2016-2020.The final drop around 2020 should be attributed to the Coronavirus and the sudden drop in oil stocks. However, average growth for oil countries was hovering around 0% since around 2012. This is contradictory to what should be assumed about resource dependent countries. Rather than growing more rapidly with a rising price of oil, there is a peak in prices around 2003-2004 and a slight decline since. Most countries that export oil have not exceed 10% increases since 2005~ but oil price peaked in 2009 and 2015 again. While stable economic growth could be seen as a benefit, it seems dependent countries only react to oil prices when they decline rapidly and not when they steadily increase. Therefore, some mechanic is preventing GDP growth inspite of rising prices. 

# <div class="alert alert-block alert-warning">
#     <b> Exports and Government Rents: </b>   
# Here, we will be establishing a correlation between dependence on nautral resources and government rents. Ultimately, this correlation demonstrates how governments employ resource revenues 

# In[ ]:


x = compdat[['NR_TE','NRR','Exports_TR']]
y = compdat['GDP_grow']

x = sm.add_constant(x)
lrm1 = smf.ols(formula='GDP_grow ~ NR_TE + NRR + Exports_TR',data=compdat).fit()


# In[410]:


print(lrm1.summary())


# ![Data_GDP_diff.png](attachment:Data_GDP_diff.png)

# In[ ]:


x = oildat[['NR_TE','Exports_TR', 'NRR','OR']]
y = oildat['GDP_grow']

x = sm.add_constant(x)
lrm2 = smf.ols(formula='GDP_grow ~ NR_TE + Exports_TR + NRR + OR',data=oildat).fit()


# In[411]:


print(lrm2.summary())


# ![image.png](attachment:image.png)

# These two data analysis show surprising results. LRM1 runs a regression that demonstrates that as natural resource rents increase, GDP growth also increase (.05 slope with a p<.01). For oil rich countries, as oil rents increase, GDP growth also increases ( .1 slope with a p<.05). This correlation is indicative that as GDP grows, governments seek to gain more rents from natural resources. This data is better represented in oil countries (R^2 = .03>.014). However, this data could be spread out due to differences in government types. Countries with higher economic growth (like Norway or the Saudi Arabia) are split between different types of government, such as democracies and autocracies. However, despite the variance, there is a positive correlation between government rents and GDP growth. 

# In[421]:


symbols = ['circle', 'x', 'square', 'cross', 'diamond', 'star-diamond', 'triangle-up']
fig5 = px.scatter(dffig,
                 x="NR_TE", 
                 y="ln_NRR", 
                 color='region',
                 symbol='region',
                 symbol_sequence=symbols,
                 hover_name='Country Name',
                 hover_data=['iso3c', 'NR_TE', 'NRR', 'gdp_pc'],
                 size='gdp_pc',
                 size_max=20,
                 trendline="ols",
                 trendline_scope="overall",
                 trendline_color_override="black",
                 labels={
                     "NR_TE": "Natural Resources as a Percentage of Total Exports",
                     "ln_NRR": 'Log of Natural Resource Rents',
                     "region": "WB Region",
                     "gdp_pc": "GDP Per Capita"
                 },
                 opacity=0.75,
                 height=700,
                )


# In[413]:


fig5.show()


# ![NR_TEvsNR_TE.png](attachment:NR_TEvsNR_TE.png)

# In[414]:


symbols = ['circle', 'x', 'square', 'cross', 'diamond', 'star-diamond', 'triangle-up']
fig6 = px.scatter(dffig2,
                 x="NR_TE", 
                 y="ln_OR", 
                 color='region',
                 symbol='region',
                 symbol_sequence=symbols,
                 hover_name='Country Name',
                 hover_data=['iso3c', 'NR_TE', 'NRR', 'gdp_pc'],
                 size='gdp_pc',
                 size_max=20,
                 trendline="ols",
                 trendline_scope="overall",
                 trendline_color_override="black",
                 labels={
                     "NR_TE": "Natural Resources (Oil) as a Percentage of Total Exports",
                     "ln_OR": 'Log Oil Rents as a Percentage of GDP',
                     "region": "WB Region",
                     "gdp_pc": "GDP Per Capita"
                 },
                 opacity=0.75,
                 height=700,
                )


# In[415]:


fig6.show()


# ![newplot%20%281%29.png](attachment:newplot%20%281%29.png)

# #### Analysis: 
# 
# These analsyes demonstrate that as dependence increases, natural resource rents also increase. For both natural resources in general and oil, there is a clear positive correlation between a rise in resources as a percent of exports and government rents. Fig5 demonstrates that as natural resources increase by 1%, natural resouce rents increase by .020% (slope=.02). The only exception to this rule was Botswana, which saw a decrease in rents. Regardless of government type, all countries increased government rents as dependence on resources increased. 
# 
# Oil countries showed similar data. These countries were filtered to exclude any low-level oil exporters, where oil rents are greater than 5% of total GDP. Although the R^2 is only .38, there is a clear cluster of countries with 90%+ oil exports and oil rents increasing exponentially. Oil showed a slightly more elastic correlation, as rents increase by .022% as oil exports increased by 1%. Excluding the outliers of Papua New Guinea and Mongolia would likely show a steeper slope as well, skewed towards the cluster in the top right quandrant. 
# 
# It is extrememly important to note the regional differences for both natural resources and oil. The Middle East consistently ranks highest for oil exports and high resource rents. The countries with highest rents also tend to be authoritarian, such as Iraq, Saudi Arabia, and the Democratic Republic of Congo. These nations also have some of the most human rights violations and political instability. The countries with the highest rents also have medium-low GDP per capita, like Iraq and Angola. Clearly, there is a diversion of revenue from the people of the country to the government. 

# <div class="alert alert-block alert-warning">
#     <b> Over Time: </b>  How GDP growth and resource rents influence economic growth over time

# In[416]:


def my_xy_line_plot(dfin, 
                    x='year', 
                    y='GDP_grow', 
                    labelvar='iso3c', 
                    dx=0.006125, 
                    dy=0.006125, 
                    xlogscale=False, 
                    ylogscale=False,
                    xlabel='Time', 
                    ylabel='GDP Growth',
                    labels=False,
                    xpct = False,
                    ypct = False,
                    OLS=False,
                    OLSlinelabel='OLS',
                    ssline=False,
                    sslinelabel='45 Degree Line',
                    filename='time-gdp-growth.pdf',
                    hue='region',
                    hue_order=['East Asia & Pacific', 'Europe & Central Asia',
                               'Latin America & Caribbean ', 'Middle East & North Africa',
                               'North America', 'South Asia', 'Sub-Saharan Africa '],
                    style='Dependence_Deg', 
                    style_order=['Dependent', 'High', 'Medium', 'Low'],
                    palette=True,
                    legend_fontsize=10,
                    label_fontsize=12,
                    loc=None,
                    save=True):
    '''
    Plot the association between x and var in dataframe using labelvar for labels. 
    '''
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_context("talk")
    df = dfin.copy()
    df = df.dropna(subset=[x, y]).reset_index(drop=True)
    # Plot
    k = 0
    fig, ax = plt.subplots()
    sns.lineplot(x=x, y=y, data=df, ax=ax, 
                    hue=hue,
                    hue_order=hue_order,
                    alpha=1, 
                    style=style, 
                    style_order=style_order,
                    palette=palette,
                )
    if OLS:
        sns.regplot(x=x, y=y, data=df, ax=ax, label=OLSlinelabel, scatter=False)
    if ssline:
        ax.plot([df[x].min()*.99, df[x].max()*1.01], [df[x].min()*.99, df[x].max()*1.01], c='r', label=sslinelabel)
    if labels:
        movex = df[x].mean() * dx
        movey = df[y].mean() * dy
        for line in range(0,df.shape[0]):
            ax.text(df[x][line]+movex, df[y][line]+movey, df[labelvar][line], horizontalalignment='left', fontsize=label_fontsize, color='black')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if xpct:
        fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
        xticks = mtick.FormatStrFormatter(fmt)
        ax.xaxis.set_major_formatter(xticks)
    if ypct:
        fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
        yticks = mtick.FormatStrFormatter(fmt)
        ax.yaxis.set_major_formatter(yticks)
    if ylogscale:
        ax.set(yscale="log")
    if xlogscale:
        ax.set(xscale="log")
    handles, labels = ax.get_legend_handles_labels()
    handles = np.array(handles)
    labels = np.array(labels)
    handles = list(handles[(labels!='region') & (labels!='incomeLevel')])
    labels = list(labels[(labels!='region') & (labels!='incomeLevel')])
    ax.legend(handles=handles, labels=labels, fontsize=legend_fontsize, loc=loc)
    if save:
        plt.savefig(pathgraphs + filename, dpi=300, bbox_inches='tight')
    return fig


# In[417]:


palette=sns.color_palette("Reds_r", compdat['Dependence_Deg'].unique().shape[0]+4)[:compdat['Dependence_Deg'].unique().shape[0]*2:2]
fig8 = my_xy_line_plot(compdat, 
                x='year', 
                y='GDP_grow', 
                xlabel='Year',
                ylabel='GDP Growth',
                filename='time-gdp-grow.pdf',
                hue='Dependence_Deg',
                hue_order=['Dependent', 'High', 'Medium', 'Low'],
                palette=palette,
                OLS=False, 
                labels=False,
                legend_fontsize=16,
                loc='lower right',
                save=False)


# ![Year%20vs%20GDP%20growth.png](attachment:Year%20vs%20GDP%20growth.png)

# In[418]:


palette=sns.color_palette("Purples_r", compdat['Dependence_Deg'].unique().shape[0]+4)[:compdat['Dependence_Deg'].unique().shape[0]*2:2]
fig9 = my_xy_line_plot(compdat, 
                x='year', 
                y='NRR', 
                xlabel='Year',
                ylabel='Natural Resource Rents as a Percentage of GDP',
                filename='time-NRR-grow.pdf',
                hue='Dependence_Deg',
                hue_order=['Dependent', 'High', 'Medium', 'Low'],
                palette=palette,
                OLS=False, 
                labels=False,
                legend_fontsize=16,
                loc='upper right',
                save=False)


# ![NRRovertime.png](attachment:NRRovertime.png)

# In[420]:


palette=sns.color_palette("Blues_r", compdat['Dependence_Deg'].unique().shape[0]+4)[:compdat['Dependence_Deg'].unique().shape[0]*2:2]
fig10 = my_xy_line_plot(oildat, 
                x='year', 
                y='OR', 
                xlabel='Year',
                ylabel='Oil Rents as a Percentage of GDP',
                filename='time-NRR-grow.pdf',
                hue='Dependence_Deg',
                hue_order=['Dependent', 'High', 'Medium', 'Low'],
                palette=palette,
                OLS=False, 
                labels=False,
                legend_fontsize=16,
                loc='upper right',
                save=False)


# ![ORovertime.png](attachment:ORovertime.png)

# #### Analysis: 
# 
# As discussed in the price section, higher dependence on nautral resources creates sporatic growth and inconsistent trend lines. This is shown most clearly whe comparing dependence levels over time. Though averages are consistently positive (excluding dips in the 1980s and 2009), the highly dependent countries have much more randomized and erratic growth. An interesting note is that the overall natural resource trends follow the changes in oil prices more than the oil price nations alone. This is likely due to overall market dips when oil prices are low, affecting other natural resource markets. 
# 
# Even more dramatically, natural resource rents vary over time. The highly dependent countries vary much more extremely in rents than the less dependent countries, from as low as 10% to more than 40% of GDP. Low, Medium, and High dependencies follow roughly the same trends of resource rents and the highest dependency deviates extremely. Throughout time, most of the dramatic changes in rents occur in the "dependent" category, rather than the other three categories. 

# Changes in rents in the dependent category for both all resources and oil-specific countries most strongly mimic trends in history. The most notable is the 2009 recession, which created a negative trend in GDP growth and rents. Both declined rapidly, but bounced back quickly. However, after 2009, most natural resources increased in price, but GDP growth did not follow this trend. It takes longer for countries to respond to increases in prices than rapid declines. This is likely due to the demand for natural resources being roughly stable *except* for during recessions. Then, as demand returns to normal slowly, resource rich countries have more long-term effects to their supply markets than the demand markets. 
# 
# Thus, natural resources tend to have negative effects on grow, as negative shocks will be more long-lasting and dramatic than positive shocks. Over time, depedence on these resources will create asymmetrical and erratic growth, limiting true and stable development for underdeveloped countries. 

# ## Conclusion

# Observing export centralization, price volatility, and resource rents illustrates that resource endowment *does* correlate heavily with economic stagnaition. Compared to total exports, natural resources have negative effects on GDP growth, GDP per capita growth, and economic diversity. Natural resources also seem to enduce economic instability, as these more resource-dependent countries are less economically stable and have erratic growth. 
# 
# While there are some unique outliers, most of this data corroborates the hypothesis that resource endowment induces or encourages economic stagnation. Export centralization negatively correlated with GDP and GDP per capita growth. Unlike other exports, resources are less stable and damage the growth of the economy altogether. Similarly, resource prices are highly volatile and there is a clear correlation between dips in resource prices and GDP growth dips. However, price hikes are *not* correlated with rises in GDP growth. Therefore, as Ross indicated, there are more negative long-term effects of resource markets than positive effects. Finally, there is also a correlation between resource dependence and government rents. There is a clear link between government's channeling revenue and an increased dependence on resources, particularly with oil. The one relatively surprising link was a lack of correlation between authoritarian leaders and government rents. While authoritarians did consentrate about the average, there were a fair number of high-ranking democracies with high levels of resource rents. Similarly, some authoritarian states were below average for rent concentration. Altogther, our data showed a distinct correlation between natural resource dependency and stagnation in economic growth. Though growth may appear to be high at times, the erratic nature and negative long-term effects deter strong, consistent economic performance. 

# ## Sources
# Adams, Dawda, Kweku Adams, Subhan Ullah, and Farid Ullah. “Globalisation, Governance, Accountability and the Natural Resource ‘curse’: Implications for Socio-Economic Growth of Oil-Rich Developing Countries.” *Resources Policy* 61 (2019): 128–40. https://doi.org/10.1016/j.resourpol.2019.02.009.
# 
# Federal Reserve Bank of St. Louis. "Historical WTI spot crude oil prices." *Drilling Manual*. https://www.drillingmanual.com/crude-oil-price-history-graph-tables-for-last-80-years/. 
# 
# Ghura, Dhaneshwar and Catherine Pattillo. “Macroeconomic Policy Frameworks for Resource-Rich Developing Countries.” *International Monetary Fund* (2012): 1-55.
# 
# Haseeb, Muhammad, Sebastian Kot, Hafezali Iqbal Hussain, and Fakarudin Kamarudin. “The Natural Resources Curse-Economic Growth Hypotheses: Quantile–on–Quantile Evidence from Top Asian Economies.” *Journal of Cleaner Production* 279 (2021): 123596–. https://doi.org/10.1016/j.jclepro.2020.123596.
# 
# Lederman, Daniel, William F. Maloney. *Natural Resources Neither Curse nor Destiny.* Palo Alto, CA: Stanford Economics and Finance, an imprint of Stanford University Press, 2007.
# 
# Murshed, Syed Mansoob, and Leandro Antonio Serino. “The Pattern of Specialization and Economic Growth: The Resource Curse Hypothesis Revisited.” *Structural Change and Economic Dynamics* 22, no. 2 (2011): 151–61. https://doi.org/10.1016/j.strueco.2010.12.004.
# 
# Ross, Michael Lewin. *The Oil Curse : How Petroleum Wealth Shapes the Development of Nations.* Princeton, N.J: Princeton University Press, 2012.
# 
# Shu Yang, Elyas Abdulahi, Muhammad Afaq Haider, and Muhammed Asif Khan. “Revisiting the Curse: Resource Rent and Economic Growth of Sub-Sahara African Countries.” *International Journal of Economics and Financial Issues* 9, no. 1 (2019): 121–30.
# 
# Venables, Anthony. “Using Natural Resources for Development: Why Has It Proven So Difficult?” *Journal of Economic Perspectives*, 30 no.1 (2016): 161-184. https://www.aeaweb.org/articles?id=10.1257/jep.30.1.161. 
# 
# Wang, Rong, Junlan Tan, and Shuangliang Yao. “Are Natural Resources a Blessing or a Curse for Economic Development? The Importance of Energy Innovations.” *Resources Policy* 72 (2021): 102042–. https://doi.org/10.1016/j.resourpol.2021.102042.
# 
# Williams, Andrew. “Shining a Light on the Resource Curse: An Empirical Analysis of the Relationship Between Natural Resources, Transparency, and Economic Growth.” *World Development* 39, no. 4 (2011): 490–505. https://doi.org/10.1016/j.worlddev.2010.08.015.

# ### Sources for Data
# [Venables - Appendix Data](https://assets.aeaweb.org/asset-server/articles-attachments/jep/app/3001/30010161_app.pdf) \
# [World Bank - GDP growth Data](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG) \
# [World Bank - GDP per capita Data](https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG) \
# [World Bank - Oil Rents as % of GDP](https://data.worldbank.org/indicator/NY.GDP.PETR.RT.ZS) \
# [World Bank - Total Exports as % of GDP](https://data.worldbank.org/indicator/NE.EXP.GNFS.ZS) \
# [World Bank - Total Natural Resources Rents as % of GDP](https://data.worldbank.org/indicator/NY.GDP.TOTL.RT.ZS) \
# [OEC - Export information](https://oec.world/en/profile/country/lbr) 
