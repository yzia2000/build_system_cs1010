For Fellow CEG Students
========================================

Instructions on how to use the template


1. Clone the template into your shell environment.

2. Create a C++ file in the root directory of the template (there is a default file called prog1.cpp)

3. Run: cmake .

4. Run: make

5. An executable with the same name as the cpp file will be generated in the same directory.

In case you have header files or libraries you wish to import into your project:

1. mkdir include

2. Put your header files in the include directory.

3. This makes your project more organized.


Why use this?

In case you have many cpp files you are working on and want to create an executable for every single cpp file (like how we had a makefile for many problems in our cs1010 assignments), this template would allow you to create as many cpp files as you want and create executables for every single cpp file in the root directory. Plus, it will include your header files in every single cpp file that you create. This makes it easier than running: clang++ -g -Wall -Wextra -Wpedantic -Wdocumentation -o [executable name] [cpp file name]
for every cpp file you are working on. Just clone this template once and it  works for all your files.



If you are thinking about using WSL Ubuntu for CS2040C, I have my WSL config that helps a lot in turning your CLI into a more IDE type 
environment. (wsl config)[https://github.com/yzia2000/dotfiles]
