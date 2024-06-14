<div align='center'>
    <img src='img/logo.png' height='200px' alt="logo"/>
    <h1>FFBMS</h1>
    <h3>Firefox Bookmark Scraper</h3>
    Get all the links from a Firefox Bookmarks.html, and put them in a .txt file.
</div>

## Why?
I needed all 296 links in my Firefox bookmarks to interact with them through another script. But I wanted them in an organized, line-by-line formatted document. So I made this to accomplish that.

## How to
<h3><li>Rip all urls from specific file</li></h3>

```bash
~ $ ./ffbms.py [BOOKMARKS_FILE]
```

<p>Execute the script with your bookmarks file directory as an argument.<br>
<em>(here, the bookmarks.html is in the same director as the script)</em></p>

<h3><li>Rip all specific sites from specific file</li></h3>

```bash
~ $ ./ffbms.py [BOOKMARKS_FILE] [SITE] [SITE1] [SITE2] [SO_ON_AND_SO_FORTH...]
```

<p>Example</p>

```bash
~ $ ./ffbms.py bookmarks.html reddit.com wallhaven.cc wikipedia.com
```

<p>Just like above, but add your site(s) as arguments behind the bookmarks path.</p>

<h3><li>Running the script without passing a file or site arguments</li></h3>

```bash
~ $ ./ffbms.py
```

<p>If no file or arguments are passed, the script will automatically assume the name of the bookmarks file to be <strong>'bookmarks.html'</strong> and in the same directory as the script, and then run. This is so that you can run the executable in Windows by double clicking the .exe file. Do realize that you can't pass site args this way. You will need to run the script with CMD or Powershell to do that.

The script then generates a <strong>'scraped.txt'</strong> with the links found in the bookmarks file.</p>

---

<h3 align='center'>DISCLAIMER</h3>
<p><em>The script only works on URLs (in the bookmarks file) that have the following schemes/prefixes:

"https://", "http://", "https://www.", "http://www."

This is because how the seeker works. It uses those schemes to check if there is a URL in the current seeking line in the file. When you enter a site(s) as an argument, the script adds those prefixes to the site(s) to match all possible schemes the site might use. Some sites use "http://" instead of "https://", and some sites don't use the "www" subdomain prefix. Thus it is necessary to check for all possible combinations.

Be vary that some sites might not be detected in the bookmarks because of this, for example "localhost" and maybe your router IP "192.168.0.1" or similar.</em></p>

