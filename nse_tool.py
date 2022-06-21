from nsetools import Nse


class Nse_data:
    def __init__(self) -> None:
        nse = Nse()
        self.q = nse.get_quote('TATAMOTORS')
        self.data = {
            "name": "TATAMOTORS",
            "dayHigh":self.q["dayHigh"],
            "averagePrice":self.q["averagePrice"],
            "totalTradedVolume":self.q["totalTradedVolume"],
            "lastPrice":self.q["lastPrice"],
            "open":self.q["open"],
            "dayLow":self.q["dayLow"],
        }
    
    def get_value(self):

        return self.data


if __name__ == '__main__':
    print("++++++++")
    nse = Nse_data()
    print(nse.get_value())