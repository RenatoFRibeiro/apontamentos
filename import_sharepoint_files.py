import credentials
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

ctx_auth = AuthenticationContext(credentials.sharepoint_base_url)
ctx_auth.acquire_token_for_user(credentials.sharepoint_user, credentials.sharepoint_password)
ctx = ClientContext(credentials.sharepoint_base_url, ctx_auth)


file = File.open_binary(ctx, credentials.folder_in_sharepoint)
file.download("./downloaded_file.txt")  # Specify the local path to save the downloaded file

print("File downloaded successfully.")
