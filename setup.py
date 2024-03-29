import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()



__version__ = "0.0.0"

## Repo name is Project Name
REPO_NAME = "Modular_Coding_Project_1"
AUTHOR_USER_NAME = "Amrinder"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "singhamrinder50@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for ML app",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)