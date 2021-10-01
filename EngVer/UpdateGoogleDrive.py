import os
from pydrive import auth, drive


def UpdateFile(file_id, src_path):
  f = drive.CreateFile({'id': file_id})
  f.SetContentFile(src_path)
  f.Upload()


def CreateFile(parent_folder_id, file_name, src_path):
  f = drive.CreateFile({
    'title': file_name,
    'parents': [{'id': parent_folder_id}],
  })
  f.SetContentFile(src_path)
  f.Upload()


FOLDER_ID       = '10CgNO2GlpE6MgC4B-WWOFdWxPMBMfeIp'
RESUME_PATH     = './EngVer.pdf'
DEST_FILE_NAME  = 'Resume-NingqiWang.pdf'


g_auth = auth.GoogleAuth()
g_auth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = drive.GoogleDrive(g_auth)


# Create or update the resume
file_list = drive.ListFile({
  'q': f"'{FOLDER_ID}' in parents and trashed=false"
}).GetList()
for f_data in file_list:
  f_name = f_data['title']
  if f_name == DEST_FILE_NAME:
    UpdateFile(f_data['id'], RESUME_PATH)
    os._exit(0)


# At this point, we can make sure that the .pdf file has not been uploaded yet
CreateFile(FOLDER_ID, DEST_FILE_NAME, RESUME_PATH)
