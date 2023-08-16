# Google-PyDrive

1. enable the Google Drive API (https://console.cloud.google.com/apis/library/drive.googleapis.com)
2. set your “User Type” as external (https://console.cloud.google.com/apis/credentials/consent)
3. fill out the OAuth consent screen:
    - Application type: “Web application”
    - Name: Whatever you want, I’ll be using “PyDrive”
    - Authorized JavaScript Origins: “http://localhost:8080”
    - Authorized redirect URIs: “http://localhost:8080/”
    Note the trailing “/” for the Authorized redirect URIs
4. download credentionals (client_secrets.json)
