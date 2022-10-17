import json
class TestingData:

    def __init__(self, url, policyTitle, searchTitle, date, search):
        self.url = url
        self.policyTitle = policyTitle
        self.searchTitle = searchTitle
        self.date = date
        self.search = search
    
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def readJson(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return TestingData(data['STEAM_URL'], 
                               data['POLICY_TITLE'],
                               data['SEARCH_TITLE'], 
                               data['EXPTECTED_DATE'], 
                               data['EXPECTED_FIRST_SEARCH'])
