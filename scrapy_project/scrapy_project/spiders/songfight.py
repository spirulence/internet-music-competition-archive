from scrapy_project.items import Song
import scrapy


class SongFightSpider(scrapy.Spider):
    name = "songfight"
    start_urls = ['https://songfight.org/']

    def parse(self, response):
        title = response.css('#songtitle::text').get()

        for song_link in response.css('#songlist td a'):
            href = song_link.attrib['href']
            if href.endswith(".mp3") or href.endswith(".ogg"):
                yield Song(
                    artist=song_link.css('::text').get(),
                    title=title,
                    file_urls=[href]
                )