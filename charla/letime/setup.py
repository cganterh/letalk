from setuptools import setup

setup(
    name='letime',
    version='0.1.0',
    py_modules=['letime'],
    entry_points={
        'le.handlers': [
            'letime_handler = letime:_handler',
        ],
    },
)