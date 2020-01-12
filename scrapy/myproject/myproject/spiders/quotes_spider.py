import scrapy

class QuotesSpider(scrapy.Spider):
    # can give any name
    name = "quotes_spider"

    # below function is used to make get/posts requests

    def start_requests(self):
        # we can have any number of urls
        urls = ["http://quotes.toscrape.com/page/1/",
                "http://quotes.toscrape.com/page/2/"
            ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
            
            # scrapy.Requests is similar to requests.get
            # callback refers to the function which will run upon 
            # receiving data


    def parse(self, response):
        # get page number 
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page

        # write as binary file and save it as .html
        # with open(filename, 'wb') as f:
        #    f.write(response.body)

        # self.log('Saved file %s' % filename)

        for q in response.css("div.quote"):
            text = q.css("span.text::text").get()
            # get the first text from span tag text class 
            author = q.css('small.author::text').get()
            tags = q.css('a.tag::text').getall()
            # get all the tags
            
            # save the above response as json file

            # filename to save the json file will be 
            # mentioned in terminal as -o filename.json
            yield {
                'text': text,
                'author': author,
                'tags': tags
            }


# to save html file: scrapy crawl quotes_spider in outermost directory
# json file: scrapy crawl quotes-spider -o quotes.json