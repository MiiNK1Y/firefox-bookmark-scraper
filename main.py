import sys, time
from colorama import Fore


#set the parameters passed
argPath = sys.argv[1]
nonFormatedArgSite = sys.argv[2:]


#setting possible prefixes found in the URLs
urlFormats = ['https://', 'http://', 'https://www.', 'http://www.']


#for each passed site-parameter, construct possible url-combinations to seek
if len(nonFormatedArgSite) > 0:
    argSite = []
    for url in urlFormats:
        for item in nonFormatedArgSite:
            constructedUrl = url + item
            argSite.append(constructedUrl)
#if there are no passed parameters, set the argSite to an empty string as placeholder
else:
    argSite = ""


#some flashy colors
def color_that_green(text):

    return f"{Fore.GREEN}{text}{Fore.RESET}"


#some more flashy colors
def color_that_cyan(text):

    return f"{Fore.CYAN}{text}{Fore.RESET}"


#format the bookmark-url-line, removing the bloat on each side of the relevant url
def format_line_string(line):
    line = line.strip().split('"')[1::2][0]
    return line


def site_seek():

    with open(argPath, 'r', encoding='UTF-8') as f:
        loadFileToMem = f.readlines()
        siteList = []
        #loop through each item in the argSite, to check the existence of each item
        if len(argSite) > 0:
            for site in argSite:
                #then loop through each line in the file, looking for valid items mathing with argSite
                for line in loadFileToMem:
                    if site in line:
                        line = format_line_string(line)
                        siteList.append(line)
        else:
            for url in urlFormats:
                #then loop through each line in the file, looking for valid items mathing with argSite
                for line in loadFileToMem:
                    if url in line:
                        line = format_line_string(line)
                        siteList.append(line)
        siteList = set(siteList)
        siteList = sorted(list(siteList))
    f.close()
    return siteList


def main():

    fetchedSites = site_seek()
    with open('demo/scraped_urls.txt', 'w') as newFile:
        for i in fetchedSites:
            shortStringI = f"{i[0:60]}....."
            print(f"Adding: {color_that_green(shortStringI)}{' ' * 30}", end='\r')
            newFile.writelines(f"{i}\n")
            time.sleep(0.001)
    newFile.close()
    print(f"\nURLs found: {len(fetchedSites)}\nNew file created with the scraped urls in /demo/scraped_urls.txt\n")


def main_imported():

    fetchedSites = site_seek()
    return fetchedSites


if __name__ == '__main__':
    main()
else:
    main_imported()