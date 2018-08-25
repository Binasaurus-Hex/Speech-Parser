from requests import post
from base64 import b64encode


class SpeechToText(object): 

    URL = "https://speech.googleapis.com/v1/speech:recognize"

    def __init__(self, api_key:str):
        self.api_key = api_key
        self.params = {
            "key": api_key
        }

    def __call__(self, filename:str):
        '''
        Sends a file[name] to Google's web servers and returns the result

        Use like:
            x = SpeechToText(key)
            t = x('filename.wav')
            print(t)
        '''

        if not filename.lower().endswith('.wav'):
            raise ValueError('Filename is not a WAV file.')

        # Read the file and encode it to b64
        with open(filename, 'rb') as a:
            raw = a.read()
        b64bytes = b64encode(raw)
        b64string = b64bytes.decode()

        # Generate the params
        json = {
            'audio': {
                'content': b64string
            },
            'config': {
                'languageCode': 'en-UK'
            }
        }

        # Send the request
        site = post(self.URL, params=self.params, json=json)
        output = site.json()
        # Return 
        return output['results'][0]['alternatives'][0]['transcript']


# transcriber = SpeechToText('api_key')
# transcription = transcriber('filename.wav')
