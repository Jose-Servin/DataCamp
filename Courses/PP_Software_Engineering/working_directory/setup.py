from setuptools import setup

setup(name='my_package',
      version='0.0.1',
      description='An example package from DataCamp',
      author='Jose Servin',
      author_email='servin@noemail.com',
      packages=['my_package'],
      install_requires=['matplotlib', 'numpy==1.15.4', 'pycodestyle>=2.4.0']
      )
