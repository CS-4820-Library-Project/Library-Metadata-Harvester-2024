# Library Metadata Harvester

## Description

The Library Metadata Harvester is a versatile cross-platform desktop application designed to streamline the collection and management of library metadata. It is crafted to aid librarians and researchers in efficiently gathering critical data such as ISBNs, OCNs and LC call numbers, enhancing the organization and accessibility of library resources.

This program uses a combination of public APIs along with webscraping some public Blacklight-based academic library catalogs to obtain the data.  If you also want to use Z39.50, see Melissa's other Metadata project. This is the one created by CS4820 Winter 2024 Team 2.

## Features

- Cross-platform compatibility: Works seamlessly on Windows, Mac, and Linux.
- User-friendly GUI: Simplifies the process of metadata input and handling.
- Direct integration with external APIs for extensive metadata retrieval.
- Local SQLite database support for persistent data storage.
- Metadata export capability in a user-friendly tab-delimited format.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x: The core programming language used for the application. On some systems, you may need to use `python3` instead of `python` to invoke Python 3.
- Pip: The Python package installer, used for managing software packages. Depending on your system, you might need to use `pip3` if you have both Python 2 and Python 3 installed.
- Google Chrome browser

### Link to Executables
- Click on your OS and download the executable located at the link

   - **Windows**: [Download Windows Executables](https://drive.google.com/drive/folders/1XN9e6EUeQKbHZkrM7AIU404lcs2sS0OE?usp=drive_link)
  
   - **Linux**: [Download Linux Executables](https://drive.google.com/drive/folders/1qbhzticMvkSbts3eexqVF1R1NeaqH9nc?usp=drive_link)
  
   - **Mac**: [Download macOS Executables](https://drive.google.com/drive/folders/1m2Y8I4PRfFwA0lBsBIMksGaQsqv9voxf?usp=drive_link)

### Setup Instructions

1. Obtain the source code by cloning the repository or downloading the source files.
2. Open a terminal or command prompt and navigate to the root directory of the project.
3. Install the necessary Python dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

   Or, if your system requires, use `pip3`:

   ```bash
   pip3 install -r requirements.txt
   ```

4. For building the application into an executable, run the build script. The executable will be located in the `dist` directory after the script completes:

   ```bash
   python build.py
   ```

   On some systems, you may need to use `python3`:

   ```bash
   python3 build.py
   ```

   The build script supports Linux, Windows, and macOS.

## Running Tests

For running tests, use the `run_tests.py` script:

```bash
python run_tests.py
```

On some systems, you may need to use `python3`:

```bash
python3 run_tests.py
```

## Supported Operating Systems

The application and build scripts are supported on the following operating systems:

- Linux
- Windows
- macOS
