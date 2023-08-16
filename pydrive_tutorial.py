# -*- coding: utf-8 -*-
"""pydrive-tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yuphSRhaH0jvhVUtTX_bNV4u_3ylC0zl
"""

# Authenticate your Google account (this will open a window in a web brower)
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

# Create GoogleDrive instance
from pydrive.drive import GoogleDrive
drive = GoogleDrive(gauth)

# Create and upload a simple file
file = drive.CreateFile({'title': 'My Awesome File.txt'})
file.SetContentString('Hello World!') # this writes a string directly to a file
file.Upload()

# Search for every file in your Drive not in the trash
#file_list = drive.ListFile({'q': 'trashed=false'}).GetList()

#for file in file_list:
#    print(file['title'], file['id'])

# Search for a file with a title that contains "Hello world" and is not in the trash
# For a full list of how to structure queries, see: https://developers.google.com/drive/api/v2/search-files#python

file_list = drive.ListFile({'q': "title contains 'My Awesome File' and trashed=false"}).GetList()
print(file_list[0]['title']) # should be the title of the file we just created
file_id = file_list[0]['id'] # get the file ID

# Download the basic file we just made
file = drive.CreateFile({'id': file_id})
file.GetContentFile('my-awesome-file.txt') # downloads 'My Awesome File.txt' as 'my-awesome-file.txt'

file.Trash() # put the simple file in Google Drive trash (not yet deleted)
file.UnTrash() # recover from trash
file.Delete() # permanently delete (downloaded copy is saved)

# Upload arbitrary file
cool_image = drive.CreateFile()
cool_image.SetContentFile('my-awesome-file.txt') # load local file data into the File instance
cool_image.Upload() # creates a file in your drive with the name: my-awesome-file.txt

# Create folder
folder = drive.CreateFile({'title': 'My Awesome Folder 123', "mimeType": "application/vnd.google-apps.folder"})
folder.Upload()

# Upload file to folder
folder = drive.ListFile({'q': "title = 'My Awesome Folder 123' and trashed=false"}).GetList()[0] # get the folder we just created
file = drive.CreateFile({'title': "I'm in a folder!.txt", 'parents': [{'id': folder['id']}]})
file.Upload()

# Save Credentials (for use in Kaggle or elsewhere)
gauth.SaveCredentialsFile("mycreds.txt")