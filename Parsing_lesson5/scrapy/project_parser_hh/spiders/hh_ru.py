import scrapy
from scrapy.http import HtmlResponse
from project_parser_hh.items import ProjectParserHhItem


class HhRuSpider(scrapy.Spider):

    name = 'hh_ru'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://spb.hh.ru/search/vacancy?area=76&search_field=name&search_field=company_name&search_field=description&text=python&no_magic=true&L_save_area=true&items_on_page=20',
        'https://spb.hh.ru/search/vacancy?area=88&search_field=name&search_field=company_name&search_field=description&text=python&no_magic=true&L_save_area=true&items_on_page=20'
    ]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        urls_vacancies = response.xpath("//div[@class='serp-item']//a[@data-qa='vacancy-serp__vacancy-title']/@href").getall()
        for url_vacancy in urls_vacancies:
            yield response.follow(url_vacancy, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        vacancy_name = response.css("h1::text").get()
        vacancy_salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        vacancy_url = response.url

        yield ProjectParserHhItem(
            name=vacancy_name,
            salary=vacancy_salary,
            url=vacancy_url
        )
