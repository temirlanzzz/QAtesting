import pytest
from pages.policy_page import PolicyPage
from pages.search_page import SearchPage
from utilities.stringUtils import StringUtilities
from utilities.testing_data import TestingData
from models.game_model import GameModel
class TestPolicy():
    @pytest.mark.usefixtures("chrome_init_driver")
    def test_policy(self):
        self.policyPage = PolicyPage(self.driver)
        test_data = TestingData.readJson(r"C:\Users\User\Desktop\a1qa\github\task2.2\data\test_data.json")
        self.policyPage.policyPrecondition(test_data.url)
        expected_result = test_data.policyTitle
        actual_result = self.policyPage.getTitle()
        assert expected_result == actual_result, 'Wrong title!'
        assert self.policyPage.languagesSwitchVisible(), 'Language switch is not visible' # check if language switch is visible
        revisionDate = self.policyPage.getSignDate()
        expected_date = test_data.date
        actual_date = StringUtilities.getYear(string=revisionDate.text)
        assert expected_date == actual_date, 'Revision dates is not 2022'

    @pytest.mark.usefixtures("chrome_init_driver")
    def test_search(self):
        test_data = TestingData.readJson(r"C:\Users\User\Desktop\a1qa\github\task2.2\data\test_data.json")
        expected_first_search = test_data.search
        self.searchPage = SearchPage(self.driver)
        self.searchPage.searchPrecondition(test_data.url, expected_first_search)
        expected_result = test_data.searchTitle
        actual_result = self.searchPage.getTitle()
        assert expected_result == actual_result, 'Wrong title!'
        actual_first_search_list = self.searchPage.getSearchResults()
        assert expected_first_search in actual_first_search_list, 'Dota 2 is not in search results'
        assert expected_first_search == actual_first_search_list[0], 'Dota 2 is not equal to first search result'
        search_first_result, search_second_result = self.searchPage.getFirstTwoResults()
        self.searchPage2 = SearchPage(self.driver)
        self.searchPage2.searchPrecondition(test_data.url, search_second_result.getName())
        actual_second_search_list = self.searchPage2.getSearchResults()
        assert search_second_result.getName() in actual_second_search_list, search_second_result.getName()+' is not in search results'
        search_third_result, search_forth_result = self.searchPage2.getFirstTwoResults()
        assert search_first_result == search_forth_result, 'Search results does not match'
        assert search_second_result == search_third_result, 'Search results does not match'

