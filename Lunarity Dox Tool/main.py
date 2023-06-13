import os
from colorama import init, Fore, Back, Style
import time
import requests
from pystyle import *
import json
import numlookupapi






bnnr2 = """
                                                                    ..;===+.
                                                                .:=iiiiii=+=
                                                             .=i))=;::+)i=+,
                                                          ,=i);)I)))I):=i=;
                                                       .=i==))))ii)))I:i++
                                                     +)+))iiiiiiii))I=i+:'
                                .,:;;++++++;:,.       )iii+:::;iii))+i='
                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
   .+=:))iiiiiiii)))+ii;
  .+=;))iiiiii)));ii+
 .+=i:)))))))=+ii+
.;==i+::::=)i=;
,+==iiiiii+,
`+=+++;`

"""

banner = """
                ``;`                              
             `,+@@@+                              
           .+@@@@@@@;                            
        `;@@@@@@@@@@@                            
       +@@@@@@@@@@@@@:                            
     ;@@@@@@@@@@@@@@@@                            
   `@@@@@@@@@@@@@@@@@@`                          
   `@@@@@@@@@@@@@@@@@@#                          
    .@@@@@@@@@@@@@@@@@@,                          
     :@@@@@@@@@@@@@@@@@@      .'@@                
      #@@@@@@@@@@@@@@@@+;  .+@@@@@                
      `@@@@@@@@@@@@@#;;+@+#@@@#:`                
       #@@@@@@@@@@';'@@@@@@@:`                    
       `@@@@@@@+;;+@@@@@##`                      
        .@@@#;;+@@@@@#+',.,'.                    
         +;;'#@@@@#+;`      ,:                    
         .#@@@@#++:  @.    ...`                  
      `'@@@@#++'. +  .#++;;+  +                  
    ,@@@@@#++:``::+   `',:+,. ,                  
  `@@@@#, #+` ',.`'.   +` ``  `,  .+              
   @@:`  ,+. ,`:``.:   '. .',+++   #              
   ``    #+`++,.`:,``    :`+@@'@@@@'    ````      
         #'`#+:`.,`:` .@@@+@#  +`.      :  `:    
         #:: +.`,.., `@@,#@':. +        :   '    
         #: ` ',:`,, @#``    + +        ' `,;    
         #: ` `:''`  @` #:.. , '        #+++:    
         #: ,     ;#'#  + :   `:         #++      
         #; '     `''         ,          '.      
         ;' '                 #         `@#      
          #.;                ;`       ,#.:;      
          `+;               '.        @   `      
           :#;            `@:        :`  `,      
            .#+;        `'+.'        +            
              .@++#'+@+@++` ;@.     '            
               `' ., ` #:`# `+.#+  :.            
                ., :  @#;.`;`:  `#@.              
                 +``,.;`@+,. '#                  
                 @' ' ;`@:+`#`;`                  
                `#+  ,'`#  :.  '                  
                ' #.  :`#` '`. +                  
                # +.  .:+: :`. .                  
               `, +,   ..+ '`   :                
               ;` #+@:,:#.;``   '                
               #'##:#+.  : `;   ;                
               #. #:      `'`   :                
                  #,        `   .    
"""
 
bnnr = """

     *                                                            *
                             aaaaaaaaaaaaaaaa               *
                         aaaaaaaaaaaaaaaaaaaaaaaa
                      aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                    aaaaaaaaaaaaaaaaa           aaaaaa
                  aaaaaaaaaaaaaaaa                  aaaa
                 aaaaaaaaaaaaa aa                      aa
*               aaaaaaaa      aa                         a
                aaaaaaa aa aaaa
          *    aaaaaaaaa     aaa
               aaaaaaaaaaa aaaaaaa                               *
               aaaaaaa    aaaaaaaaaa
               aaaaaa a aaaaaa aaaaaa
                aaaaaaa  aaaaaaa
                aaaaaaaa                                 a
                 aaaaaaaaaa                            aa
                  aaaaaaaaaaaaaaaa                  aaaa
                    aaaaaaaaaaaaaaaaa           aaaaaa        *
      *               aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                         aaaaaaaaaaaaaaaaaaaaaaaa
                      *      aaaaaaaaaaaaaaaa
    
         
"""





os.system("mode 70,40")
os.system("title Lunarity Dox Tool")

def print_menu():
    os.system("cls")
    print(bnnr)

    print("[ " + Fore.MAGENTA + "1" + Fore.RESET + " ] " + Fore.MAGENTA + "Track Down User" + Fore.RESET)
    print("[ " + Fore.MAGENTA + "2" + Fore.RESET + " ] " + Fore.MAGENTA + "IP Lookup" + Fore.RESET)
    print("[ " + Fore.MAGENTA + "3" + Fore.RESET + " ] " + Fore.MAGENTA + "Phone Number Lookup\n" + Fore.RESET)
    print("[ " + Fore.MAGENTA + "4" + Fore.RESET + " ] " + Fore.MAGENTA + "Developer Info" + Fore.RESET)

def track_down_user():
    os.system("cls")
    print(bnnr)
    username = input("[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Enter Username: " + Fore.RESET)

    instagram = f'https://www.instagram.com/{username}'
    twitch = f'https://www.twitch.tv/{username}'
    facebook = f'https://www.facebook.com/{username}'
    twitter = f'https://www.twitter.com/{username}'
    youtube = f'https://www.youtube.com/@{username}'
    google_plus = f'https://plus.google.com/s/{username}/top'
    reddit = f'https://www.reddit.com/user/{username}'
    wordpress = f'https://{username}.wordpress.com'
    pinterest = f'https://www.pinterest.com/{username}'
    github = f'https://www.github.com/{username}'
    steam = f'https://steamcommunity.com/id/{username}'
    imgur = f'https://imgur.com/user/{username}'
    spotify = f'https://open.spotify.com/user/{username}'
    dailymotion = f'https://www.dailymotion.com/{username}'
    keybase = f'https://keybase.io/{username}'
    pastebin = f'https://pastebin.com/u/{username}'
    wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'
    hackernews = f'https://news.ycombinator.com/user?id={username}'
    ebay = f'https://www.ebay.com/usr/{username}'
    linkedin = f'https://www.linkedin.com/in/{username}'
    tiktok = f'https://www.tiktok.com/@{username}'
    snapchat = f'https://www.snapchat.com/add/{username}'
    vimeo = f'https://vimeo.com/{username}'
    soundcloud = f'https://soundcloud.com/{username}'
    tumblr = f'https://{username}.tumblr.com'
    medium = f'https://medium.com/@{username}'
    quora = f'https://www.quora.com/profile/{username}'
    slack = f'https://{username}.slack.com'
    behance = f'https://www.behance.net/{username}'
    flickr = f'https://www.flickr.com/photos/{username}'
    bitbucket = f'https://bitbucket.org/{username}'
    xing = f'https://www.xing.com/profile/{username}'
    goodreads = f'https://www.goodreads.com/user/show/{username}'
    producthunt = f'https://www.producthunt.com/@{username}'
    deviantart = f'https://{username}.deviantart.com'
    flipboard = f'https://flipboard.com/@{username}'
    venmo = f'https://venmo.com/{username}'
    trello = f'https://trello.com/{username}'
    aboutme = f'https://about.me/{username}'
    slideshare = f'https://www.slideshare.net/{username}'
    lastfm = f'https://www.last.fm/user/{username}'
    dribbble = f'https://dribbble.com/{username}'
    foursquare = f'https://foursquare.com/{username}'
    trip = f'https://www.trip.skyscanner.com/user/{username}'
    zillow = f'https://www.zillow.com/profile/{username}'
    meetup = f'https://www.meetup.com/members/{username}'
    patreon = f'https://www.patreon.com/{username}'
    buzzfeed = f'https://www.buzzfeed.com/{username}'
    mixcloud = f'https://www.mixcloud.com/{username}'
    etsy = f'https://www.etsy.com/people/{username}'
    tiktok = f'https://www.tiktok.com/{username}'

    WEBSITES = [
        instagram, twitch, facebook, twitter, youtube, google_plus, reddit,
        wordpress, pinterest, github, steam, imgur, spotify, dailymotion, keybase, pastebin, wikipedia, hackernews, ebay,
        linkedin, tiktok, snapchat, vimeo, soundcloud,
        tumblr, medium, quora, slack, behance,
        flickr, bitbucket, xing, goodreads, producthunt,
        deviantart, flipboard, venmo, trello, aboutme,
        slideshare, lastfm, dribbble, foursquare, trip,
        zillow, meetup, patreon, buzzfeed, mixcloud, etsy, tiktok
    ]

    print("[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Searching..." + Fore.RESET)
    time.sleep(1)

    count = 0
    match = True
    for url in WEBSITES:
        r = requests.get(url)

        if r.status_code == 200:
            if match == True:
                print("[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Username Has Been Tracked" + Fore.RESET)
                time.sleep(2)
                match = False
                os.system("cls")
                time.sleep(1)
                os.system("mode 70,60")
            if username in r.text:
                print("[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + url + Fore.RESET)
                print(" ")
            else:
                print("[ " + Fore.RED + "-" + Fore.RESET + " ] " + Fore.RED + "Account Doesn't Exist " + Fore.RESET)
                print(" ")

    input("\n[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Press Enter to go back to the main menu. " + Fore.RESET)

def ip_lookup():
    os.system("cls")
    print(banner)
    a_text = input("[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Enter IP: " + Fore.RESET)

    api = f"https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_jYVnB7nBhtoO6M4Abl5hio1IUGX0Y&ipAddress={a_text}"
    response = requests.get(api)
    ip = json.loads(response.text)


    results = f"\nIP: {ip['ip']}\n" \
              f"Country: {ip['location']['country']}\n" \
              f"Region: {ip['location']['region']}\n" \
              f"City: {ip['location']['city']}\n" \
              f"Lat: {ip['location']['lat']}\n" \
              f"Long: {ip['location']['lng']}\n" \
              f"Postal Code: {ip['location']['postalCode']}\n" \
              f"Time Zone: {ip['location']['timezone']}\n" \
              f"Geo Name ID: {ip['location']['geonameId']}\n" \
              f"ISP: {ip['isp']}\n" \
              f"Connection Type: {ip['connectionType']}\n"
    
    print(results)
    input("\n[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Press Enter to go back to the main menu. " + Fore.RESET)

def phone_number_lookup():
    time.sleep(1)
    os.system("cls")
    os.system("mode 77,50")
    print(bnnr2)
    print("[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Example: +420 {number}\n" + Fore.RESET)
    number = input("[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Enter Phone Number: " + Fore.RESET)

    api2 = f"http://phone-number-api.com/json/?number={number}" 
    response2 = requests.get(api2)
    phonersp = json.loads(response2.text)

    phoneresults = f"\nPhone Number: {phonersp['query']}"\
                    f"\nExists: {phonersp['numberValid']}"\
                    f"\nPhone Number Type: {phonersp['numberType']}"\
                    f"\nArea Code: {phonersp['numberAreaCode']}"\
                    f"\nProvider: {phonersp['carrier']}"\
                    f"\nContinent: {phonersp['continent']}"\
                    f"\nCountry: {phonersp['countryName']}"\
                    f"\nLatitude(not consistent): {phonersp['lat']}"\
                    f"\nLongitude(not consistent): {phonersp['lon']}"\
                    f"\nTimezone: {phonersp['timezone']}"\
                    
    
    print(phoneresults)
    

    input("\n[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Press Enter to go back to the main menu. " + Fore.RESET)

def developer_info():
    time.sleep(1)
    os.system("cls")
    Write.Print(f"Developed By Peroxide#8681\n", Colors.blue_to_green, interval=0.05)
    Write.Print(f"https://github.com/Peroxidelol\n", Colors.blue_to_green, interval=0.05)
    Write.Print(f"Dont Skid :)\n", Colors.blue_to_green, interval=0.05)

    input("\n[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Press Enter to go back to the main menu. " + Fore.RESET)

while True:
    print_menu()
    choice = input("[ " + Fore.MAGENTA + "+" + Fore.RESET + " ] " + Fore.MAGENTA + "Choose an option: " + Fore.RESET)

    if choice == '1':
        track_down_user()
    elif choice == '2':
        ip_lookup()
    elif choice == '3':
        phone_number_lookup()
    elif choice == '4':
        developer_info()
    else:
        print("[ " + Fore.RED + "-" + Fore.RESET + " ] " + Fore.RED + "Invalid choice. Please try again." + Fore.RESET)

