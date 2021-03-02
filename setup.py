from setuptools import find_packages, setup
setup(
    name="hyperbolic_numbers",
    packages=find_packages(include=['hyperbolic_numbers']),
    version="0.1.0",
    description="Library for hyperbolic numbers",
    author="Frank Zimmer",
    license="MIT",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)