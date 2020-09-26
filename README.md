# freeg 

freeg is simple script to scrape limited free games.

Currently only able to scrape website https://isthereanydeal.com/specials/.

# Installation

```sh
$ pip install freeg
```

# Usage

#### **From console**

##### Basic
```sh
$ freeg
1. Watch Dogs 2 - epicgames.com
2. Stick It To The Man - epicgames.com
3. Football Manager 2020 - epicgames.com

Choose game(s) :
```

Choose and enter the number according to the games you want to claim.

  ```sh
  Choose game(s) : 1
  ```
It will automatically open (in this example) *Watch Dogs 2* game page on *Epic Games* store from your default web browser. 

##### Open multiple games
You can also open multiple games with `,` and `-` symbol
```
1,2     # Open games 1 and 2
1-3     # Open games 1,2,3
1,3-6   # Open games 1,3,4,5,6
6,2-3   # Open games 6,2,3 (order doesn't matter)
2-3,6   # Same with above
```

#### **Using `scraper.extract()`**
```
from freeg import scraper

games = scraper.extract()
```

`games` would look like this :
```
[
    {
      "title":"Bridge Constructor",
      "url":"https://gaming.amazon.com/loot",
      "store":"amazon.com",
      "time_left":"26 days left"
   },
   {
      "title":"Watch Dogs 2",
      "url":"https://www.epicgames.com/store/en-US/product/watch-dogs-2/home",
      "store":"epicgames.com",
      "time_left":"4 days left"
   },
   {
      "title":"Stick It To The Man",
      "url":"https://www.epicgames.com/store/en-US/product/stick-it-to-the-man/home",
      "store":"epicgames.com",
      "time_left":"4 days left",
      
    }
]
```

# Notes

- Currently only able to scrape website https://isthereanydeal.com/specials/.
- Some games may have wrong information *(ex: already free forever, region locked on specific store)*

