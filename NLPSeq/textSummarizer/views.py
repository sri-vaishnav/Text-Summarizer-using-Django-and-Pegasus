from django.shortcuts import render
from django.http import HttpResponse

import requests

API_URL = "https://api-inference.huggingface.co/models/google/pegasus-large"
headers = {"Authorization": f"Bearer {'api_obRAuTuievzuOXrdKNOsJyejsUoIqzgLUi'}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
    "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
})


def index(request):
    if(request.method =="POST"):
        input_string = request.POST['input']
        print(input_string)
        output = query({"inputs" : input_string})
        return render(request, "textSummarizer/index.html", {"text"  : input_string, "summary" : output[0]['summary_text']})
        
    return render(request, "textSummarizer/index.html", {"text"  : ""})
