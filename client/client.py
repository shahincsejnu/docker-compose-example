# import python system library, it is used to download the index.html from server
import urllib.request

# this variable contain the request 
fp = urllib.request.urlopen("http://localhost:8080/")

# it correspond to the server response encoded index.html
encodedContent = fp.read()

# it correspond to the server response decoded (what we want to display)
decodedContent = encodedContent.decode("utf8")

# display the server file : index.html
print(decodeContent)


# close the server connection
fp.close()
