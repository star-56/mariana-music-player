import os
from ruamel.yaml import YAML

yaml = YAML(typ='safe')

curdir=os.path.dirname(__file__)
os.chdir(curdir)

def fbs(about): # First boot setup
    print(f"Welcome to Mariana Player v{about['ver']['maj']}.{about['ver']['min']}.{about['ver']['rel']}")

    locally_stored_permission = input("Do you have any locally stored/downloaded music files? (y/n): ").lower().strip()
    while locally_stored_permission not in ['y', 'n', 'yes', 'no']:
        locally_stored_permission = input("[INVALID RESPONSE] Do you have any locally stored/downloaded music files? (y/n): ").lower().strip()

    if locally_stored_permission in ['yes', 'y']:
        locally_stored_permission = True
    else:
        locally_stored_permission = False

    local_file_dirs = []

    if locally_stored_permission:
        print("Please enter absolute path of your music directories one by one:")
        print("When done, just write \"xxx\"")
        n=0
        while True:
            n+=1
            local_file_dir = input("  Enter directory path {n}: ").lower().strip()
            if local_file_dir != 'xxx':
                if os.path.isdir(local_file_dir): local_file_dirs.append(local_file_dir)
                else: print("This directory does not exist, please retry...")
            else:
                print(f"Saving directory paths in library file\n  @location: {os.path.join(curdir, 'lib.lib')}")
            
            local_file_dir = list(set(local_file_dir))
            
            with open("lib.lib", 'a') as libfile:
                for dir in local_file_dir:
                    libfile.writeline(dir+'\n')


    about['first_boot'] = False
    with open('about/about.info', 'w') as about_file:
        yaml.dump(about, about_file)

