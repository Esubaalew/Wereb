import os
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

# Configuration
base_url = 'https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/wereb%20keamet%20eske%20amet.html'
target_folder = 'wereb'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def sanitize(name):
    """Sanitize names for both directories and filenames"""
    name = re.sub(r'[\\/*?:"<>|]', '_', name.strip())
    name = re.sub(r'\s+', ' ', name)
    return name[:100]  # Trim to 100 characters

# Create base target folder
os.makedirs(target_folder, exist_ok=True)

# Fetch HTML content
print("Fetching HTML page...")
response = requests.get(base_url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all MP3 links with their text and paths
mp3_entries = []
for a in soup.find_all('a', href=True):
    href = a['href']
    if href.lower().endswith('.mp3'):
        link_text = a.text.strip()
        mp3_entries.append((href, link_text))

print(f"Found {len(mp3_entries)} MP3 files to download")

# Download files with progress
for idx, (href, text) in enumerate(mp3_entries, 1):
    # Construct full URL
    full_url = urljoin(base_url, href)
    
    # Extract and sanitize directory structure from href
    dir_part = os.path.dirname(href)
    dir_parts = [sanitize(p) for p in dir_part.split('/')] if dir_part else []
    
    # Create sanitized filename from link text
    filename = sanitize(text)
    if not filename.lower().endswith('.mp3'):
        filename += '.mp3'
    
    # Create full local path
    local_path = os.path.join(target_folder, *dir_parts, filename)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    # Download with progress
    print(f"Downloading ({idx}/{len(mp3_entries)}): {filename}")
    try:
        response = requests.get(full_url, headers=headers, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, 
                          desc=filename[:20])  # Trim filename for display
        
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    progress_bar.update(len(chunk))
        
        progress_bar.close()
    except Exception as e:
        print(f"Failed to download {filename}: {str(e)}")

print("Download complete!")