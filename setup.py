import setuptools

setuptools.setup(
        name="tfrec-utils", # library name will go here
        version="0.5.0", # version info
        author="vwhvpwvk",
        description="Utility functions for reading and writing TFRecords",
        packages=setuptools.find_packages(),
        install_requires=[
            #'tensorflow',
		#'opencv-python-headless',
		#'tqdm'
            ]
)

