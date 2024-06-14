<div align="center">
    <img src="logo.png" height="200px"/>
    <h1>FFBMS</h1>
    <h3>Firefox Bookmark Scraper</h3>
    Get all the links from a Firefox Bookmarks file, and put them in a .txt file.
</div>

## Why?
I needed all 196 links in my Firefox bookmarks to interact with them through another script. But I wanted them in an organized, line-by-line formatted document. So I made this to accomplish that.

## How?
1. Place the script and your exported bookmarks.html file in the same directory.
2. Open a terminal in that directory, and execute the script with the bookmarks.html file as an argument. As follow:

```bash
~ $ ./FFBMS.py bookmarks.html
```

The script then generates a new .txt file with the links found in the bookmarks.html file.