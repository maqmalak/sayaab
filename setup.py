from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sayaab/__init__.py
from sayaab import __version__ as version

setup(
	name="sayaab",
	version=version,
	description="this is clothing bussiness application",
	author="Maqbool Hussain",
	author_email="maqmalak@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
