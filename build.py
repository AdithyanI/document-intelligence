import PyInstaller.__main__
import sys
import os

def build():
    # Determine the executable extension based on the OS
    ext = '.exe' if sys.platform.startswith('win') else ''
    
    PyInstaller.__main__.run([
        'cli.py',
        '--onefile',
        '--name=pdf2md' + ext,
        '--clean',
        '--noconsole',
    ])

if __name__ == "__main__":
    build() 