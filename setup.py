import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quran.py",
    version="0.1",
    author="Jadtz",
    author_email="amjid482@gmail.com",
    description="An API wrapper for Quran.com written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jadtz/quran.py",
    project_urls={
        "Bug Tracker": "https://github.com/Jadtz/quran.py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
    'certifi==2020.12.5',
    'chardet==4.0.0',
    'idna==2.10',
    'requests==2.25.1',
    'urllib3==1.26.4'
    ]
)