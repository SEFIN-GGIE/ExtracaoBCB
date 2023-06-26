import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
from googleapiclient.errors import HttpError

class GoogleCloudHandler:
    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        self.service = self.build_drive_service()

    def build_drive_service(self):
        credentials = service_account.Credentials.from_service_account_file(
            self.credentials_file,
            scopes=['https://www.googleapis.com/auth/drive']
        )
        return build('drive', 'v3', credentials=credentials)

    def upload_file_to_drive_folder(self, file_path, folder_id):
        file_name = os.path.basename(file_path)
        print(file_name)
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path)

        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        print('File uploaded. File ID: {}'.format(file.get('id')))