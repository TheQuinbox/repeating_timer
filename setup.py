from setuptools import setup, find_packages

setup(
	name="repeating_timer",
	version=0.2,
	author="Quin Marilyn",
	author_email="quin.marilyn05@gmail.com",
	description="Run a function over and over in a thread",
	long_description=open("readme.md", "r").read(),
	long_description_content_type="text/markdown",
	url="http://github.com/TheQuinbox/repeating_timer",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Development Status :: 5 - Production/Stable",
		"Topic :: Utilities",
	],
	python_requires=">=3",
)
