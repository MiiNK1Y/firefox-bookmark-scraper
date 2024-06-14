#!.env/bin/python3

from sys import argv
from colorama import Fore

target_file = argv[1]
target_sites = argv[2:]

class Firefox():
    def __init__(self, target_file: str, target_sites: list) -> None:
        self.target_file = target_file
        self.target_sites = target_sites
        self.url_schemes = ['https://', 'http://', 'https://www.', 'http://www.']

    def clean_url_line(self, url: str) -> str:
        cleaned_url_line = url.strip().split('"')[1::2][0]
        return cleaned_url_line

    def make_url_from_string(self, site: str) -> str:
        created_urls = []
        for url in self.url_schemes:
            created_urls.append(url + site)
        return created_urls

    def make_url_combos(self) -> list:
        possible_url_combos = []
        if len(self.target_sites) > 0:
            for site in self.target_sites:
                url_combos = self.make_url_from_string(site)
                for url in url_combos:
                    possible_url_combos.append(url)
        return possible_url_combos

    def seek_sites(self) -> list:
        target_sites = self.make_url_combos()
        bookmark = open(self.target_file, 'r', encoding='UTF-8')
        lines = bookmark.readlines()
        bookmark.close()
        urls = []
        if len(target_sites) > 0:
            look_for = target_sites
        else:
            look_for = self.url_schemes
        for line in lines:
            for site in look_for:
                if site in line:
                    site = self.clean_url_line(line)
                    urls.append(site)
        urls = set(urls)
        urls = sorted(list(urls))
        return urls

def c_green(string: str) -> str:
    colored_string = Fore.GREEN + string + Fore.RESET
    return colored_string

def main() -> None:
    bookmark = Firefox(target_file, target_sites)
    fetched_sites = bookmark.seek_sites()
    scraped = open('scraped.txt', 'w')
    for num, url in enumerate(fetched_sites):
        num += 1
        short_string = url[0:40] + "....."
        print(f"Adding ({num}): {c_green(short_string)}{' ' * 30}", end='\r')
        scraped.writelines(url + "\n")
    scraped.close()
    print(f"\nURLs found: {len(fetched_sites)}\n'scraped.txt' was created.\n")

if __name__ == '__main__':
    main()
