from setuptools import setup

# 'Import' __version__
exec(open('venmo/_version.py').read())

requirements = [
    'requests>=2.9.1',
]

setup(
    name='venmo',
    version=__version__,  # noqa
    description='Venmo CLI',
    url='http://github.com/zackhsi/venmo',
    author='Zack Hsi',
    author_email='zackhsi@gmail.com',
    license='MIT',
    packages=['venmo'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'venmo = venmo.cli:main',
        ],
    },
)
