from setuptools import setup, find_packages

setup(
    name='visualization_tests',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your project's core dependencies here
        'dash',
    ],
    extras_require={
        'testing': [
            'dash[testing]',  # Include dash testing support
            'pytest',
            # any other testing libraries you might need
        ],
    },
)