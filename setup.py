from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

packages = find_packages(where=".")

if "tests" in packages:
    packages.remove("tests")

setup(
    name='FCSAppAccessSDK',
    version='1.0.1',
    packages=packages,
    url='https://github.com/CPSuperstore/FangCloudServicesAppAccessSDK',
    license='Apache License 2.0',
    author='CPSuperstore',
    author_email='cpsuperstoreinc@gmail.com',
    description='The SDK for accessing FangCloudServices with Application Access Credentials',
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/CPSuperstore/FangCloudServicesAppAccessSDK/issues",
    },
    keywords=['FANG', 'CLOUD', 'SERVICES', 'FCS', 'SDK', 'USER', 'MANAGEMENT', 'OAUTH2', 'SECURITY'],
    install_requires=[
        "requests"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'License :: OSI Approved :: Apple Public Source License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English'
    ]
)
