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

---

<div align='center'>
    <h3>DISCLAIMER</h3>
    <em>The script only works on URLs (in the bookmarsk file) that have the following schemes/prefixes:<br>
    <br>
    "https://", "http://", "https://www.", "http://www."<br>
    <br>
    This is because how the seeker function works. It uses those schemes to check if there is a URL in the current seeking line in the file.<br>
    When you enter a site(s) as an argument, the script adds those schemes to the site(s) to match all possible schemes the site might use.<br>
    Some sites use "http://" instead of "https://", and some sites don't use the "www" subdomain prefix. Thus it is neccessary to check for all possible combinations.<br>
    <br>
    Be vary that some sites might not be detected in the bookmarks because of this, for example "localhost" and maybe your router IP "192.168.0.1" or simmilar.
    </em>
</div>
