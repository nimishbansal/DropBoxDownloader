import dropbox

SAVE_PATH = "/home/nimish/PycharmProjects/freelancer/cangetprojects/"
dbx = dropbox.Dropbox("f-KS6Mn4phcAAAAAAAAA5hIw4MCEgnsFDKO2fkMZ3R801SQiFnFJNlLnTWdkT0NI")
dbx.users_get_current_account()
search_input = input()
# search_input = "images"
results = dbx.files_search(path="", query=search_input)
# results = dbx.files_search(path="/bbcfirstwebsite", query=search_input)
ctr = 0
for j in results.matches:
    if type(j.metadata) == dropbox.files.FolderMetadata:
        ctr += 1
        file_name = j.metadata.name + "-result-" + str(ctr) + ".zip"
        print(j.metadata.path_lower)
        folder_download = dbx.files_download_zip_to_file(SAVE_PATH + file_name, j.metadata.path_lower)
