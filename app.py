from flask import *
from nse_tool import Nse_data


app = Flask(__name__)

@app.route("/")
def index():
    nse = Nse_data()
    print(nse.get_value())
    res = nse.get_value()
    return f'<html><body><h1>NSE DATA</h1></br><h4>Name : {res["name"]}</h4></br><p>open : {res["open"]}</p>  </br><p>dayHigh : {res["dayHigh"]}</p>  </br><p>dayLow : {res["dayLow"]}</p>  </br><p>averagePrice : {res["averagePrice"]}</p>  </br><p>totalTradedVolume : {res["totalTradedVolume"]}</p> </body></html>'


if __name__ == '__main__':
   app.run(debug = True)