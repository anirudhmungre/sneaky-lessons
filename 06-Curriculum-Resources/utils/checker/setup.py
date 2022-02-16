from setuptools import setup

setup(
    name='checker',
    version='0.1',
    py_modules=['checker'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        checker=checker:cli
    ''',
)
