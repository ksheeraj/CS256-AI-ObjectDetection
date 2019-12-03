import os 
  
# This is to get the directory that the program  
# is currently running in. 
dir_path = os.path.dirname(os.path.realpath(__file__)) 
#i = 1
for root, dirs, files in os.walk(dir_path): 
    for file in files:  
        if file.endswith('_fake_B.jpg'):
            subString = file.replace('_fake_B', '')
            my_dest = "/fakeImg/" + subString
            my_source = file
            my_dest = dir_path + my_dest
            os.rename(my_source, my_dest)
