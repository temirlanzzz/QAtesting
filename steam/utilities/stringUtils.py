class StringUtilities:
        def getYear(string):
                return string[-4:]

        def getLastWord(string):
                words = string.split()
                return words[-1]