from region import *
import sys
import os
from tabulate import tabulate

def main_menu():
    print(
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[3;37;49m What would you like to do:
   (1) List statistics
   (2) Display 3 cities with the longest names
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
        os.system("clear")
        flag()
        main_menu()
        choice = input("your choice: ")
        print("\n")
        if choice == "1":
            print (tabulate(EachRegion.list_statictics(list_of_objects_from_file), headers=['MAŁOPOLSKIE', 'AMOUNT'], tablefmt='orgtbl'))
            Exit = input("\n\033[3;37;49mPress ENTER to continue.\033[0;37;49m")
        elif choice == "2":
            print("\n\033[1;37;49mThree cities with the longest name:\033[0;37;49m\n")
            EachRegion.three_cities_with_longest_name(list_of_objects_from_file)
            Exit = input("\n\033[3;37;49mPress ENTER to continue.\033[0;37;49m")
        elif choice == "3":
            print("\n\033[1;37;49mCounty with the largest number of communities:\033[0;37;49m\n")
            print(EachRegion.county_with_communities(list_of_objects_from_file))
            Exit = input("\n\033[3;37;49mPress ENTER to continue.\033[0;37;49m")
        elif choice == "4":
            print("\n\033[1;37;49mLocations, that belong to more than one category:\033[0;37;49m\n")
            for num, item in enumerate(EachRegion.more_than_one_category(list_of_objects_from_file)):
                print("{}. {}".format(num+1, item))
            Exit = input("\n\033[3;37;49mPress ENTER to continue.\033[0;37;49m")
        elif choice == "5":
            print(tabulate(EachRegion.advanced_search(list_of_objects_from_file), headers=['LOCATION', 'TYPE'], tablefmt='orgtbl'))
            Exit = input("\n Press ENTER to continue.")
        else:
            sys.exit()


main()
