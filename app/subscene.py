import asyncio
import aiohttp
from bs4 import BeautifulSoup
from .base import Base
import re


class Subscene(Base):
    async def search(self, title):
        """
        search function gives a title and search for it in subscene
        results will be passed as list of dicts, sample:
        {"name": "movie/series title", "link": "link to that title", "count": "counts"}
        """
        url = f"https://subscene.com/subtitles/searchbytitle?query={title}"
        resp = await self.aiorequest(url)  # send request to subscene
        if " " in title:
            title = title.replace(" ", "+")
        soup = BeautifulSoup(resp, 'lxml')
        find_ul = soup.find('div', class_='search-result').find_all('ul')  # .find('ul')

        subtitles = []  # list for all finded subs to return
        for ul in find_ul:
            find_li = ul.find_all('li')
            for li in find_li:
                base_li = li.find('div', class_='title').a
                name = base_li.text  # movie/show name
                link = base_li['href']  # movie/show url
                try:  # movie/show subtitle counts
                    sub_count = li.find('div', class_='subtle count').text
                except:
                    sub_count = li.find('span', class_='subtle count').text
                sub_count = re.findall(r'\d+', sub_count)[0]

                link = "https://subscene.com/subtitles" + link

                data = {"name": name, "link": link, "count": int(sub_count)}
                subtitles.append(data)
 
        return subtitles
