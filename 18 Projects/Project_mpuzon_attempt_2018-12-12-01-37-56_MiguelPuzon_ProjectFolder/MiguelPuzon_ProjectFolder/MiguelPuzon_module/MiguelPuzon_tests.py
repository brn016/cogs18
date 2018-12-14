"""Tests for my functions"""


def test_organize(): 
    assert isinstance(path, str)
    assert isinstance(os.listdir(path), list)
    folder_name = ['pdf', 'pages', 'ipynb'] #use same folder names and range as organize()
    for x in range(0,3): 
        assert os.path.exists(path+folder_name[x])
    assert organize(path) == list_files(path)
    
    
def test_list_files():
    assert isinstance(path, str)
    assert isinstance(os.listdir(path), list)
    
    
def test_create_new_folders():
    assert isinstance(path, str)
    assert isinstance(os.listdir(path), list)
    folder_name = ['pdf', 'pages', 'ipynb']
    for x in range(0,3): 
        assert os.path.exists(path+folder_name[x])
            
            
def test_sort_files(path):
    assert isinstance(path, str)
    assert isinstance(os.listdir(path), list)