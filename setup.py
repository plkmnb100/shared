from setuptools import setup

setup(
   name='dblogger',
   version='1.0',
   description='dblogger',
   author='pcy06',
   packages=['dblogger'],  # would be the same as name
   install_requires=['pymysql'], #external packages acting as dependencies
)