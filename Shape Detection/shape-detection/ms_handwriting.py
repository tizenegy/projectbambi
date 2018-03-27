
# imports for MS computer vision API (Elfert)
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, time, json
import time


# code according to MS:
# https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python

subscription_key = "6d980068a64147e4bf70dfde51a5a787"
vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Cursive_Writing_on_Notebook_paper.jpg/800px-Cursive_Writing_on_Notebook_paper.jpg"
image_url = "https://1.bp.blogspot.com/-pZUYBRStFN8/WresdmAiDPI/AAAAAAAADTk/XnTvz4q7TJ4ReOn_3TRhU5CM_bgPP20xgCLcBGAs/s1600/hand4.png"
text_recognition_url = vision_base_url + "RecognizeText"
print(text_recognition_url)
headers  = {'Ocp-Apim-Subscription-Key': subscription_key}
params   = {'handwriting' : True}
data     = {'url': image_url}
response = requests.post(text_recognition_url, headers=headers, params=params, json=data)
response.raise_for_status()
print(str(response.status_code))
operation_url = response.headers["Operation-Location"]
# polling
analysis = {}
while not "recognitionResult" in analysis:
    response_final = requests.get(response.headers["Operation-Location"], headers=headers)
    response_final.raise_for_status()
    print(str(response_final.status_code))
    analysis = response_final.json()
    time.sleep(1)



#from matplotlib.patches import Polygon
polygons = [(line["boundingBox"], line["text"]) for line in analysis["recognitionResult"]["lines"]]

# plt.figure(figsize=(15,15))

# image  = Image.open(BytesIO(requests.get(image_url).content))
# ax     = plt.imshow(image)
for polygon in polygons:
#     vertices = [(polygon[0][i], polygon[0][i+1]) for i in range(0,len(polygon[0]),2)]
    text     = polygon[1]
    print(polygon[1])
#     patch    = Polygon(vertices, closed=True,fill=False, linewidth=2, color='y')
#     ax.axes.add_patch(patch)
#     plt.text(vertices[0][0], vertices[0][1], text, fontsize=20, va="top")
# _ = plt.axis("off")