from setuptools import setup

setup(name='braintree',
  version='0.1',
  description='Braintree for Google App Engine',
  url='',
  author='MM',
  author_email='matchman@redso.com.hk',
  license='MIT',
  packages=['braintree'],
  install_requires=[
  'requests',
  'requests-toolbelt',
  ],
  zip_safe=False)
