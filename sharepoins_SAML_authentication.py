import requests
import credentials
# Credentials is a file where I hardcode usernames and passwords
from requests_ntlm import HttpNtlmAuth

# Authentication config
sharepoint_url = credentials.sharepoint_base_url
username = credentials.sharepoint_user
password = credentials.sharepoint_password
adfs_url = credentials.adfs_url
adfs_username = credentials.adfs_username
adfs_password = credentials.adfs_password

# ADFS authentication form
session = requests.Session()
response = session.get(adfs_url)
login_data = {
    'UserName': adfs_username,
    'Password': adfs_password,
    'AuthMethod': 'FormsAuthentication'
}
response = session.post(adfs_url, data=login_data)

# Extract ADFS authentication token
token_start = response.text.find('<input type="hidden" name="SAMLResponse" value="') + len(
    '<input type="hidden" name="SAMLResponse" value="')
token_end = response.text.find('"/>', token_start)
saml_token = response.text[token_start:token_end]

# NTLM authentication with SharePoint
session.auth = HttpNtlmAuth(username, password)
session.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})

# Post SAML token to authenticate in SharePoint
response = session.post(sharepoint_url, data={'SAMLResponse': saml_token})

# GET for the SharePoint page contect
response = session.get(sharepoint_url + "/_layouts/15/viewlsts.aspx")

# Print page content
print(response.content)
