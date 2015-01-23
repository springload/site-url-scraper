try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Jazz festival link scraper',
    'author': 'Dave Cartweright',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'dave@springload.co.nz',
    'version': '0.1',
    'install_requires': ['unittest'],
    'packages': [''],
    'scripts': [],
    'name': 'GLSapp'
}

setup(**config)