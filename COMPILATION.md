### Thank you for displaying interest in compiling youtube-downloader!

# Compiling youtube-downloader 101
### Step 1. Install required dependencies:

You need [PyQt5](https://pypi.org/project/PyQt5/) and [PyTube](https://pypi.org/project/pytube/) to compile youtube-downloader. If you want to compile it to .exe, [PyInstaller](https://www.pyinstaller.org/) is recommended.
<br>**NOTE:** If you're using an older version of PyTube, please update it. See [this](https://github.com/pytube/pytube/issues/990) for more details.

### Step 2. Compile it.

For compilation, as mentioned above, we recommend PyInstaller. You can find documentation for PyInstaller [here](https://github.com/pytube/pytube/tree/master/docs).
<br>**NOTE:** After a successful compilation, you may encounter this error: `PyQt5 not found .` <br>In such case, you should pass the `--hidden-import Pyqt5` argument to the compiler.
