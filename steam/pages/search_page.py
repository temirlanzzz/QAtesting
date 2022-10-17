from selenium.webdriver.common.by import By
from utilities.stringUtils import StringUtilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from models.game_model import GameModel
class SearchPage():
    ID_SEARCH_BUTTON = "store_search_link"
    ID_SEARCH_INPUT = "store_nav_search_term"
    XPATH_SEARCH_PLATFORM = ".//div[@class='responsive_search_name_combined']//div[@class='col search_name ellipsis']//div//span"
    XPATH_SPAN_TITLE = "//span[@class='title']"
    XPATH_SEARCH_RESULT_ROWS = "//div[@id='search_resultsRows']"
    XPATH_FIRST_A = ".//a[1]"
    XPATH_SECOND_A = ".//a[2]"
    XPATH_SEARCH_PRICE = ".//div[@class='responsive_search_name_combined']//div[@class='col search_price_discount_combined responsive_secondrow']//div[@class='col search_price  responsive_secondrow']"
    XPATH_SEARCH_REVIEW = ".//div[@class='responsive_search_name_combined']//div[@class='col search_reviewscore responsive_secondrow']//span"
    XPATH_SEARCH_RELEASE_DATE = ".//div[@class='responsive_search_name_combined']//div[@class='col search_released responsive_secondrow']"
    XPATH_SEARCH_NAME = ".//div[@class='responsive_search_name_combined']//div[@class='col search_name ellipsis']//span"
    def __init__(self, driver):
        self.driver = driver


    def searchPrecondition(self, url, text):
        self.driver.get(url)
        self.driver.find_element(By.ID, self.ID_SEARCH_INPUT).send_keys(text)
        button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, self.ID_SEARCH_BUTTON)))
        self.driver.execute_script("arguments[0].click();", button)

    def getTitle(self):
        return self.driver.title

    def getSearchResults(self):
        #self.waitForElement((By.XPATH, self.XPATH_SEARCH_RESULT_ROWS))
        searchResultsRows = self.driver.find_element(By.XPATH, self.XPATH_SEARCH_RESULT_ROWS)
        results = [] #list of result names
        span_titles = searchResultsRows.find_elements(By.XPATH, self.XPATH_SPAN_TITLE)
        for span_title in span_titles:
            results.append(span_title.text)
        return results

    def saveResultInfo(self, element):
        game = GameModel()
        game.setName(element.find_element(By.XPATH, self.XPATH_SEARCH_NAME).text)
        platforms = element.find_elements(By.XPATH, self.XPATH_SEARCH_PLATFORM)
        platforms_list = []
        for platform in platforms:
            classname = platform.get_attribute("class")
            if len(classname) > 0:
                platform_name = StringUtilities.getLastWord(classname)
                if platform_name not in platforms_list:
                    platforms_list.append(StringUtilities.getLastWord(classname))
        game.setPlatforms(platforms_list)
        game.setReleaseDate(element.find_element(By.XPATH, self.XPATH_SEARCH_RELEASE_DATE).text)
        review_result = element.find_element(By.XPATH, self.XPATH_SEARCH_REVIEW).get_attribute("class")
        game.setReviewResult(StringUtilities.getLastWord(review_result))
        game.setPrice(element.find_element(By.XPATH, self.XPATH_SEARCH_PRICE).text)
        return game

    def getFirstTwoResults(self):
        searchResultsRows = self.driver.find_element(By.XPATH, self.XPATH_SEARCH_RESULT_ROWS)
        first = self.saveResultInfo(searchResultsRows.find_element(By.XPATH, self.XPATH_FIRST_A))
        second = self.saveResultInfo(searchResultsRows.find_element(By.XPATH, self.XPATH_SECOND_A))
        return first, second
