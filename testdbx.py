from importlib.abc import ResourceLoader
import dropbox
import os

flist = []



token = os.environ.get('TOKEN')
token = 'sl.BJl0TJ_paTytFLHhdYWsGbxd7tASp2R--L8YpxMuASJJGEpeLOJf7t6P0vBj3Xy_ogcnbjuYe1ygyxLQarscg4mHDwe7P7PNJ-Rti5qqszh-MSUh3Sollmbpj31VE-Hp7XK30K4'
dbx = dropbox.Dropbox(token)
# dbx.sharing_share_folder('/maricunga')
# dbx.files_create_folder('/borrar')
# DEST = '/Aplicaciones/gestor-econsult/'
# SOURCE = '/home/fdo/code/gestor-django/gestorbackend/'
# dbx.files_copy('/borrar/folder1/'+'manage.py', '/borrar/folder2/manage.py')
dbx.files_download_to_file('/home/fdo/code/gestor-django/gestorbackend/'+'requirements.txt', '/borrar/folder2/requirements.txt')
# dbx.files_create_folder('/borrar')


# def process_entries(entries):
#     for entry in entries:
#         if isinstance(entry, dropbox.files.FileMetadata):
#             flist.append(entry.name)
#             dbx.files_download_to_file('/Users/fela/Downloads/dropbox/'+entry.name, '/'+entry.name)

# result = dbx.files_list_folder("", recursive=True)
# print(result)