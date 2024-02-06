from setuptools import setup, find_packages

exec(open("cloud_diffusion/version.py").read())

setup(
    name="cloud_diffusion",
    packages=find_packages(),
    version=__version__,
    license="MIT",
    description="Diffusion on the Clouds: Short-term solar energy forecasting with Diffusion Models",
    author="Thomas Capelle",
    author_email="tcapelle@pm.me",
    url="https://github.com/tcapelle/cloud_diffusion",
    long_description_content_type="text/markdown",
    keywords=[
        "artificial intelligence",
        "generative models",
        "pytorch",
        "stable diffusion",
    ],
    install_requires=[
        "torch==2.1.0+cu121",
        "fastprogress==1.0.3",
        "fastcore==1.5.29",
        "wandb==",
        "numpy",
        "matplotlib",
        "diffusers==0.26.2",
        "denoising_diffusion_pytorch==1.9.6",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
