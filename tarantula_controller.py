# -*- coding: utf-8 -*-
import tarantula_profile, tarantula_search
type = input("""1. About search
2. Id search
3. Total Search
>> """)


if type == '2':
    profile = input("Enter LinkedIn Id : ")
    # tarantula_profile.collectInfo(profile)
    # tarantula_profile.createProfile(profile)
    # print("Profile created successfully : {}.txt".format(profile))
    try:
        tarantula_profile.collectInfo(profile)
        tarantula_profile.createProfile(profile)
        print("Profile created successfully : {}.txt".format(profile))
    except:
        print("Invalid Id or Error occured!")


if type == '1':
    profiles = tarantula_search.searchProfiles(input("Enter space separated keywords to search : "), int(input("No. of pages to search : ")), int(input("No. of profiles (whichever occurs first) : ")))
    print(profiles)
    l1 = []
    keywords = input("Enter words to filter the profiles\nTo search for phrases, you may enter underscore-separated words\n(For example to search for 'software engineer' enter 'software_engineer')\n>> ")
    for i in profiles:
        try:
            l1.append([tarantula_profile.aboutSearch(i, keywords.split()), i])
        except:
            pass
    l1.sort(reverse=True)
    for i in l1:
        print(i[1], i[0], sep='\t')


if type == '3':
    profiles = tarantula_search.searchProfiles(input("Enter space separated keywords to search : "), int(input("No. of pages to search : ")), int(input("No. of profiles (whichever occurs first) : ")))
    print(profiles)
    l1 = []
    keywords = input("Enter words to filter the profiles\nTo search for phrases, you may enter underscore-separated words\n(For example to search for 'software engineer' enter 'software_engineer')\n>> ")
    keepFiles = True if input("Keep the files(y/n)?") == 'y' else False
    for i in profiles:
        try:
            l1.append([tarantula_profile.totalSearch(i, keywords.split(), keepFiles), i])
        except:
            pass
    l1.sort(reverse=True)
    for i in l1:
        print(i[1], i[0], sep='\t')