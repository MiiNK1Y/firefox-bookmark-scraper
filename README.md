<div align="center">
    <img src="logo.png" height="200px"/>
    <h1>FFBMS</h1>
    <h3>Firefox Bookmark Scraper</h3>
    Get all the links from a Firefox Bookmarks.html, and put them in a .txt file.
</div>

## Why?
I needed all 296 links in my Firefox bookmarks to interact with them through another script. But I wanted them in an organized, line-by-line formatted document. So I made this to accomplish that.

## How to
#### Rip all urls
1. Execute the script with your bookmarks file directory as an argument. Like this:

```bash
~ $ ./ffbms.py bookmarks.html
```
#### Rip all speciffic sites
2. Just like above, but add your site(s) as arguments behind the bookmarks path. LIke this:

```bash
~ $ ./ffbms.py bookmarks.html [site] [site1] [site2] [so_on_and_so_forth...]
```

Example

```bash
~ $ ./ffbms.py bookmarks.html reddit.com wallhaven.cc wikipedia.com
```

The script then generates a '<strong>scraped.txt</strong>' with the links found in the bookmarks file.
