from setuptools import setup, find_packages

setup(
    name='chartsnap',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium'
    ],
    author="Aniket Inamdar",
    author_email="aniketinamdar02@gmail.com",
    description="Python module that scrapes tradingview charts when appropriate inputs are given.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
    "console_scripts": [
        "chart-snap = chartsnap:get_chart",
    ],
},    
)
