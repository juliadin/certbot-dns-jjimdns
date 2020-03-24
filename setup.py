from setuptools import setup
from setuptools import find_packages

with open('README.md') as file:
    long_description = file.read()

version = '0.0.10'

# Remember to update local-oldest-requirements.txt when changing the minimum
# acme/certbot version.
install_requires = [
    'acme>=0.21.1',
    'certbot>=0.21.1',
    'setuptools',
    'zope.interface',
]

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
]

setup(
    name='certbot-dns-jjimdns',
    version=version,
    description="DNS Authenticator plugin proxying records via SSH",
    url='https://sauce.vm.is.jjim.de/julia/certbot-dns-jjimdns/',
    author="Julia Brunenberg",
    license='PD',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    long_description=long_description,
    long_description_content_type='text/x-md',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'docs': docs_extras,
    },
    entry_points={
        'certbot.plugins': [
            'dns-jjimdns = certbot_dns_jjimdns.dns_jjimdns:JJIMDNS_Authenticator',
        ],
    },
)
