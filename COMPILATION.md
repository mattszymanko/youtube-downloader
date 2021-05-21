# Compilation of youtube-downloader
Step 1. Install required dependencies:

For compiling youtube-downloader you need PyQt5 and PyTube. If you want to compile this file to .exe, PyInstaller is recommended.
**NOTE:** If you use an older version of PyTube please update it. See https://github.com/pytube/pytube/issues/990 for more info.

Step 2. Compile it.

For compilation, as mentioned above, we recommend PyInstaller. You can find documentation for pyinstaller [here](https://github.com/pytube/pytube/issues/990).
**NOTE:** After succesfull compilation, you might run into error like this: `PyQt5  not found.` In such case you should pass the `--hidden-import Pyqt5` argument to the compiler.
