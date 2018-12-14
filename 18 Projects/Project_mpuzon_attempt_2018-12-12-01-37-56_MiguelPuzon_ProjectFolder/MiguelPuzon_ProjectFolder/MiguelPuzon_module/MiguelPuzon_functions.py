"""A collection of functions for my project"""


def organize(path): 
    list_files(path)
    create_new_folders(path)
    sort_files(path)
    
    
def list_files(path):
    file_list = os.listdir(path)
    print(file_list)
    
    
def create_new_folders(path):
    folder_name = ['pdf', 'pages', 'ipynb']
    for x in range(0,3): 
        if not os.path.exists(path+folder_name[x]): 
            os.makedirs(path+folder_name[x])
            
            
def sort_files(path):
    file_list = os.listdir(path)
    for files in file_list:
        if ".pdf" in files and not os.path.exists(path+'pdf//'+files):
            shutil.move(path+files, path+'pdf//'+files)
        if ".pages" in files and not os.path.exists(path+'pages//'+files):
            shutil.move(path+files, path+'pages//'+files)
        if ".ipynb" in files and not os.path.exists(path+'ipynb//'+files):
            shutil.move(path+files, path+'ipynb//'+files)