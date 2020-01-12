# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger


class SeleniumMiddleware(object):
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # Chrome 开启无窗口模式
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(service_args=service_args, chrome_options=chrome_options)
        self.driver.set_window_size(1400, 700)
        self.driver.implicitly_wait(self.timeout)
        self.driver.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.driver, self.timeout)


    def __del__(self):
        self.driver.close()


    def process_request(self, request, spider):
        self.logger.debug('Chrome is Starting')
        try:
            page = request.meta.get('page', 1)
            self.driver.get(request.url)
            if page > 1:
                input = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="J_bottomPage"]/span[2]/input')))
                button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="J_bottomPage"]/span[2]/a')))
                input.clear()
                input.send_keys(page)
                button.click()
            return HtmlResponse(url=request.url, body=self.driver.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('CHROME_SERVICE_ARGS'))