
# imports for MS computer vision API (Elfert)
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, time, json

# Code for MS computer vision API: (Elfert)
# https://nordicapis.com/digitize-your-notes-with-microsoft-vision-api/

# Keys  
endpoint = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0'  
api_key = '81fe31408397418bbeb94ddf992e9b81'

headers = {  
	# Request headers.  
	# Another valid content type is "application/octet-stream".  
	'Content-Type': 'application/json',  
	'Ocp-Apim-Subscription-Key': api_key,  
}
body = {'url':'http://i.imgur.com/W2fF6uC.jpg'}
params = {'handwriting' : 'true'}

# API calls
try:  
	response = requests.request('POST', endpoint + '/RecognizeText', json=body, data=None, headers=headers, params=params)
if response.status != 202:  
	# Display JSON data and exit if the REST API call was not successful.  
	parsed = json.loads(response.text)  
	print ("Error:")  
	print (json.dumps(parsed, sort_keys=True, indent=2))  
	exit()
# grab the 'Operation-Location' from the response  
operationLocation = response.headers['Operation-Location']
print('\nHandwritten text submitted. Waiting 10 seconds to retrieve the recognized text.\n')  
time.sleep(10)
# Execute the second REST API call and get the response.  
response = requests.request('GET', operationLocation, json=None, data=None, headers=headers, params=None)

# 'data' contains the JSON data. The following formats the JSON data for display.  
parsed = json.loads(response.text)
lines = parsed['recognitionResult']['lines']
for line in lines:  
    print (line['text'])
except Exception as e:  
    print('Error:')  
    print(e)

# this opens the file for writing  
with open(“mynote.txt”, “w”) as f:  
    for line in reversed(lines):  
        print line['text']  
        # write the value to the file  
        f.write(line['text'])  
