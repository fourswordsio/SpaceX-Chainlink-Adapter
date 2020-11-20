import requests

class SpaceX:
    
    def __init__(self):
        self._api_endpoint = "https://api.spacexdata.com/v3/launches/next"
        
    def get_launch_info(self):
        response = requests.get(self._api_endpoint).json()
        try:
            flight_data = {
                "launch_time": response["launch_date_utc"],
                "mission_id": str(response["mission_id"][0]),
                "mission_name": response["mission_name"],
                "flight_number": response["flight_number"],
                "rocket_name": response["rocket"]["rocket_name"],
                "launch_center": response["launch_site"]["site_name_long"]
            }
            return flight_data
        except Exception as error:
            return error
