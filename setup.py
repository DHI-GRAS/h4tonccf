from setuptools import setup, find_packages

setup(
    name='h4tonccf',
    version='0.1',
    description='Python wrapper for h4tonccf',
    author='Jonas Solvsteen',
    author_email='josl@dhigroup.com',
    packages=find_packages(),
    include_package_data=True,
    extras_require={
        'test': [
            'pytest']})
