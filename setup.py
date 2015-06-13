try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

kw = {
    'name': 'draw',
    'version': '0.0.1',
    'description': 'A drawing tool for IPython',
    'long_description': "",
    'author': 'Naoki Nishida',
    'author_email': 'domitry@gmail.com',
    'license': 'MIT License',
    'url': 'https://github.com/domitry/draw',
    'keywords': 'data visualization',
    'classifiers': (
        'License :: OSI Approved :: MIT License'
    ),
    'packages': ['draw'],
    'install_requires': (
        'ipython'
    ),
    'zip_safe': True,
}

setup(**kw)
