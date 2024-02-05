# Media-News

## List of contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Author](#author)


## Prerequisites

- Python 3.x
- Required Python libraries (install via `pip install -r requirements.txt`):
  - `tqdm`
  - `requests`
  - `beautifulsoup4`


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aditi-Mokashi/Media-News-Scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Media-News-Scraper-main
   ```
3. Setup virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate virtual environment:
   ```bash
   source venv/Scripts/activate
   ```
   
6. Install the required dependencies:

   ```bash
   pip install -r requirements.txt


## Usage

1. Edit the `config.json` file to configure the URLs.

2. Run the main script:

   ```bash
   python main.py
   ```

3. The extracted information will be stored in `news.csv` file in the project directory.


## Configuration

- **config.json**: This file contains the input configuration for the script i.e. URLs of the news articles.


## Author
- Aditi Mokashi
