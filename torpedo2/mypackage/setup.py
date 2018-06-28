from setuptools import setup


setup(
    name='mypackage',
    version='0.1.0',
    author='cris',
    author_email='cganterh@gmail.com',
    url='http://github.com/cganterh',
    py_modules=['mypackage'],
    entry_points={
        'my_ep_group': [
            'ep1 = mypackage:string_1',
            'ep2 = mypackage:string_2',
        ],
    },
)