import requests

# Define the endpoint URL
url = 'https://graph.microsoft.com/v1.0/me/todo/lists/{yourId}==/tasks'

# Set your access token here
YOUR_ACCESS_TOKEN_HERE = ''
headers = {
    'Authorization': 'Bearer ' + YOUR_ACCESS_TOKEN_HERE,
    'Content-Type': 'application/json'
}
# Make a GET request to get all tasks in the "thoughts" list
response = requests.get(url, headers=headers, params={'$filter': 'startswith(title, \'Thought\')'})
print(response.json())                                 
tasks = response.json()['value']

# Write the task titles to a .text file
with open('thoughts.txt', 'w') as f:
    for task in tasks:
        f.write(task['createdDateTime'] + '\n\n')
        f.write(task['body']['content'] + '\n\n')