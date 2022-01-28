#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"Initialize an OpenCV C++ project with git, CMake and Vim"

__author__ = 'QidiLiu'

import os

# Enter the name
project_name = input('| -Qidi- | Enter OpenCV C++ project name: ')
if project_name == '':
    print('| -Qidi- | Bye~')
    os._exit(0)
print(f'| -Qidi- | Project name: {project_name}.')

# Copy template of CMakeList.txt and main.cpp to project folder
project_dir = f'~/Work/{project_name}'
os.system('mkdir ' + project_dir)
os.system('cp ~/.SpaceVim.d/autocreate/CMakeLists.txt ' + project_dir)
os.system('cp ~/.SpaceVim.d/autocreate/main.cpp ' + project_dir)
#os.system('cmake -S ' + project_dir + ' -B ' + project_dir)
print('| -Qidi- | CMake configured.')

# Initialize git and configure "exclude/info" automatically
os.system('git -C ' + project_dir + ' init')
home_path = os.path.expanduser('~')
with open(home_path+f'/Work/{project_name}/.git/info/exclude', 'a') as exclude_file:
    exclude_file.write('CMake*\ncmake*\nMakefile\nmain')
os.system('git -C ' + project_dir + ' add -A')
os.system('git -C ' + project_dir + ' commit -m "first commit"')
print('| -Qidi- | Git initialized.')

# Open new project with Vim
os.system('vim ' + project_dir + '/main.cpp')

# Quit
os._exit(0)
