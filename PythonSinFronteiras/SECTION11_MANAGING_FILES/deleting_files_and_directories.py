import os

try:
    os.remove('delete_this_file_10')
    os.renames('delete_this_file_7', 'this_file_has_been_renamed')
    os.rmdir('delete_this_folder_7')
except PermissionError:
    pass
except FileNotFoundError:
    pass

