from setuptools import setup, find_packages

setup(
    name='stepcapture',
    version='0.4.0',
    description='轻量级屏幕操作步骤记录工具，支持截图、圈注、气泡注释和导出',
    author='YourName',
    author_email='you@example.com',
    url='https://github.com/yourname/stepcapture',
    packages=find_packages(exclude=('tests', 'scripts')),
    include_package_data=True,
    install_requires=[
        'PySimpleGUI>=4.45.0',
        'pynput>=1.7.6',
        'mss>=8.0.1',
        'Pillow>=9.4.0',
        'PyYAML>=6.0'
    ],
    entry_points={
        'gui_scripts': [
            'stepcapture=stepcapture.cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.7'
)
