from region import *
import sys
import time

def main_menu():
    print(
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[3;37;49m What would you like to do:
   (1) List statistics
   (2) Display 3 cities with longest names
   (3) Display county's name with the largest number of communities
   (4) Display locations, that belong to more than one category
   (5) Advanced search
   (0) Exit program \033[0;37;49m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

def main():
    list_from_file = open_data("malopolska.csv")
    list_of_objects_from_file = EachRegion.make_list_of_objects(list_from_file)
    while True:
        flag()
        main_menu()
        choice = input("your choice: ")
        print("\n")
        if choice == "1":
            for item in EachRegion.list_statictics(list_of_objects_from_file):
                print(item[0], item[1])
            Exit = input("\n\033[3;37;49mPress ENTER to continue.\033[0;37;49m")
        elif choice == "2":
            print("\n3 cities with longest name:\n")
            EachRegion.three_cities_with_longest_name(list_of_objects_from_file)
            Exit = input("\n\033[3;37;49mPress ENTER to continue.\033[0;37;49m")
        elif choice == "3":
            print("\nCounty with the largest number of communities:\n")
            print(EachRegion.county_with_communities(list_of_objects_from_file))
            Exit = input("\n\033[3;37;49mPress ENTER to continue.\033[0;37;49m")
        elif choice == "4":
            print("\nLocations, that belong to more than one category:\n")
            for num, item in enumerate(EachRegion.more_than_one_category(list_of_objects_from_file)):
                print("{}. {}".format(num+1, item))
            Exit = input("\n\033[3;37;49mPress ENTER to continue.\033[0;37;49m")
        elif choice == "5":
            EachRegion.advanced_search(list_of_objects_from_file)
            Exit = input("\n Press ENTER to continue.")
        else:
            sys.exit()


main()
