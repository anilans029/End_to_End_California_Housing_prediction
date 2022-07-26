import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "End_to_End_California_Housing_prediction"
USER_NAME = "anilans029"

setuptools.setup(
    name= "housing",
    version="0.0.1",
    author=USER_NAME,
    author_email="anilsai029@gmail.com",
    description="A small package for End_to_End_California_Housing_prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    packages=["Housing"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'numpy',
        'matplotlib',
        'tqdm',
        'gunicorn',
        'sklearn',
        'flask'
    ]
)