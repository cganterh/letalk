from setuptools import setup

setup(
    name='mypackage',
    version='0.1.0',
    py_module=['mypackage'],
    entry_points={
        'my_ep_group': [
            'my_ep_name = mypackage:string_1',
        ],
    },
)