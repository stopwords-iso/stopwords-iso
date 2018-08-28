from setuptools import setup

setup(name='stopwordsiso',
      version='0.1',
      description='Collection of stopwords for multiple languages. Using ISO 639-1 language code.',
      url='http://github.com/thothmedia/stopwords-iso',
      author='Gene Diaz and Arthit Suriyawongkul',
      author_email='arthit.s@wisesight.com',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='stopwords language',
      license='MIT',
      packages=['stopwordsiso'],
      include_package_data=True,
      zip_safe=False)
