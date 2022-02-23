from pprint import pprint

def spain_dict():
    f = open("listado-general.txt", "r", encoding="utf-8")
    content = f.read()
    word = ""
    words = []
    for char in content:
        if char != "\n":
            word += char
        else:
            words.append(word)
            word = ""
    a_bit = []
    trhee = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    ten = []
    eleven = []
    twelve = []
    thirteen = []
    fourteen = []
    fifteen = []
    sixteen = []
    a_lot = []
    for word in words:
        if len(word) < 3:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            a_bit.append(word)
        elif len(word) == 3:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            trhee.append(word)
        elif len(word) == 4:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            four.append(word)
        elif len(word) == 5:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            five.append(word)
        elif len(word) == 6:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            six.append(word)
        elif len(word) == 7:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            seven.append(word)
        elif len(word) == 8:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            eight.append(word)
        elif len(word) == 9:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            nine.append(word)
        elif len(word) == 10:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            ten.append(word)
        elif len(word) == 11:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            eleven.append(word)
        elif len(word) == 12:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            twelve.append(word)
        elif len(word) == 13:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            thirteen.append(word)
        elif len(word) == 14:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            fourteen.append(word)
        elif len(word) == 15:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            fifteen.append(word)
        elif len(word) == 16:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            sixteen.append(word)
        elif len(word) > 16:
            word = word.replace("á", "a")
            word = word.replace("é", "e")
            word = word.replace("í", "i")
            word = word.replace("ó", "o")
            word = word.replace("ú", "u")
            word = word.replace("ï", "i")
            word = word.replace("ü", "u")
            a_lot.append(word)

    spain_dict = {
        "a_bit" : a_bit,
        "trhee" : trhee,
        "four" : four,
        "five" : five,
        "six" : six,
        "seven" : seven,
        "eight" : eight,
        "nine" : nine,
        "ten" : ten,
        "eleven" : eleven,
        "twelve" : twelve,
        "thirteen" : thirteen,
        "fourteen" : fourteen,
        "fifteen" : fifteen,
        "sixteen" : sixteen,
        "a_lot" : a_lot,
    }
    f.close()

    return spain_dict

class Finder:

    def __init__(self, word_length) -> None:
        lengths = {
            3 : "trhee",
            4 : "four",
            5 : "five",
            6 : "six",
            7 : "seven",
            8 : "eight",
            9 : "eight",
            10 : "nine",
            11 : "ten",
            12 : "eleven",
            13 : "twelve",
            14 : "thirteen",
            15 : "fifteen",
            16 : "sixteen"
        }

        if word_length < 3:
            length = "a_bit"
        elif word_length > 16:
            length = "a_lot"
        else:
            length = lengths[word_length]
        
        self.word_list = spain_dict()[length]
        self.found_leters = {}
        self.discarted_leters = set()
        self.positioned_leters = {}
    
    def get_found_leters(self):
        return self.found_leters

    def get_discarted_leters(self):
        return self.discarted_leters

    def get_positioned_leters(self):
        return self.positioned_leters
    
    def found_leter(self, leter, position):
        try:
            self.found_leters[leter].append(position)
        except:
            self.found_leters[leter] = [position]
    
    def discarted_leter(self, leter):
        self.discarted_leters.add(leter)

        if leter in self.get_found_leters():
            self.found_leters.pop(leter)
        if leter in self.get_positioned_leters():
            self.positioned_leters.pop(leter)
    
    def positioned_leter(self, leter, position):
        try:
            self.positioned_leters[leter].append(position)
        except:
            self.positioned_leters[leter] = [position]
        if leter in self.get_found_leters():
            self.found_leters.pop(leter)
    
    def found_filter(self, word):
        founds = self.get_found_leters()
        for leter in founds:
            for position in founds[leter]:
                if word[position] == leter or leter not in word:
                    return False
            
        return True
    
    def discarted_filter(self, word):
        for leter in word:
            if leter in self.get_discarted_leters():
                return False
        
        return True
    
    def positioned_filter(self, word):
        positioneds = self.get_positioned_leters()
        for leter in positioneds:
            for position in positioneds[leter]:
                if word[position] != leter:
                    return False
        
        return True
    
    def find_posibles(self):
        res = []
        for word in self.word_list:
            if not self.discarted_filter(word) or not self.positioned_filter(word) or not self.found_filter(word):
                continue

            res.append(word)

        return res