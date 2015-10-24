try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
        'description': 'circle: a code snippet managment tool',
        'author': 'Zeyuan Hu',
        'url': 'https://github.com/xxks-kkk/circle',
        'download_url': 'https://github.com/xxks-kkk/circle',
        'author_email': 'ferrishu3886@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['circle'],
        'scripts': [],
        'name': 'circle'
        }

setup(**config)
