import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="analog_mod-rophad", # Replace with your own username
    version="0.0.1",
    author="Rohan Phadnis",
    author_email="rohan.phadnis,usa@gmail.com",
    description="A library that allows easy PWM functionalities with the Jetson.GPIO and the RPi.GPIO libraries.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
