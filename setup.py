from setuptools import find_packages, setup

# To create an executable file in venv:
# pip install -e wc_tool
setup(
    name='pywc',
    version='0.0.1',
    packages=find_packages('wc'),
    # install_requires=[],
    entry_points={
        'console_scripts': [
            'ccwc=wc.app:main',
        ]
    }
)
