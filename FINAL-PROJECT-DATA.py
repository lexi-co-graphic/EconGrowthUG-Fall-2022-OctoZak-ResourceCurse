#!/usr/bin/env python
# coding: utf-8

# Lexi Eid and Krithi Choudhary \
# Dr. Ozak \
# ECON 4362 \
# 13 November 2022  
# 
# # Paying for Poverty: Why Resource Endowment Prevents Growth 
# ## Final Project: Data and Analysis
# 

# ## Question/ Problem We’re Addressing
# Beginning in the 1950s, scholars have reflected on the lack of development in low and middle-income countries. This correlation between lower income and slower growth was originally suspected to be a factor of path dependence, where a lack of wealth in the 1800s and 1900s could lead to a lack of growth in the 21st century. However, the 1980s demonstrated that lower-income countries CAN experience rapid economic growth, by a factor of more than 10% per year. In particular, the “miracle growth” countries like China, Korea, and Japan, categorized as countries with sustained economic growth of more than 6% per year, inspired further research. Still, the majority of low-income nations remained low-income. Some glaring exceptions also stood out: countries endowed with natural resources which should catalyze growth and integration into the international economy. Often, the results were counterintuitive to logic. These countries, endowed with oil, natural gas, and other high-value-added resources, experienced slower economic growth than their high-income counterparts and their low-income neighbors. In 1993, Richard Auty coined the term *resource curse* to describe this phenomenon of lower economic growth in resource-abundant countries. 
# 
# The resource curse was inspired by another similar phenomenon, the Dutch disease. The Dutch disease suggests that increased exports of natural resources instigated a decline in national production competitiveness and created conditions for recessions. Growing natural resource markets often correlate to weakened export markets of goods and services because tradable goods become less competitive as the country becomes less specialized in its non-resource goods. Particularly for countries in the fuel industry, these changes in specialization influence how competitive countries are in the international and create unfavorable conditions for economic growth. The resource curse expands this phenomenon to include economic stagnation and stunting of growth in sectors outside of the export market. 
#     
# Our research aims to investigate this exact topic: *How does the resource curse affect low-income economies and do natural resources induce economic stagnation?*

# ## Explanation of Variables
# 1) Volatility of prices \
# 	Most natural resources are roughly price inelastic on the supply and demand side, making the market highly vulnerable to small price changes. Changes in demand or supply shocks of all kinds can create large swings in prices that affect the market rapidly. As Michael Ross highlights, “the price of oil is more volatile than the price of 95 percent of all products sold in the United States,” making energy resources and other natural resources dangerous investments (Ross, 50). When governments rely on these revenues, economic growth is highly dependent on international prices. If prices dip, as they did in 2020 during the COVID pandemic, unexpected changes can create detrimental setbacks in growth. Goods and services are much less volatile, making them safer investments for growth. Resource-rich countries are therefore at the mercy of the international market for economic revenue and growth. \
#     We will tracking the trend lines between prices of oil and other nautral resources and economic growth. A positive correlation would indicate that economic growth is reliant on export prices. Thus, the volatility of the prices would be an impediment to economic growth.     
#     
# 2) Resource Rent Revenues \
# 	Overwhelmingly, a positive correlation exists between resource endowment and the size of government. These larger governments are also disproportionately dependent on revenues from natural resources, relying less on taxes than their resource-poor counterparts (Ross, 29). These disproportionately large governments rely on resource revenues and often fail to stabilize their economies due to shorter time horizons. The alternating periods of high prices tend to correlate with faster growth whereas low prices are associated with poor budgeting and high expenditures. Thus, governmental rents from resources can reveal where money is wasted or spent on consumption rather than investment.\
#     We will observe the trends between the size of government and economic growth. If there is a negative correlation, it would imply that government rents are detrimental to economic growth. 
# 
# 3) Income Stagnation and Unemployment \
# 	As a factor of the Dutch disease, a competitive advantage in natural resources prevents development in other export industries. The “competitive hypothesis” of the resource curse argues that specialization in the resource industry can subdue growth in more diversified and stable industries, thus preventing the overall growth of the economy (Mershed and Serino, 152). In addition, the overemphasis on the resource sector can create unemployment as jobs shift from other industries. In the long term, the oversaturation of the labor market can create wage stagnation, lower GDP per capita, and lower standards of living. This combination of hyperspecialized industries and low wages can subdue economic growth, even when prices for natural resources are high. \
#     For this section, we will be observing what percent of the economy is employed by the natural resource industry and whether employment in other sectors is decreasing. We will also be comparing natural resource rents to GDP per capita. If increased unemployment in non-resource industries is negatively correlated with economic growth, this data would suggest that natural resources are detrimental to economic growth. 

# ## Data 
# The data necessary to assess our argument is compiled into five essential pieces of data: 
# 1) Statistics of resource endowment, detailing which resource each country has and the percent of exports \
# 2) GDP growth (and reductions) since exporting natural resources \
# 3) GDP per capita growth (and reductions) since exporting natural resources \
# 4) Prices of the natural resources before and after exportation \
# 5) Government rents from natural resources and their factor of total GDP/production \
# and \
# 6) Exports and Natural Resource Exports as a percentage of Total GDP. 
# 
# These five factors will demonstrate how the exchange of natural resources has changed in recent years and how developing economies have responded. As outlined above, our goal is to compare the data on the total production of natural resources to GDP per capita and total GDP growth to measure whether correlations exist between the two variables. The prices of the resources and the government rents will serve as control variables, to test whether extreme variation in GDP comes from internal or external factors. Due to a large number of confounding variables, we chose two external factors (price and government rents) to measure internal and external pressure on the market at all times. 
# 
# Ultimately, these variables will address the factors of economic growth and demonstrate how resource-rich countries are at a unique disadvantage: despite an ingrained source for wealth, the countries are failing to develop or to grow. 
# 
# ### Goals of Analysis 
# 
# With our data, we intend to demonstrate four main correlations. 
# 
# 1) Demonstrate a correlation between the price of natural resource exports and negative (OR neutral) GDP growth \
# Economic logic suggests that increase exports is linked to GDP growth. Therefore, a negative or neutral correlation between GDP growth and natural resource exports would illustrate some negative pressure from natural resources on GDP. \ 
# 
# We plan to run regression to determine a correlation between price of exports and GDP growth both average for countries and over time. Ideally, both will demonstrate that peaks of prices are correlated with dips in GDP growth. 
# 
# 
# 2) Demonstrating negative (OR neutral) correlation between price of natural resources and GDP per capita growth \
# Again, economic logic would suggest that increasing GDP and increased natural resources exports would benefit the country's population. A negative or neutral correlation suggests that the increased revenues do not go to the people, but go somewhere else. If GDPPC is stagnant, this suggests limited development and growth. \
# 
# We plan to run regression between prices of natural resources and GDPPC growth, as well as a regression for resource endowment as a percentage of exports and GDPPC growth. A negative correlation for both would support or hypothesis. 
# 
# 
# 3) Illustrating a correlation between prices of natural resource exports and government rents \
# Given that natural resource have a negative pressure on GDP growth and GDPPC is stagnant, where does that extra income go? Demonstrating a correlation between prices and rents will illustrate that in some way, governments benefit from increase prices rather than the people. Therefore, government rents would be detrimental to development and growth. \
# 
# We plan to run regressions between prices of natural resources and government rent growth, as well as a regression for resource endowment as a percentage of exports and rent growth. It is crucially import to note that we plan to use region as a control variable for these regressions. Regions that are more authoritarian than others (like the Middle East) will naturally have higher resource rents than democratic regions (like Europe or Africa). However, all regions should show negative trends. Therefore, by keeping region as a control variable, we will ensure that no data is skewed by government type or regional diversity. 
# 
# 
# and lastly, \
# 4) Illustrating the general correlation between high resource endowment and GDP growth over time \
# Using the data compiled previously, we hope to illustrate how resource endowment has an overwhelmingly negative impact of GDP growth and GDPPC growth. These variables demonstrate the various factors of the economy which are influenced by resource endowment and those which are negatively impacted. 
# 
# 
# Our outputs will be linear regression dynamic models and several R2 data analyses. Particularly for regressions over time, we intend to use linear regressions to show correlations between variables. 
# 
# ### Source of the Data
# 
# Most of our data can be sources from either OEC, the IMF, and the World Bank. However, some data is incomplete or unreliable. By using international market price and reported government rents of minerals, we hope to limit the effect of unreliable information. 

# <div class="alert alert-block alert-warning">
#     <b> Country Selection </b> 
# 
# We chose our countries from the IMF(2012) Data set. These countries were chosen as "resource-rich" as natural resources account for 20%+ of exports or 20%+ of fiscal revenue. 
# This data set is organized by GNI per capita from lowest to highest. We excluded the rising natural resource exporters due to a lack of reliable information across several data banks. Information not included in the IMF Data Set was acquired through OEC data banks. 

# In[30]:


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


# In[65]:


countryprelimdata = (['Congo, Dem. Rep', 'COD', 'Minerals & Oil', 94],
                     ['Liberia', 'LBR', 'Gold/Iron Ore', 35],
                     ['Niger', 'NER', 'Gold/Oil/Uranium', 79],
                     ['Guinea', 'GIN', 'Mining Products', 93],
                     ['Mali', 'MLI', 'Gold', 75],
                     ['Chad', 'TCD', 'Oil', 89],
                     ['Mauritania', 'MRT', 'Iron Ore', 24],
                     ['Lao PDR', 'LAO', 'Copper & Gold', 57],
                     ['Zambia', 'ZMB', 'Copper', 72],
                     ['Vietnam', 'VNM', 'Oil', 14],
                     ['Yemen', 'YEM', 'Oil', 82],
                     ['Nigeria', 'NGA', 'Oil', 97],
                     ['Cameroon', 'CMR', 'Oil', 47],
                     ['Papua New Guinea', 'PNG', 'Oil/Copper/Gold', 77],
                     ['Sudan', 'SDN', 'Oil', 97],
                     ['Uzbekistan', 'UZB', 'Gold/Gas', 54],
                     ['Cote d\'Ivoire', 'CIV', 'Oil/Gold', 17],
                     ['Bolivia', 'BOL', 'Gas', 74],
                     ['Mongolia', 'MNG', 'Copper', 81],
                     ['Congo, Rep. of', 'COG', 'Oil', 90],
                     ['Iraq', 'IRQ', 'Oil', 99],
                     ['Indonesia', 'IDN', 'Oil', 10],
                     ['Timor Leste', 'TLS', 'Oil', 99],
                     ['Syrian Arab Republic', 'SYR', 'Oil', 36],
                     ['Guyana', 'GUY', 'Gold & Bauxite', 42],
                     ['Turkmenistan', 'TKM', 'Oil', 91],
                     ['Angola', 'AGO', 'Oil', 95],
                     ['Gabon', 'GAB', 'Oil', 83],
                     ['Equatorial Guinea', 'GNQ', 'Oil', 99],
                     ['Ecuador', 'ECU', 'Oil', 55],
                     ['Albania', 'ALB', 'Oil/Gas', 10],
                     ['Algeria', 'DZA', 'Oil', 98],
                     ['South Africa', 'ZAF', 'Minerals', 55],
                     ['Iran', 'AZE', 'Oil', 94],
                     ['Peru', 'PER', 'Minerals', 48],
                     ['Brazil', 'BRA', 'Oil/Iron', 26],
                     ['Azerbaijan', 'AZE', 'Oil', 94],
                     ['Botswana', 'BWA', 'Diamonds', 66],
                     ['Kazakhstan', 'KAZ', 'Oil', 60],
                     ['Suriname', 'SUR', 'Minerals', 11],
                     ['Mexico', 'MEX', 'Oil', 15],
                     ['Russia', 'RUS', 'Oil/Minerals', 61],
                     ['Chile', 'CHL', 'Copper', 53],
                     ['Venezuela', 'VEN', 'Oil', 93],
                     ['Libya', 'LBY', 'Oil', 97],
                     ['Bahrain', 'BHR', 'Oil', 96],
                     ['Brunei Darussalam', 'BRN', 'Gas', 87],
                     ['Trinidad and Tobago', 'TTO', 'Gas', 38],
                     ['Saudi Arabia', 'SAU', 'Oil', 87],
                     ['Oman', 'OMN', 'Oil', 73],
                     ['United Arab Emirates', 'UAE', 'Oil', 41],
                     ['Qatar', 'QAT', 'Gas', 88],
                     ['Norway', 'NOR', 'Oil', 62])                             

cpd = pd.DataFrame(countryprelimdata, columns=['Country Name', 'iso3c', 'Exports', 'NR_TE'])
#NR/TE represents natural resources as a percentage of total exports


# In[66]:


cpd


# <div class="alert alert-block alert-warning">
#     <b>Compilation of Data</b> Combining the IMF and OEC data set with the WDI data

# In[33]:


# Paths
pathout = './data/'

if not os.path.exists(pathout):
    os.mkdir(pathout)
    
pathgraphs = './graphs/'
if not os.path.exists(pathgraphs):
    os.mkdir(pathgraphs)


# In[34]:


currentYear = datetime.now().year
year = min(2020, currentYear-2)


# In[35]:


wbcountries = wb.get_countries()
wbcountries = wbcountries.loc[wbcountries.region.isin(['Aggregates'])==False].reset_index(drop=True)
wbcountries['name'] = wbcountries.name.str.strip()
wbcountries['incomeLevel'] = wbcountries['incomeLevel'].str.title()
wbcountries.loc[wbcountries.iso3c=='VEN', 'incomeLevel'] = 'Upper Middle Income'


# In[36]:


wdi_indicators = ['NY.GDP.MKTP.KD.ZG', 'NY.GDP.PCAP.KD.ZG', 'NY.GDP.PETR.RT.ZS', 'NE.EXP.GNFS.ZS', 'NY.GDP.TOTL.RT.ZS', 'NY.GDP.PCAP.PP.KD', 'EP.PMP.SGAS.CD']


# In[37]:


pop_vars = wb.search(string='population')
pop_vars.head()


# In[67]:


wdi = wb.download(indicator=wdi_indicators, country=wbcountries.iso2c.values, start=1950, end=year)
wdi = wdi.reset_index()
wdi['year'] = wdi.year.astype(int)
#GDP Per Capita
wdi['gdp_pc'] = wdi['NY.GDP.PCAP.PP.KD']
#GDP growth annually
wdi['GDP_grow'] = wdi['NY.GDP.MKTP.KD.ZG']
#GPD Per Capita growth annually
wdi['GDPPC_grow'] = wdi['NY.GDP.PCAP.KD.ZG']
#Oil Rents as a percentage of GDP
wdi['OR'] = wdi['NY.GDP.PETR.RT.ZS']
#Natural resource rents as a percentage of GDP
wdi['NRR'] = wdi['NY.GDP.TOTL.RT.ZS']
#Exports as a percentage of GDP
wdi['Exports%'] = wdi['NE.EXP.GNFS.ZS']
#Price of oil 
wdi['POil'] = wdi['EP.PMP.SGAS.CD']

wdi


# In[39]:


wdi = wbcountries.merge(wdi, left_on='name', right_on='country')
wdi


# In[40]:


# merging data to create one complete data set
compdat = cpd.merge(wdi, how="inner", on=["iso3c"])
compdat = compdat.drop(['iso2c', 'adminregion', 'NY.GDP.MKTP.KD.ZG',
                        'NY.GDP.PCAP.KD.ZG', 'NY.GDP.PETR.RT.ZS', 'NE.EXP.GNFS.ZS', 'NY.GDP.TOTL.RT.ZS', 
                        'latitude', 'longitude', 'name', 'capitalCity', 'lendingType', 'country', 
                        'NY.GDP.PCAP.PP.KD', 'EP.PMP.SGAS.CD'], axis=1)


# In[41]:


compdat.loc[compdat.year==2015].count()


# In[42]:


compdat.dtypes


# In[43]:


compdat


# <div class="alert alert-block alert-warning">
#     <b>Example Data Analysis:</b> Regressions and Correlations between variables

# In[68]:


dffig = compdat.loc[compdat.year==year]\
            .dropna(subset=['NR_TE', 'GDP_grow', 'gdp_pc'])\
            .sort_values(by='region').reset_index()


# In[45]:


mod = smf.ols(formula='NR_TE ~ GDP_grow', data=dffig, missing='drop').fit()


# In[46]:


mod.summary2()


# In[47]:


symbols = ['circle', 'x', 'square', 'cross', 'diamond', 'star-diamond', 'triangle-up']
fig1 = px.scatter(dffig,
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
                 height=800,
                )


# In[48]:


fig1.show()


# In[49]:


symbols = ['circle', 'x', 'square', 'cross', 'diamond', 'star-diamond', 'triangle-up']
fig2 = px.scatter(dffig,
                 x="OR", 
                 y="GDP_grow", 
                 color='region',
                 symbol='region',
                 symbol_sequence=symbols,
                 hover_name='Country Name',
                 hover_data=['iso3c', 'OR', 'GDP_grow'],
                 size='gdp_pc',
                 size_max=20,
                 trendline="ols",
                 trendline_scope="overall",
                 trendline_color_override="black",
                 labels={
                     "OR": "Oil Rents as a Percentage of Total GDP",
                     "GDP_grow": "GDP Growth",
                     "region": "WB Region",
                     "gdp_pc": "GDP Per Capita"
                 },
                 opacity=0.75,
                 height=800,
                )


# In[50]:


fig2.show()


# In[59]:


symbols = ['circle', 'x', 'square', 'cross', 'diamond', 'star-diamond', 'triangle-up']
fig3 = px.scatter(dffig,
                 x="Exports%", 
                 y="GDP_grow", 
                 color='region',
                 symbol='region',
                 symbol_sequence=symbols,
                 hover_name='Country Name',
                 hover_data=['iso3c', 'Exports%', 'GDP_grow'],
                 size='gdp_pc',
                 size_max=20,
                 trendline="ols",
                 trendline_scope="overall",
                 trendline_color_override="black",
                 labels={
                     "Exports%": "Total Exports as a Percentage of GDP",
                     "GDP_grow": "GDP Growth",
                     "region": "WB Region",
                     "gdp_pc": "GDP Per Capita"
                 },
                 opacity=0.75,
                 height=800,
                )


# In[60]:


fig3.show()


# ## Sources
# Adams, Dawda, Kweku Adams, Subhan Ullah, and Farid Ullah. “Globalisation, Governance, Accountability and the Natural Resource ‘curse’: Implications for Socio-Economic Growth of Oil-Rich Developing Countries.” *Resources Policy* 61 (2019): 128–40. https://doi.org/10.1016/j.resourpol.2019.02.009.
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
