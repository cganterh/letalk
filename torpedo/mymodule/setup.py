from setuptools import setup


setup(
    name='mymodule',
    version='0.1.0',
    author='cris',
    author_email='cganterh@gmail.com',
    url='http://github.com/cganterh',
    py_modules=['mymodule'],
    entry_points={
        'my_ep_group': [
            'my_ep_name = mymodule:some_object',
            'my_other_ep = mymodule:other_object',
        ],
    },
)
