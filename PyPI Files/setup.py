from setuptools import setup

rst = []
with open('/Users/firsttry/Desktop/Image/README.rst', 'r') as file:
    for line in file:
        rst.append(str(line))
ld = ''
for i in rst:
    ld += i + '\n'

setup(
    name = 'image-modifier',
    version = '3.0',
    license = 'LPPL-1.3c',
    description = 'A python library for modifying .jpg images using PIL',
    long_description = ld,
    author = 'RandomKiddo',
    author_email = 'nghugare2@outlook.com',
    url = 'https://github.com/RandomKiddo/image-modifier',
    download_url = 'https://github.com/RandomKiddo/image-modifier/archive/v3.0.tar.gz',
    keywords = ['PYTHON', 'IMAGE', 'FILTER'],
    install_requires = [
        'wheel',
        'warnings',
        'PIL'
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: LaTeX Project Public License v1.3c',
        'Programming Language :: Python :: 3.8'
    ]
)