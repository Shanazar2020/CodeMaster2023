import requests
from bs4 import BeautifulSoup


def extract_all_url(from_soup):
    tags = from_soup.select('a', )
    # print(tags)
    links = [tag.get('href') for tag in tags]

    return links


def filter_urls(urls):
    url: str
    same_domain = set()
    for url in urls:
        if url and url.startswith(domain_name) and url not in same_domain:
            same_domain.add(url)
    return same_domain


def get_content_as_soup(url):
    print(url)
    page = requests.get(url=url)
    soup = BeautifulSoup(markup=page.content, features='lxml')
    return soup


def add_if_not_exists(traversed, new_urls, url_list):
    for u in new_urls:
        if u not in traversed and u not in url_list:
            url_list.append(u)


def get_content(from_soup):
    tags = from_soup.select("[x-data-value]")
    return tags


if __name__ == '__main__':
    all_url = ["https://cm2023.obss.io/3c6ddc3f-ade5-4910-a5fc-a0b00a8c2b61?lang=EN"]
    untraversed_links = [all_url[0]]
    traversed_links = set()

    domain_name = "https://cm2023.obss.io"
    url_exists = True

    while url_exists:
        url = untraversed_links[0]
        soup = get_content_as_soup(url)
        all_url = extract_all_url(soup)
        urls = filter_urls(all_url)

        traversed_links.add(url)

        untraversed_links = untraversed_links[1:]
        add_if_not_exists(traversed_links, urls, untraversed_links)

        if len(untraversed_links) == 0:
            url_exists = False

        get_content(soup)
