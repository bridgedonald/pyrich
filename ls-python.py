import os;

def show_items_in_(path):
  for entry in os.listdir(path):
    print(f'{entry}', end="	")
# show_items_in_(".");

def show_only_files_in_(path):
  for entry in os.listdir(path):
    if os.path.isfile((entry)):
      print(f'{entry}')
#=> config.py ls.py Mango.db model.py app.py sample_data.txt 

def show_only_dirs_in_(dir_path):
  for entry in os.listdir(dir_path):
    if os.path.isdir((entry)):
      print(f'{entry}')
#=> templates src 

import stat

def show_stats_of_items_in(path):
    for entry in os.listdir(path):
        statinfo = os.stat(entry)
        print(f'{stat.filemode(statinfo.st_mode)} ', end="")
        print(f'{entry}');

# show_stats_of_items_in(".");


# As a keen observer, you might have noticed that we have to first make a call to os.listdir() to get all the file/directory listings and then another call to os.stat() to get further details about them. Woudn’t it be better if we can get both results in the same pass? Fortunatley in python3.6 and above you can, using the function os.scandir()

def show_stats_of_items_in_1(path):
    total = 0
    for entry in os.scandir():
        print(f'{stat.filemode(entry.stat().st_mode)} ', end="")
        print(f'{entry.name}');

print("fdjfdkfjdkjkfjdkfjkjkdjf")
show_stats_of_items_in_1(".") ;  