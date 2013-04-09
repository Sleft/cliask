from distutils.core import setup

setup(name='cliask',
      version='0.0.4',
      py_modules=['cliask'],
      data_files=[('', ['LICENSE.org', 'README.org'])],
      description='A module for getting validated user input via the console',
      author='Sleft',
      author_email='fte08eas@student.lu.se',
      license='LICENSE.org',
      url='https://github.com/Sleft/cliask',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Shells',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
      long_description=open('README.org').read())
