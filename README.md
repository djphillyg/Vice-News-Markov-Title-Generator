# Vice-News-Markov-Title-Generator
A Markov probabilistic generator using Markovify 
Here's a little side project I've hacked away it for a little bit!!

I got inspired from the Hacker News Twitter bot @HNTitles and thought it would be really funny to make one for Vice
Since I couldn't grab the articles from Vice directly, and the RSS feed was buggy I used InternetArchive's python library to grab all of the
vice news RSS Feeds. 
Once those were grabbed, I had to make sure that the RSS Feeds weren't feeding in duplicate titles, because the archive also happens multiple times
per day so I did a simple if function to filter out the duplicates by time object.

Then All I needed to use was Markovify to generate the titles and Wallah! Vice News Article Title generator

Here are some of my favorites I've generated so far 

I Watched the World’s Great Toilet Paper Debate
Reluctant Dirtbags Tell Us Why They Wouldn't Choose to Be Queer and Muslim in Canada
A Whole Week in the Last 100 Years
Everything We Know So Far About the First News Story They Can Remember
Why ‘Super Smash Bros. Melee’ Is the Next Reagan, According to Al Green
Over or Under: We Asked Men What They Thought About the Study That Says They Can’t Stop Drinking
