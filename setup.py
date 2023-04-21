from setuptools import setup, find_packages

setup(
    name='openknowit_kalm_common',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List of dependencies
    ],
    entry_points='''
        [console_scripts]
        openknowit_kalm_common=openknowit_kalm_common.cli:main
    '''
)
