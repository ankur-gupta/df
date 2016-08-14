from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='df',
      version='0.1',
      description='An easier-to-use implementation of dataframes.',
      long_description=readme(),
      url='http://github.com/ankur-gupta/df',
      author='Ankur Gupta, Bryson Hagerman',
      author_email='ankur@perfectlyrandom.org, brysonova@gmail.com',
      keywords='dataframes pandas groupby apply custom function',
      license='MIT',
      packages=['df'],
      zip_safe=False,
      install_requires=[
          'pandas',
      ])
