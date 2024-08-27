from setuptools import setup, find_packages

setup(
    name='background_remove_app',
    version='0.1.0',
    description='A Streamlit app that uses a CV model to remove people, cars, and artifacts from image backgrounds.',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'Pillow',  # For image processing
    ],
)