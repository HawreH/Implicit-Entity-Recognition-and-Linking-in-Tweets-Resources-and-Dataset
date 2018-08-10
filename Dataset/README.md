# Proposed Gold Standard Dataset Overview
This folder contains the proposed gold standard dataset in JSON format. The complete dataset is split into 3 folders; one for implicit tweets, one for explicit tweets, and one for NIL tweets. In the explicit and implicit files, the tweets are classified by their coarse-grained class, namely Person, Organization, Location, Event, Device, and Work. In each coarse-grained class, the tweets are further classified into their fine-grained class and the breakdown can be found in **Table 2**. This dataset, inspired by the DBPedia taxonomy, is comprised of [Perera et al.'s gold standard dataset](https://github.com/sujanucsc/IEL-Twitter/tree/master/data) for implicit entity linking in the categories of WrittenWork and Film as well as our tweets for the rest of the categories. In the NIL file, there is only the class of NIL for both coarse and fine grain. More information about the dataset and how to navigate the files can be found below:

## JSON File Example/Explanation
This example is created from to demonstrate how the navigate the JSON files. Of course, the JSON files contain a lot more tweets per category than as shown below. The format to access the tweets is: <br>`variable_name['course-grained class']['fine-grained class'][tweet number]['tweet-url / entitiy']`<br> For example, to access the url of the first tweet in Person-Actor, the command would be: <br>`dataset['Person']['Actor'][0]['tweet-url']`<br>
```javascript
{
  "Person": {
    "Actor": [
      {
        "tweet-url": "https://twitter.com//tweetiebirdies/status/940196198505504771",
        "entity": "http://dbpedia.org/page/Brad_Pitt"
      },
      {
        "tweet-url": "https://twitter.com//livestrong83062/status/951178198238285824",
        "entity": "http://dbpedia.org/page/Dwayne_Johnson"
      }
    ],
    "MusicalArtist": [
      {
        "tweet-url": "https://twitter.com//RandyWhitePDX/status/953470582913470469",
        "entity": "http://dbpedia.org/page/Michael_Jackson"
      }
    ]
  },
  "Organization": {
    "Company": [
      {
        "tweet-url": "https://twitter.com//Orly_licious/status/952488621902303233",
        "entity": "http://dbpedia.org/page/Walmart"
      }
    ]
  }
}
```

## Table 1. Dataset Stats
| Type | Implicit | Explicit | NIL |
|------|----------|----------|-----|
| **Count** | 1,345 | 2,683 | 3,842 |
| **Average explicit entity per tweet** | 2.53 | 2.68 | 0 |
| **Average token per tweet** | 26.16 | 21.96 | 16.60 |

## Table 2. Proposed Gold Standard Dataset Taxonomy
| Coarse-<br>Grained<br>Class | | Fine-Grained Class | Freq.<br>Implicit | Freq.<br>Explicit |
|-----------------------------|-|--------------------|-------------------|-------------------|
| **Person**  | a<br>b<br>c<br>d<br>e<br>f<br>g | Artist (Actor, Comedian, Rapper, MusicalArtist, Director, ...)<br>Athlete<br>Businessperson (Leader, CEO, Founder, Entrepreneur, Executive, ...)<br>Celebrity (Model)<br>Politician (PrimeMinister, VicePresident, ...)<br>Scientist<br>Writer (Author) | 91<br>18<br>74<br>4<br>84<br>10<br>70 | 163<br>78<br>144<br>53<br>200<br>21<br>137 |
| **Organization** | a<br>b<br>c<br>d | Company<br>EducationalInstitution<br>Group (MusicGroup, Band, PoliticalParty, Charity)<br>SportsClub (SoccerClub, BaseballTeam, HockeyTeam, ...) | 82<br>1<br>85<br>105 | 58<br>13<br>156<br>210 |
| **Location** | a<br>b<br>c<br>d | Monument/HistoricalPlace<br>PopulatedPlace (Country, city, ...)<br>Building/Tower<br>ArchitecturalStructure (Skyscraper,ReligiousBuilding, ...) | 14<br>174<br>10<br>50 | 29<br>338<br>20<br>95 |
| **Event** | a<br>b | NaturalEvent (Earthquake, Cyclone, ...)<br>SocietalEvent (Awards, FilmFestival, SportsEvent, ReligiousEvent, ...) | 10<br>87| 19<br>159 |
| **Device** | a<br>b<br>c | MobilePhone/CellularTelephone<br>Instrument/MusicalInstrument<br>Software | 36<br>8<br>5 | 68<br>2<br>5 |
| **Work** | a<br>b | WrittenWork (book)<br>Film | 158<br>169 | 261<br>255 |


## Table 3. Implicit Tweet Examples
| Domain | Implicit Tweet Example | Target Entity |
|--------|------------------------|---------------|
| Person | [950457140346572800](https://twitter.com//LeeAnnP87/status/950457140346572800) | [Brad Pitt](http://dbpedia.org/page/Brad_Pitt) |
| Organization | [948547408044027904](https://twitter.com//N_S_Styles/status/948547408044027904) | [One Direction](http://dbpedia.org/page/One_Direction) |
| Location | [945842113530482690](https://twitter.com//TheJackOBrien/status/945842113530482690) | [Toronto](http://dbpedia.org/page/Toronto) |
| Event | [949267461970345985](https://twitter.com//Forged_Steele/status/949267461970345985) | [Christmas](http://dbpedia.org/page/Christmas) |
| Device | [922246176853954562](https://twitter.com//phillkane/status/922246176853954562) | [iPhone](http://dbpedia.org/page/IPhone) |
| Book | [496348359754809346](https://twitter.com/GanjaGaby/status/496348359754809346) | [The Great Gatsby](http://dbpedia.org/page/The_Great_Gatsby) |
| Film | [502664791333158913](https://twitter.com/trevorbasset/status/502664791333158913) | [Boyhood](http://dbpedia.org/page/Boyhood_(film)) |

## Table 4. Emplicit Tweet Examples
| Domain | Emplicit Tweet Example | Target Entity |
|--------|------------------------|---------------|
| Person | [953778862164496384](https://twitter.com//itscourtneytho/status/953778862164496384) | [Ed Sheeran](http://dbpedia.org/page/Ed_Sheeran) |
| Organization | [953778836843454465](https://twitter.com//Nicola_Burgin/status/953778836843454465) | [Yonsei University](http://dbpedia.org/page/Yonsei_University) |
| Location | [953773005796200453](https://twitter.com//LiveSpaceAlerts/status/953773005796200453) | [United Kingdom](http://dbpedia.org/page/United_Kingdom) |
| Event | [953588140886888448](https://twitter.com//lunchtimelady/status/953588140886888448) | [Boxing Day](http://dbpedia.org/page/Boxing_Day) |
| Device | [941324274496884736](https://twitter.com//MirianMFI/status/941324274496884736) | [OnePlus X](http://dbpedia.org/page/OnePlus_X) |
| Book | [951756801489293312](https://twitter.com//ilakshta/status/951756801489293312) | [Harry Potter and the Philosopher's Stone](http://dbpedia.org/page/Harry_Potter_and_the_Philosopher's_Stone) |
| Film | [953773515160698881](https://twitter.com//Steinmoney/status/953773515160698881) | [Blade Runner 2049](http://dbpedia.org/page/Blade_Runner_2049) |

## Table 5. NIL Tweet Examples
| Domain | NIL Tweet Example | Target Entity |
|--------|------------------------|---------------|
| N/A | [953778787073904640](https://twitter.com//court_bootem/status/953778787073904640) | N/A |
| N/A | [953778784444080129](https://twitter.com//DaiSikSeoi/status/953778784444080129) | N/A |
| N/A | [953778787065520134](https://twitter.com//ajsutts/status/953778787065520134)| N/A |
