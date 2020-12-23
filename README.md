# ExpositionScraper
This scraper goes through the [Formnext AM exposition](https://formnext.mesago.com/frankfurt/en/exhibitor-search.html) to output a csv of exhibitors/company names, websites, their location, AND if they are currently hiring. The original website used some funky country codes, so I also converted them into something more recognizable. This is how this one works:

![](example1.PNG)

To find out if they are hiring, I html.parsed the entire contents of each website and ran a search function for the word "Career" or "Jobs". There may be some false positive or negatives, but it covers 90% of the cases, plus a human would manually go through the companies to see if they want to apply anyway.


