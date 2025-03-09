import scrapy
from buivietnam_21108771_w1.items import BookItem

class NambuiOmegaSpiderSpider(scrapy.Spider):
    name = "nambui_omega_spider"
    allowed_domains = ["shop.alphabooks.vn"]

    def start_requests(self):
        yield scrapy.Request(url="https://shop.alphabooks.vn/omega-b42264.html", callback=self.parse)

    def parse(self, response):
        books = response.css('.box-product')
        for book in books:
            apartofbook_url = book.css('.box-product > a ::attr(href)').get()
            if apartofbook_url:  # Kiểm tra nếu URL tồn tại
                book_url = response.urljoin(apartofbook_url)
                yield scrapy.Request(url=book_url, callback=self.parse_book_page)

        next_page = response.xpath('//li[@class="active"]/following-sibling::li[1]/a/@href').get()
        if next_page:
            nextpage_url = response.urljoin(next_page)
            yield scrapy.Request(url=nextpage_url, callback=self.parse)

    def parse_book_page(self, response):
        book_item = BookItem()
        
        # Lấy danh sách các hàng trong bảng thông tin
        table_book_info = response.css('.ck-table-resized tr')

        def get_table_value(index):
            """Trả về giá trị từ bảng nếu tồn tại, nếu không trả về None"""
            if index < len(table_book_info):
                return table_book_info[index].css('td:nth-child(2) ::text').get(default="").strip()
            return None

        book_item['tensach'] = response.css('.pd-title ::text').get(default="").strip()
        book_item['giagoc'] = response.css('.price_retail ::text').get(default="").strip()
        book_item['giagiam'] = response.css('.price_sale ::text').get(default="").strip()
        book_item['tacgia'] = get_table_value(0)
        book_item['nguoidich'] = get_table_value(1)
        book_item['kichthuoc'] = get_table_value(3)
        book_item['sotrang'] = get_table_value(4)
        book_item['hinhthuc'] = get_table_value(5)

        yield book_item
