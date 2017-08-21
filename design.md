# Website

## Team statistics

### Background

1. Beikao is a team of broadcasters, located www.lizhi.fm/40624

1. There are two major categories of broadcasts:

	* commentaries on the recent news

	* interviews with the interesting people around

### Goal

1. Display the stats(number of views, comments, likes, etc.) of each program in lizhi.fm

1. Display the stats of each team member 

1. (Optional) Based on the current stats, predict who is the recommended next broadcaster



### Implementation

1. Crawl over lizhi.fm and then get the data (very small, guaranteed to fit in one single machine).

1. Do processing and feed them into the database

1. In backend api, get the data per team member and the overall stats




## New recommendation

### Goal

1. Display the recommended news for the next program

1. Display the recommended topic for the next interview program


### Implementation

1. Crawler the usual websites for the news that people used to watch.

1. Feed the data into a recommendation system and then get top K results
	* input to the recommendation system is the crawler results from the news websites, and also the stats of each programs.

1. Display the top K results on the frontend
	* title, content, source link
	* thumbnails if so found
	* Useful? Useless? button if so chosen




