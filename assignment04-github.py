from github import Github
from config import config as cfg
import requests

# Defining the key, stored in config file to avoid publishing

apikey = cfg["apikey"] 

#Using the key

g = Github(apikey)

# Clone repo location

repo = g.get_repo("BTunney92/data-representation-coursework")

# Getting the repo file

fileInfo = repo.get_contents("test.txt")

urlOfFile = fileInfo.download_url

#print (urlOfFile)

# using the file url to get the file data

response = requests.get(urlOfFile)

# pulling the text file conten

contentOfFile = response.text

#print (contentOfFile)

#using replace function to switch all occurences of 'Andrew' (and 'andrew') with 'Brendan'

newContents = contentOfFile.replace("Andrew", "Brendan").replace("andrew", "Brendan")

#print (newContents)

gitHubResponse = repo.update_file(fileInfo.path, "Replacing Andrew", newContents, fileInfo.sha)

print (gitHubResponse)