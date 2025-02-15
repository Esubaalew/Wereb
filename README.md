# Ethiopian Orthodox Church Toolkit(Subject to update - readme expails the available version not the future)

A Python script to download liturgical music files from the Ethiopian Orthodox Church website while preserving directory structure and using meaningful filenames.

## Features

- 🕷️ **Web Scraping**: Automatically extracts MP3 links from webpage
- 📂 **Directory Preservation**: Maintains original server directory structure
- 📝 **Meaningful Filenames**: Uses link text for descriptive filenames
- 🧹 **Sanitization**: Cleans invalid characters from filenames/paths
- 📊 **Progress Tracking**: Visual progress bars with `tqdm`
- ♻️ **Duplicate Handling**: Skips already downloaded files
- 🛡️ **Error Handling**: Gracefully handles download errors

## Prerequisites

- Python 3.6+
- Required packages:
  ```bash
  pip install requests beautifulsoup4 tqdm
  ```

## Installation

1. Clone repository:
   ```bash
   git clone https://github.com/yourusername/church-music-downloader.git
   cd church-music-downloader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python download_script.py
```

The script will:
1. Connect to [target website](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/wereb%20keamet%20eske%20amet.html)
2. Parse all MP3 links
3. Create `wereb` folder with subdirectories
4. Download files with progress bars

## File Structure

Downloaded files will follow this structure:
```
wereb/
├── 4 wereb keamet eske amet/
│   └── 1 zemeskerem/
│       └── 1- mekerem kidus yohannes/
│           └── 1 - አመላለስ ዘዋዜማ = ባርከኒ ባርከኒ.mp3
├── 2 - አመላለስ = ዳዕሙ ከመ ያእምርዎ.mp3
└── ...
```

## Configuration

Key script settings (modify directly in code):
```python
base_url = 'https://www.ethiopianorthodox.org/.../wereb keamet eske amet.html'
target_folder = 'wereb'  # Change output directory
headers = { ... }  # Modify request headers if needed
```

## Error Handling

The script will:
- Skip files that already exist
- Continue after failed downloads
- Show error messages for troubleshooting
- Retain partial downloads for resume capability

## Legal & Ethical Considerations

⚠️ **Important**:
- Verify website's terms of service before use
- Respect `robots.txt` directives
- Limit request rate to avoid server overload
- Use only for authorized personal archival purposes

## License

[MIT License](LICENSE) (modify as needed)

## Acknowledgments

- Built with:
  - [Requests](https://docs.python-requests.org/)
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
  - [tqdm](https://tqdm.github.io/)
- Amharic text support via UTF-8 encoding
## Sample Images
![Screenshot from 2025-02-15 23-37-49](https://github.com/user-attachments/assets/b2f8f05b-3012-4e4e-a0bc-32d84cb5150d)
