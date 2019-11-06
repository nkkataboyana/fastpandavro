from setuptools import setup

setup(name='fastpandavro',
      version='0.1',
      description='Parallel conversion of Avro file to Pandas dataframe and conversion of pandas dataframe to avro file',
      url='https://github.com/deepakagrawal/fastpandavro',
      author='Deepak Agrawal',
      author_email=['agrawal.deepankur@gmail.com','deepak.agrawal@aa.com'],
      license='MIT',
      packages=['fastpandavro'],
      zip_safe=False,
      install_requires=['fastavro', 'joblib'])
