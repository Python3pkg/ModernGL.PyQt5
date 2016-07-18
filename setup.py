import platform

target = platform.system().lower()

from setuptools import setup

Version = '0.1.1'

ShortDescription = ''

LongDescription = '''
'''

Classifiers = [
	'Development Status :: 1 - Planning',
]

Keywords = [
	'ModernGL',
	'PyQt5',
	'Qt5',
	'Qt',
	'modern OpenGL',
	'OpenGL',
]

args = {
	'name' : 'ModernGL.PyQt5',
	'version' : Version,
	'description' : ShortDescription,
	'long_description' : LongDescription,
	'url' : 'https://github.com/cprogrammer1994/ModernGL.PyQt5',
	'download_url' : 'https://github.com/cprogrammer1994/ModernGL.PyQt5/releases',
	'author' : 'Szabolcs Dombi',
	'author_email' : 'cprogrammer1994@gmail.com',
	'license' : 'MIT',
	'classifiers' : Classifiers,
	'keywords' : Keywords,
	'packages' : [],
	'ext_modules' : [],
	'platforms' : ['any'],
	'install_requires' : ['ModernGL', 'PyQt5']
}

if target == 'windows':
	args['zip_safe'] = True

setup(**args)
