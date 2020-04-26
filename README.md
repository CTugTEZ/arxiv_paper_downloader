# Arxiv Paper Downloader
Paper Downloader, downloads the papers created by bookmarks ARX application on iOS. 

REQUIREMENTS
- python3
- requests
- sys
- argparse

USAGE
- Create txt file from bookmarks in ARX application.
- Save file to computer. 
<code>
python paper_downloader.py -l "path to list of arx app output" -p "path to download"
</code>

İmportant note: add "/" to end of -p argument.

Example:
<code>
python paper_downloader.py -l /Desktop/savedDocumentExport.txt -p /Desktop/papers/
</code>
