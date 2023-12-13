# SortStream

SortStream is a Python script designed to automatically organize files in a directory, particularly useful for managing downloads. It's ideal for users who frequently download various file types and want to keep their workspace organized.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
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

To run the script, navigate to the repository directory and execute: `python -m sortstream`


The script monitors your Downloads folder. New files are automatically categorized and moved to appropriate subfolders based on file type, as configured in `config.py`.

To deactivate the virtual environment when you're finished, simply run: `deactivate`

## Features

* Automatic file sorting by type
* Customizable file type categorization

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you'd like to change. Ensure to update tests as appropriate.

## Support

For support, please open an issue on the GitHub repository.

## License

[MIT License](LICENSE) 