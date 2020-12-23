import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://formnext.mesago.com/frankfurt/en/exhibitor-search.html'

#opening a connection and grabbing a page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#the main list of exhibitors
exhibitors_unfiltered = page_soup.findAll("div",{"class":"o-search-results-container__results h-background h-background--fullwidth"})

#breaking down to individual exhibitor
individual_exhibitor = exhibitors_unfiltered[0].findAll("div",{"data-entry":""})

#creating a csv
filename = '.\Desktop\Jobs.csv'
f = open(filename, "w", encoding="utf-8")
#creating titles of each column, note the \n
headers= "Company Name,Website,Location\n"
f.write(headers)

#dictionary of country codes that Formnext uses. some codes were used twice for the same country (see Sweden and Spain)
country_codes = {
  "D": "Germany",
  "PL": "Poland",
  "F": "France",
  "CN": "China",
  "CAN": "Canada",
  "GB": "UK",
  "NL": "Netherlands",
  "AUS": "Australia",
  "PT": "Portugal",
  "E": "Spain",
  "ES": "Spain",
  "LUX": "Luxemborg",
  "A": "Austria",
  "KOR": "Korea",
  "TUR": "Turkey",
  "SW": "Sweden",
  "HU": "Hungary",
  "LV": "Latvia",
  "SLO": "Slovakia",
  "IND": "India",
  "ISR": "Israel",
  "B": "Belgium",
  "IRL": "Ireland",
  "I": "Italy",
  "FIN": "Finland",
  "RUS": "Russia",
  "S": "Sweden",

}

for exhibitor in range(2, 205):
    company_name = individual_exhibitor[exhibitor].find("span",{"data-entry-key":"name1_kat"}).text.strip()
    website = individual_exhibitor[exhibitor].find("span",{"data-entry-key":"webseite"}).text.strip()
    location = individual_exhibitor[exhibitor].find("span",{"data-entry-key":"kfzkz_kat"}).text.strip()
    try:
        if country_codes[location]: #this statement finds and replaces the country code
            location = country_codes[location]
    except:
        pass #used in case I missed a country code, in which case it prompts an error
    print(company_name)
    print(website)
    print(location)
    f.write(company_name.replace(',', '') + "," + website.replace(',', '') + "," + location.replace(',', '') + "\n")

f.close()