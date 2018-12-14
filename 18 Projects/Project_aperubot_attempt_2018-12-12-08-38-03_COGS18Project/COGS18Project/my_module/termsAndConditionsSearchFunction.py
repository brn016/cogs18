import requests
from bs4 import BeautifulSoup
import webbrowser 

Terms_and_Conditions = {'Spotify':'https://www.spotify.com/us/legal/end-user-agreement/plain/','Facebook Data Policy':'https://www.facebook.com/about/privacy/update','PayPal':'https://www.paypal.com/us/webapps/mpp/ua/privacy-full','Google':'https://policies.google.com/privacy?hl=en','Netflix Privacy Statement':'https://help.netflix.com/legal/privacy','Microsoft Privacy Statement':'https://privacy.microsoft.com/en-US/privacystatement','Goldman Sachs Global Privacy Policy':'https://www.goldmansachs.com/privacy-and-cookies/global-privacy-policy.html','UCSD Privacy Policy':'https://admissions.ucsd.edu/terms-of-use/privacy-policy.html','Cisco':'https://www.cisco.com/c/en/us/about/legal/privacy.html','Forbes':'https://www.forbes.com/privacy/english/#59ac0c003061','Amgen':'https://www.amgen.com/privacy-statement/'}

def termsAndConditionsSearch():
    """Takes a webpage and outputs the number of occurances of the intended search word
    
    Paramters
    ---------
    input() : user input
        Webpage that will be scraped and analyzed
    input() : user input
        Word that will be searched in the webpage
    
    Returns
    -------
    output : string
        occurances of the search word
    output: float
        percentage of the search word occurance to the total number of words on the webpage
    output: webpage 
        webpage that was analyzed will open in a new tab
    """
    
    print(Terms_and_Conditions.keys())
    
    #Take User's link to scrape 
    terms_and_conditions_input = input("Choose a terms of conditions:")
    
    #Take User's word to search for 
    word_to_search = input('Enter a word to search for:')
    terms_and_conditions_link = Terms_and_Conditions.get(terms_and_conditions_input)
    
    #Scrape the page and parse it using BeautifulSoup and split the text for analysis
    page = requests.get(terms_and_conditions_link)
    soup = BeautifulSoup(page.content,'html.parser')
    terms_converted_to_text = soup.get_text()
    text_terms_split = terms_converted_to_text.split()
    
    count = 0
    for element in text_terms_split:
        if element.lower() == word_to_search.lower():
            count += 1 
        else:
            continue
            
    #calculates the frequency of the word compared to the total number of words on the webpage
    frequency_percent = (count/len(text_terms_split)) * 100
    
    url = Terms_and_Conditions.get(terms_and_conditions_link)
    
    print("Occurances of the word " + word_to_search + ":" ,count) 
    url = terms_and_conditions_link
    webbrowser.open(url)
    return print(word_to_search + " appears in ",frequency_percent,"% of the page")
    
   
    
