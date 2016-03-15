try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Link scraper for Google external link referrences',
    'author': 'Dave Cartwright',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'dave@springload.co.nz',
    'version': '0.2',
    'install_requires': ['requests'],
    'packages': ['GLSapp'],
    'scripts': [],
    'name': 'GLSapp'
}

setup(**config)
