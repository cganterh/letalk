from setuptools import setup

setup(
    name='letime',
    version='0.1.0',
    author='cris',
    author_email='cganterh@gmail.com',
    url='http://github.com/cganterh',
    py_modules=['letime'],
    entry_points={
        'le.handlers': ['le_time_handler = letime:_handler'],
    },
)
