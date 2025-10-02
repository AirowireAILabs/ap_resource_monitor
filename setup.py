from setuptools import setup, find_packages

setup(
    name="ap_resource_monitor",
    version="0.1.0",
    description="WiFi Access Point Resource Monitoring and Health Analysis Library",
    author="AirowireAILabs",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    python_requires='>=3.6',
    keywords=['wifi', 'resource', 'monitoring', 'health', 'analysis', 'network'],
    license="MIT",
    url="https://github.com/AirowireAILabs/ap_resource_monitor",
)
