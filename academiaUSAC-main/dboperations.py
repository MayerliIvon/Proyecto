import json

# Update user status
def UserStatus(user, status):
    # Open the file to read
    with open('users.json', 'r') as file:
        # Load the JSON data
        data = json.load(file)

    # Iterate through the list of dictionaries
    for item in data:
        # Check if the dictionary has the key 'admin'
        if user in item:
            if not status:
                item[user]['confirm'] = False
            else:
                item[user]['confirm'] = True
            

    # Convert the updated data back to a JSON string
    newData = json.dumps(data, indent=4)

    # Open the file to write
    with open('users.json', 'w') as file:
        # Write the updated JSON data to the file
        file.write(newData)

# Add user data
def UserBuild(user, data):
    pass

# Update user data
def UserUpdate(user, key, value):
    pass

# Get user data
def UserData(user):
    pass




