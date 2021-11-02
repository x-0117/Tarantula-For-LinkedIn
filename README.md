# Tarantula (for linkedIn)
Tarantula is a crawler or spider, currently designed for linkedIn. It's a powerful OSINT(Open-source Intelligence, the technical and politically correct term for stalking!!) tool to automate linkedIn searches, scraping profiles to compile relevant information about users and filtering profiles by searching for keywords in them. The project mainly utilises the request module of python to create sessions and to send get and post requests.

## Dependencies
- requests : `pip install requests`
- html : `pip install html`

The three files have to be stored in the same location.

## How it works
For the project, I had to create a separate linkedIn profile, as linkedIn doesn't allow access to any profiles without logging in (and I wasn't keen on making my own credentials public!). Every time a function is called, a session is created by sending a post request to `https://www.linkedin.com/uas/login-submit` using the `email`, `password` of the bot and other hidden form inputs in the data and putting relevant information in the headers to make it appear like the request is coming from an actual browser. Best way to achieve this is `copying command as cURL` from the network tab of developer tools and converting that `cURL` command to `python` using any of the innumerable tools available online.
Keeping the session active ensures that the cookie data don't have to be sent again and again and simulates a log-in of the user. Once logged-in the data can be collected and analysed with the help of relevant requests.

## The tools
The package consists of three files.

`tarantula_search.py` utilises the function `searchProfile(keywords, pages, number)` to automate a search of the given space separated `keywords`, to search the given number of `pages` and to return a `list` of the `number` of profiles (whichever is smaller).

`tarantula_profile.py` compiles the data from the given profile Id, searches for certain keywords in the collected data-Chunks, sorts the profiles accordingly, arranges the data in a compact but human readable form according to the functions called.

`tarantula_controller.py` imports the two files and utilizes the `functions` to perform specific tasks. The three given tasks are as follows :
- ### Id search
`collectInfo(profile)`:
Accepts the linkedIn id as a parameter, crawls the profile of the user and scrapes information from the profile. This information is organized in a compact human readable form to be stored in a text file `linkedIn_Id_info.txt`. It has three separate portions, `About Info`, `Contacts` and `Important links`

- ### Total Search
`totalSearch(profile, keywords, keepFiles)` :
Makes a list of the profiles to be searched using `tarantula_search.py.searchProfile(keywords, pages, number)` and iterates through this list to search each of the profiles individually. The data collected is then serialized into a space separated string to ease the search of the keywords. The profiles are arranged in descending order of the no. of keywords found. For example if the keyword list is `python machine_learning kolkata`, a profile-string containing all three of the strings(the `machine_learning` gets converted to `machine learning` before the search occurs) will be placed in a higher priority position than the profile-string containing just one. Finally the keepFiles parameter, if `True`, tells the machine to store the information of all the users in the list in a text file.
A serialized data chunk to search for keywords, after filtering all unnecessary characters and making the string 1-space separated, may look as follows :
```
india chakdaha west bengal india computer software special mention award for 10 days of code by glug nit durgapur 102020 vishwactf  certificate of achievement by vishwactf 2019  2023 indian institute of engineering science and technology iiest shibpur computer engineering bachelor of technology  btech none hindi  limitedworking english  professionalworking bengali  nativeorbilingual anirban sikder none incoming intern wells fargo  expert  codeforces  4 star  codechef  web developer  interested in cybersecurity  student  iiest shibpur student  indian institute of engineering science and technology passionate problem solver and participated in quite a lot of competitive programming competition full stack web developer mostly following mern stack interested in cybersecurity and participated in many capture the flag competition none none anirbansikder5b7773185 52021  52021 helps in visualizing comparison based sorting algorithm sorting algo visualiser httpsvisualisesortingalgonetlifyapp 52021  52021 build your resume by providing details about yourself resume builder application httpsresumebuildanirbanherokuappcom c c programming language javascript bash python programming language nodejs httpsleetcodecomanirban2000 my leetcode profile anirban sikder  leetcode profile httpswwwcodechefcomusersanirban2000 anirban2000  codechef user profile for anirban sikder  codechef anirban2000  codechef user profile for anirban sikder  codechef httpscodeforcescomprofilebreakingcode codeforces programming competitions and contests programming community breakingcode  codeforces httpsgithubcomanirbansikder iiest shibpur  competitive programmer  web developer  anirbansikder anirbansikder  overview birthdateon none birthdayvisibilitysetting none address none wechatcontactinfo none primarytwitterhandle none twitterhandles  phonenumbers none ims none type comlinkedinvoyageridentityprofileprofilecontactinfo emailaddress none entityurn urnlifscontactinfoacoaacu3spsbggqtmfdalhfk6b7yizkvaguepe connectedat none websites none sesamecreditgradeinfo none interests none
```

- ### About search
It's similar to the Total Search, but is much faster, as it collects only the `about` and `headline` from a person's linkedIn profile and searches for keywords in them. Just like the total Search, it then arranges the profiles in descending order of the no. of keywords found.
Unlike Total Search, their is no provision for storing the collected information in a text file.

## Difficulties
- LinkedIn is very particular about bot activity, and may trigger captcha verifications which would hamper the normal functioning of the bot, causing it to raise errors and hence affect the normal functioning.(However, if used in a limited scale, no problems should occur)

- The tarantula bot was created only for the purpose of this project and the numnber of connections it has is very limited (0 to be specific -_-)
hence, it doesn't have access to a lot of profiles.

## Solutions
- The credentials of the bot are `tarantula.1110101@protonmail.com:T4ran7ula` (No, you can't change the password, you don't have access to the mail. Try Brute-forcing! Go on!!) if you login manually to the profile and pass a few of the captcha tests, you're good to go. It's better if you're logged in from a browser, while the code runs.
- The `session_key` and `session_password` parameters, marked in both the files can be replaced with the credentials of another account. This owing to a larger network of connections may have access to more no. of profiles. Furthermore, if you are using your own credentials, the searches will be more personalised (Not my credit! Props to linkedIn) as the chances of the searched profiles being closely connected to the user increases. (And NO! The program won't send a post request to a remote server with your credentials as parameters, so that I can steal your profile!! Check the code, it's open-source for a reason!!!)
