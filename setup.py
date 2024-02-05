import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TplinkRoutergdpr",
    version="0.1",
    author="Simon ZAbienski",
    author_email="tcollect@szab.de",
    description="TP-Link Router GDPR API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.dev/waffelheld/TP-Link-gdpr-api/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests', 'pycryptodome', 'macaddress'],
    python_requires='>=3.10',
)