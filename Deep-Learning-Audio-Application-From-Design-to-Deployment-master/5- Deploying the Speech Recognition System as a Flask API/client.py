import requests
import os

# server url
URL = "http://127.0.0.1:5000/predict"


# audio file we'd like to send for predicting keyword
FILE_PATH = "test"


if __name__ == "__main__":
    for f in FILE_PATH:
        # open files
        FILE_PATHTemp = ""
        FILE_PATHTemp = os.path.join(FILE_PATH, "/")
        FILE_PATHTemp = os.path.join(FILE_PATHTemp, f)

        file = open(f, "rb")

        # package stuff to send and perform POST request
        values = {"file": (FILE_PATHTemp, file, "audio/wav")}
        response = requests.post(URL, files=values)
        data = response.json()

        print("Predicted keyword: {}".format(data["keyword"]))












