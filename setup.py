from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name='AskOmics website',
    version='0.0.1',
    description='AskOmics website',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
    maintainer='Xavier Garnier',
    url='https://askomics.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
