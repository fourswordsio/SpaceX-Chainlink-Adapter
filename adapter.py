from bridge import Bridge
from elonmusk import SpaceX
import requests

class Adapter:
    
    def __init__(self, input):
        self.id = input.get('id', '1')
        self.bridge = Bridge()
        self.create_request()

    def create_request(self):
        try:
            data = SpaceX().get_launch_info()
            self.result_success(data)
        except Exception as e:
            self.result_error(e)
        finally:
            self.bridge.close()
    
    def result_success(self, data):
        self.result = {
            'jobRunID': self.id,
            'data': data,
            'result': data["launch_time"],
            'statusCode': 200,
        }

    def result_error(self, error):
        self.result = {
            'jobRunID': self.id,
            'status': 'errored',
            'error': f'There was an error: {error}',
            'statusCode': 500,
        }