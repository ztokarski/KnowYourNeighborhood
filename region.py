from ui import *
from collections import Counter
from operator import itemgetter


class Województwo:
    '''
    class for Województwo.
    '''
    def __init__(self, woj, nazwa, typ):
        self.woj = woj
        self.nazwa = nazwa
        self.typ = typ

    def __repr__(self):
        return "{} {}".format(self.nazwa, self.typ)

    @classmethod
    def make_list_of_objects(self, list_of_lists):
        '''
        Making list of objects from list of lists
        '''
        list_of_objects = []
        for item in list_of_lists:
            obj = Gmina(item[0], item[1], item[2], item[3], item[4], item[5])
            list_of_objects.append(obj)
        return list_of_objects

    @classmethod
    def list_statictics(self, list_of_objects):
        '''
        Returns list with all types of items.
        '''
        return Counter([x.typ for x in list_of_objects]).most_common()


    @classmethod
    def county_with_communities(self, list_of_objects):
        '''
        Returns county with the largest number of communities.
        '''
        count_typ_list = Counter([x.pow for x in list_of_objects]).most_common(1)
        for item in list_of_objects:
            if count_typ_list[0][0] in item.pow:
                return item.nazwa


    @classmethod
    def three_cities_with_longest_name(self, list_of_objects):
        '''
        Returns three items with longest name (item.nazwa)
        '''
        three_names = sorted([x.nazwa for x in list_of_objects if x.typ == "miasto"], key=getKey3, reverse = True)
        for num, item in enumerate(three_names[:3]):
            print("{}. {}".format(num+1, item))

    @classmethod
    def more_than_one_category(self, list_of_objects):
        '''
        Display locations, that belong to more than one category
        '''
        more_than_one = []
        count_name_list = Counter([x.nazwa for x in list_of_objects]).most_common()

        for item in count_name_list:
            if int(item[1])>1:
                more_than_one.append(item[0])
        return more_than_one


    @classmethod
    def advanced_search(self, list_of_objects):
        '''
        search for: "string"
        '''
        search_list = []
        search_string = input("Searching for: ")
        for item in list_of_objects:
            if search_string in item.nazwa:
                search_list.append(item)
        search_list_sorted = (sorted(sorted(search_list, key=getKey2),key=getKey))
        for num, item in enumerate(search_list_sorted):
            print("{}. {}".format(num+1, item))


class Powiat(Województwo):
    '''
    class for Powiat.
    '''
    def __init__(self, woj, pow, nazwa, typ):
        Województwo.__init__(self, woj, nazwa, typ)
        self.pow = pow


class Gmina(Powiat):
    '''
    class for Gmina.
    '''
    def __init__(self, woj, pow, gmi, rgmi, nazwa, typ):
        Powiat.__init__(self, woj, pow, nazwa, typ)
        self.gmi = gmi
        self.rgmi = rgmi


class EachRegion(Gmina):
    '''
    class for each type of region.
    '''
    def __init__(self, woj, pow, gmi, rgmi, nazwa, typ):
        Gmina.__init__(self, woj, pow, gmi, rgmi, nazwa, typ)
