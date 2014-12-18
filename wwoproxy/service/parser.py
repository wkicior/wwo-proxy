import json
from converter import *

class Parser:
    """
    Parses the whole json message
    Returns the forecast dictionary
    """
    def parse(self, json_wwo_input):
        result = json.loads(json_wwo_input)
        days = result['data']['weather']
        result =  map(lambda x: self.parse_day(x), days)        
        return {'forecast' : result }

    """
    Parses one day entry
    """
    def parse_day(self, day):
        dayval = {'date': day['date'], 
                  'condition_entries': self.parse_conditions(day['hourly'])}
        day = {'day' : dayval}
        return day

    """
    Parses all the hourly condition entry for a given day
    """
    def parse_conditions(self, hourly_list):
        result = map(lambda x: self.parse_condition_entry(x), hourly_list)
        return result

    """
    Parses a record for a given time
    This should contain all the weather conditions data
    """
    def parse_condition_entry(self, hourly_entry):
        hour = (int(hourly_entry['time']) / 100)
        wind_guts_knots = kmh_to_knots(int(hourly_entry['WindGustKmph']))
        wind_speed_knots = kmh_to_knots(int(hourly_entry['windspeedKmph']))
        wind_dir_degree = int(hourly_entry['winddirDegree'])
        return {'hour' : hour, 'wind_gust_knots': wind_guts_knots, 
                'wind_speed_knots' : wind_speed_knots, 'wind_dir_degree': wind_dir_degree}






