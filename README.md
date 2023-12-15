# SortStream

SortStream is a Python script designed to automatically organize files in a directory, particularly useful for managing downloads. It's ideal for users who frequently download various file types and want to keep their workspace organized.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Using the Executable](#using-the-Executable)
- [Features](#features)
- [Contributing](#contributing)
- [Support](#support) 
- [License](#license)

## Installation

Requirements:
* Python 3.x

Steps:
1. Clone this repository: `git clone git@github.com:TurboTeam335/SortStream.git`

2. Navigate to the repository directory: `cd sortstream`
3. Set up a virtual environment (optional but recommended):
   - Create the virtual environment: `python3 -m venv venv`
   - Activate the virtual environment:
     - On macOS and Linux: `source venv/bin/activate`
     - On Windows: `.\venv\Scripts\activate`

4. Install dependencies: `pip install -r requirements.txt`

## Usage

After installation, ensure your virtual environment is activated. If not, follow the activation steps in the Installation section.

To run the script, navigate to the repository directory and execute: `python main.py`


The script monitors your Downloads folder. New files are automatically categorized and moved to appropriate subfolders based on file type, as configured in `config.py`.

To deactivate the virtual environment when you're finished, simply run: `deactivate`

## Using the Executable

For users who prefer not to install Python and dependencies, a pre-built executable version of SortStream is available.

### Downloading the Executable
1. Go to the [Releases](https://github.com/TurboTeam335/SortStream/releases) section of the SortStream GitHub repository.
2. Download the latest release for your operating system.
3. Unzip the downloaded file.

### Running the Executable
- On macOS and Linux: 
  - Open Terminal.
  - Navigate to the directory containing the unzipped executable.
  - Run the executable with `./main` (assuming `main` is the executable name).
- On Windows:
  - Navigate to the directory containing the unzipped executable in File Explorer.
  - Double-click the `main.exe` file to run it.

The executable functions just like the Python script, automatically organizing files in the specified directory.


## Features

* Automatic file sorting by type
* Customizable file type categorization

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you'd like to change. Ensure to update tests as appropriate.

## Support

For support, please open an issue on the GitHub repository.

## License

[MIT License](LICENSE) 