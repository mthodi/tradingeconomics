import flask
from flask_cors import CORS
from flask import request, jsonify
import datetime
import pandas as pd
import tradingeconomics as te 
te.login('57ecw2ffxbs8337:15gcsbewqm3hrpd')

app = flask.Flask(__name__)

app.config['DEBUG'] = True
cors = CORS(app, supports_credentials=True) # setup CORS

@app.route('/', methods=['GET'])
def index():
    # return index data from te
    data = te.getMarketsData(marketsField='index', output_type='df')
    return jsonify(data.to_dict(orient='records'))

@app.route('/index/', methods=['GET'])
def get_index_components():
    symbol = request.args.get('symbol', type=str)
    data = {}
    if symbol is not None:
        data = te.getMarketsComponents(symbols=symbol, output_type='df').dropna().to_dict(orient='records')
    return jsonify(data)

@app.route('/index/trend', methods=['GET'])
def get_index_trend():
    symbol = request.args.get('symbol', type=str)
    today = datetime.date.today()
    last_year_today = today - datetime.timedelta(days=365)
    data, series = {}, {'data' : [] }
    if symbol is not None:
        data = te.fetchMarkets(
            symbol=symbol,initDate=last_year_today.strftime('%Y-%m-%d'), endDate=today.strftime('%Y-%m-%d')
        ).dropna()
        data['date']  = list(map(lambda x: x.strftime('%m/%d/%Y'), data.index.tolist()))
    return jsonify(data.to_dict(orient='records'))

@app.route('/index/peers', methods=['GET'])
def get_index_peers():
    symbol = request.args.get('symbol', type=str)
    data = [{}]
    if symbol is not None:
        data = te.getMarketsPeers(symbols=symbol, output_type='df').to_dict(orient='records')
    return jsonify(data)

@app.route('/news/', methods=['GET'])
def get_headlines():
    country = request.args.get('country', type=str)
    if country is not None:
        data = te.getNews(country=country).dropna()
        return jsonify(data.to_dict(orient='records'))
    data = te.getNews()
    return jsonify(te.getNews().dropna().to_dict(orient='records'))

@app.errorhandler(404)
def page_not_found(e):
    return " Error 404: The content you were looking for was not found on this server."

@app.errorhandler(500)
def server_fault(e):
    return "Something went wrong, and it is our fault."

app.run(host='127.0.0.1')