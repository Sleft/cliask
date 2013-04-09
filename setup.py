from distutils.core import setup
import sys

if sys.version_info <= (3, 2, 3):
    sys.stderr.write("cliask requires Python 3.2.3 or newer.\n")
    sys.exit(-1)

setup(name='cliask',
      version='0.0.2',
      py_modules=['cliask'],
      description="A module for getting validated user input via the console",
      author="Sleft",
      author_email="fte08eas@student.lu.se",
      license="Public domain",
      url="https://github.com/Sleft/cliask",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: System :: Shells",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
      long_description="""\
A Python module for getting validated user input via the console which is meant to ease the process of building command line interfaces. Provides the function ask which will ask for input until a valid response is given. Also provides the function agree which will ask for input until the answer is yes or no. Both functions are similar to and inspired by the functions with the same name in the Ruby library HighLine. The following code gives a peek of how the functions can be used:


  import cliask
  
  animal = cliask.ask('Cow or cat? ',
                      validator=('cow', 'cat'),
                      invalid_response='You must say cow or cat')
  yn = cliask.agree('Yes or no? ')
  
  print(animal)
  print(yn)
"""
      )
