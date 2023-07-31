from setuptools import setup, find_packages

setup(
    name="streamlit_motherduck",
    version="0.1",
    author="Patrick Trainer",
    author_email="patrick@patricktrainer.xyz",
    description="A Streamlit component for connecting to MotherDuck",
    keywords=["streamlit", "motherduck", "duckdb"],
    url="https://github.com/patricktrainer/motherduck-connection",
    license="MIT",
    packages=find_packages(),
    install_requires=["duckdb==0.8.1", "streamlit>=1.22.0"],
)
