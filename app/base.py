import asyncio
import os

import aiofiles
import aiohttp

if os.path.isdir("downloaded") is False:
    print(f"downloaded directory dose not exitst\ncurrent directory: {os.getcwd()}")
    os.mkdir("downloaded")
    print("downloaded directory created!")


class Base:
    """
    base class for package
    all dirty works will be done here.
    """

    # send request to subscene and get the response
    async def request(self, session: aiohttp.ClientSession, url: str):
        resp = await session.request('GET', url=url)
        if resp.status != 200:
            await asyncio.sleep(3)
            resp = await session.request('GET', url=url)
        return await resp.text()

    async def aiorequest(self, url, lang=None):
        if lang is not None:
            language = await self.get_language_filter(lang)
            lang = f"LanguageFilter={language}"
        else:
            lang = ""
        costume_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36', 'cookie': lang}
        async with aiohttp.ClientSession(headers=costume_headers) as session:
            html = await self.request(session, url)
            return html

    async def get_language_filter(self, lang):
        languages = {"fa": "46", "en": "13", "ar": "4"}
        lang = lang.replace(lang, languages[lang])

        return lang

    async def download_file(self, url, file_path):
        async with aiohttp.ClientSession() as session:
            async with session.request('GET', url=url) as resp:
                if resp.status == 200:
                    file_path = f'downloaded/{file_path}.zip'
                    f = await aiofiles.open(file_path, mode='wb')
                    await f.write(await resp.read())
                    await f.close()
        return file_path
