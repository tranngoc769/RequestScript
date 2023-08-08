from setuptools import setup

APP = ['api.py']  # Replace 'your_script.py' with the actual name of your script
DATA_FILES = []  # Add any additional data files your script depends on

OPTIONS = {
    'argv_emulation': True,  # This helps your application to work correctly with command-line arguments
    'packages': [],          # Add any additional packages your script needs
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)