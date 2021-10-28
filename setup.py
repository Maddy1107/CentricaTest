import setuptools
from setuptools import setup

# calling the setup function
setup(name="google_scrapper",
      version='1.0.0',
      description='Search Google to extract links',
      author='Nilankar Deb',
      packages=['src'],
      install_requires=['requests', 'bs4'],
      python_requires='>3.6'
      )
