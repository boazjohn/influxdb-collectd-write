# -*- coding: utf-8 -*-

from setuptools import setup

version = '0.1'

# Forking - using 0.8 legacy client
setup(name='influxdb-collectd-write',
      version=version,
      description='Collectd Python plugin for writing to InfluxDB',
      long_description=open('README.rst').read(),
      keywords='',
      author='Jason Kölker',
      author_email='jason@koelker.net',
      url='https://github.com/jkoelker/influxdb-collectd-write.git',
      license='MIT',
      py_modules=['write_influxdb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'influxdb==0.4.1',
          'Monotime',
          'requests',
      ],
      )
