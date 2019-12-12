from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='agolbackup',
      version='0.2',
      description='Python backup automation for AGOL',
      long_description=readme(),
      url='https://github.com/ErikKBethke/agolbackup',
      author='ErikKBethke',
      author_email='erik.k.bethke@gmail.com',
      license='GNU',
      test_suite='nose.collector',
      tests_require=['nose'],
      keywords='tableau xml workbook',
      include_package_data=True,
      packages=['agolbackup'],
      install_requires=[
      'lxml',
    ],
    zip_safe=False
)
