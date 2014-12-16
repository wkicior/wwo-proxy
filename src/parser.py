import json

class Parser:
    def parse_day(self, day):
        dayval = {'date': day['date']}
        day = {'day' : dayval}
        return day

    def parse(self, json_wwo_input):
        result = json.loads(json_wwo_input)
        days = result['data']['weather']
        result =  map(lambda x: self.parse_day(x), days)        
        return {'forecast' : result}
