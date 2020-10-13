import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dmc_remastered",
    version="1.0",
    author="Jake Grigsby",
    author_email="jcg6dn@virginia.edu",
    description="A version of the DeepMind Control Suite with randomly generated graphics, for measuring visual generalization in continuous control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jakegrigsby/dmc_remastered",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "gym",
        "dm_control",
        "dm_env",
        "numpy",
    ],
)
