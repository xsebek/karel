""" Karel the Robot (now in Python)

See the README in linked GitHub repository for more details.
"""
import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read().replace(
        "images/", "https://raw.githubusercontent.com/xsebek/karel/master/images/"
    )

setuptools.setup(
    name="karel_robot",
    version="1.1.0",
    author="Ondřej Šebek",
    author_email="xsebek@fi.muni.cz",
    description="Karel the Robot simple library and interactive executable",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xsebek/karel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Environment :: Console :: Curses",
        "Topic :: Education",
        "Intended Audience :: Education ",
    ],
    python_requires=">=3.6",
    install_requires=[
        "windows-curses >= 2.2; platform_system=='Windows'"
        ],
    entry_points={"console_scripts": ["karel=karel_robot.run.main:main"]},
)
