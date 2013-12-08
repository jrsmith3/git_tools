from distutils.core import setup

setup(name='git_tool',
      version='0.0.1',
      author='Joshua Ryan Smith',
      author_email='joshua.r.smith@gmail.com',
      packages=['gittool'],
      url='https://github.com/jrsmith3/git_tools',
      description='tools for managing many git repositories',
      install_requires=[
        'gittle',
        ],
      test_suite='nose.collector',
      tests_require=['nose'],
      license='MIT',
      zip_safe=False)