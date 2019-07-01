# ABOUT
This repository contains code written for review by Trading Economics Recruitment team.
The code consists of an API written in Python 3.6 using Flask Framework, and a UI written in
Vue.js using Vuetify as a UI framework. 

# How to run

Clone the repository to your machine and then follow the steps below.

## How to run the API
The API is in the folder named mthodi-api. The following should be done while inside that folder.
### 1. Install requirements

Install the required modules with: 

`pip install < requirements.txt`

Make sure you are using Python 3.6+ 

### 2. Add Trading Economics API Key
Insert an API Key from Trading Economics on line 8 of the `app.py` file.
To get a TE API key, please create a developer account at [Trading Economics](https://developer.tradingeconomics.com).

### 3. Run the API
Now you can run the API as follows:

`$ python3 app.py` 

The API should run on `http://localhost:5000` by default.


## How to run the frontend
The UI is contained in folder named `mthodi-ui`. You can run it by doing the following while
working inside `mthodi-ui`

### 1. Install the required modules
`npm install`

### 2. Run a development server
Running `npm run serve` will run a development server on `http://localhost:8000`.
The frontend is configured to fetch data from the API running on `localhost:5000`.
If you run the API on a different URL you should change `src\_config.js` and point it to that URL.
And make sure the API is running when you run the frontend.

### 3. Build the software.
If you don't want to run the development server, you can build the UI as follows:

`npm run build`

This will build the UI into a folder the `dist` folder. You can now run the build using:

`npm run start`

This run an express server on `localhost:5002`. Again, the frontend will be fetching data from 
`localhost:5000`. If you changed the URL of the API, be sure to change the URL in `src\_config.js`
to point to that URL.


***
End of Martin Thodi edit. The rest is original Content from Trading Economics.
***



# ABOUT TRADING ECONOMICS 

Trading Economics provides its users with accurate information for 196 countries including historical data for more than 300.000 economic indicators, exchange rates, stock market indexes, government bond yields and commodity prices. Our data is based on official sources, not third party data providers, and our facts are regularly checked for inconsistencies. TradingEconomics.com has received more than 100 million page views from more than 200 countries. Trading Economics is owned by IECONOMICS INC.

# ABOUT THE API

The TE API provides you with direct access to 300.000 economic indicators, exchange rates, stock market indexes, government bond yields and commodity prices. Providing several request methods to query our databases, with samples available in different programming languages, it is the best way to export data in XML, CSV or JSON format. The API can be used to feed a custom developed application, a public website or just off-the-shelf software like Microsoft Excel. 

# DOCUMENTATION

http://docs.tradingeconomics.com/
