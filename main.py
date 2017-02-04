from region import *
import sys

def main_menu():
    print(
'''
What would you like to do:
   (1) List statistics
   (2) Display 3 cities with longest names
   (3) Display county's name with the largest number of communities
   (4) Display locations, that belong to more than one category
   (5) Advanced search
   (0) Exit program
''')


def main():
    list_from_file = open_data("malopolska.csv")
    list_of_objects_from_file = Gmina.make_list_of_objects(list_from_file)
    while True:
        main_menu()
        choice = input("your choice: ")
        if choice == "1":
            for item in EachRegion.list_statictics(list_of_objects_from_file):
                print (item [0], item[1])
        elif choice == "2":
            EachRegion.three_cities_with_longest_name(list_of_objects_from_file)
        elif choice == "3":
            print(EachRegion.county_with_communities(list_of_objects_from_file))
        elif choice == "4":
            for num, item in enumerate(Gmina.more_than_one_category(list_of_objects_from_file)):
                print("{}. {}".format(num+1, item))
        elif choice == "5":
            EachRegion.advanced_search(list_of_objects_from_file)
        else:
            sys.exit()




main()
