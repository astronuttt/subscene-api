from app.subscene import Subscene
import asyncio

subscene = Subscene()


async def search(title):
    # you can give a move/tv show title and its returns a list of results for searched query
    # example:
    # [{'name': 'True Detective - Third Season', 'link': 'https://subscene.com/subtitles/true-detective-third-season', 'count': 263},
    # {'name': 'True Detective - Second Season', 'link': 'https://subscene.com/subtitles/true-detective-second-season', 'count': 360},]
    result = await subscene.search(title)
    print(result)


async def get_subtitle_list(url, lang):
    # you can get the url from search and pass it to see the subtitles for that title
    # you can filter the language by passing "fa" for Persian, "en" for English and "ar" for Arabic.
    # example result:
    # {'title': 'True Detective - Third Season', 'subtitles': [{'name': 'True.Detective.Season03.Complete.720p.WEB.H264-METCON',
    # 'link': 'https://subscene.com/subtitles/true-detective-third-season/farsi_persian/1953370',
    # 'owner': 'Arian Drama', 'comments': ''}]}
    result = await subscene.subtitles(url, lang)
    print(result)


async def download_page(url):
    # get download pages data. you can get the url from get_subtitle_list()
    # after getting the elements you can pass the download link to down(url) and download the subtitle file.
    # its pretty simple like other steps.
    result = await subscene.down_page(url)
    print(result)


async def down(url):
    file_name = "subtitle1234"  # file name goes here. you can extract it from url or download_page url.
    # finally its become something like: downloaded/subtitle1234.zip (you just need to enter the 'subtitle1234' part)
    resp = await subscene.download(url, file_name)
    # print the path where file saved
    print(resp)


if __name__ == "__main__":
    # search for a title:
    asyncio.run(search("true detective"))

    # see a list of one title with language filter
    # asyncio.run(get_subtitle_list("https://subscene.com/subtitles/true-detective-third-season", "fa"))

    # get the download page:
    # asyncio.run(download_page("https://subscene.com/subtitles/true-detective-third-season/farsi_persian/1916576"))

    # download the file:
    # asyncio.run(down("download link goes here"))
