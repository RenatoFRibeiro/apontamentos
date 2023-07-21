from sharepy import SharePoint

# Replace these values with your SharePoint site URL, username, and password
site_url = "https://your-sharepoint-site.sharepoint.com"
username = "your-username"
password = "your-password"

# Initialize the SharePoint connection
sharepoint = SharePoint(site_url, username, password)

# Specify the SharePoint list name
list_name = "YourListName"

# Get list items from SharePoint
list_items = sharepoint.get_list_items(list_name)

# Print the list data
if list_items.status_code == 200:
    data = list_items.json()
    print(data)
else:
    print(f"Failed to retrieve list data. Status Code: {list_items.status_code}")
