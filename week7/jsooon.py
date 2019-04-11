import requests



#open up a new file named dogpicture.html and write on it 
f = open("dogpicture.html", "w+")

#curl get from the url 
response = requests.get("https://dog.ceo/api/breeds/image/random")
print(response)

data = response.json()
print(data)
#data is JSON format (looks like dictionary)

image = data["message"]
print(image)
#calling the value of key called "message"

message = """
        <html>
        <body>
        <img src="{}" alt="Dog" />
        </body>
        </html>
        """.format(image)

f.write(message)
f.close()
