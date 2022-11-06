import json

with open('books.json', 'r+') as file:
    content = file.read()
    file.seek(0)
    content.replace('andrew', 'brendan')
    file.write(content)
    
    