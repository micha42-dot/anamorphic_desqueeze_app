The Desqueeze-App is a simple command-line tool that allows you to horizontally desqueeze images that were shot with anamorphic lenses. It restores the correct aspect ratio of squeezed images and can be used in batch mode on multiple files. The program supports common image formats including JPG, PNG, BMP, and TIFF. It comes with preset desqueeze factors of 1.25, 1.33 (which is the default), 1.5, and 1.8, while also allowing you to enter a custom factor if needed.

You can choose the output format for the processed images. By default, the original format is preserved, but you may also export to JPG with configurable quality (95 percent is the default) or to PNG. The application preserves the original file names and appends the suffix “_Desq” to them. If the program is run multiple times on the same files, it automatically adds numbers to the suffix such as “_Desq2” or “_Desq3”. Whenever possible, EXIF orientation and ICC profiles are preserved.

The Desqueeze-App is designed for efficient batch processing and supports optional multithreading for faster execution. It also includes a built-in self-test that generates dummy images to verify that the program works correctly.

In addition to the Python script, a pre-built Windows executable file is available so that users can run the program without installing Python or additional dependencies. This makes it convenient for non-technical users who just want to drag and drop their images and get corrected results.

To install the application, you simply clone the repository and install the dependencies listed in the requirements file, which at present includes only Pillow. Once installed, you can run the tool with default settings to desqueeze images with a factor of 1.33, or you can specify presets or custom factors along with your choice of export format. Example commands are provided in the documentation to show how to export as JPG with a specific quality, how to apply a custom factor with PNG export, and how to run the self-test mode.


The project requires Python version 3.9 or higher. It is open source and distributed under the Apache License 2.0.
