from setuptools import setup, find_packages

setup(
    name='shelter',
    version='1.0',

    # Author details
    author='Henk Griffioen',
    author_email='henkgriffioen@godatadriven.com',

    packages=find_packages(include=['shelter']),
    
    setup_requires=["pandas","pytest-runner"],
    tests_require=["pytest", "pytest-flake8", "pytest-cov"],
)
