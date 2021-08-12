# Niche.com Back-End Coding Exercise: <br/> Indexing College Reviews

## Overview
Your task is to write a command line program that creates a basic index of user reviews of colleges and, 
once finished, allows the user to query the index by keyword and see the number of reviews per college
that contained that keyword.  

There are roughly one thousand text files on one of our web servers that we would like to be able to query. 
Each file represents reviews for a particular college. The first line of each text file is the name of a 
college in our system. The rest of the lines in each file are reviews about that college from users who 
have attended the school (one review per line). The URLs for each of these "college review files" are 
specified in [`urls.txt`](urls.txt), which contains one URL per line. 

In [`stopWords.txt`](stopwords.txt) you will find a list of common words, one per line, which you should
exclude from your index.

Your program should:
 1. download the review files specified in [`urls.txt`](urls.txt) and build a search index, ignoring words 
 in [`stopWords.txt`](stopwords.txt)
 1. prompt the user for a search token
 1. return results showing the colleges with reviews matching that token, as well as a count of reviews per
 college
 1. repeat steps 2-3, allowing the user to perform multiple searches
 
Your program should support case-insensitive searches for a single whitespace-delimited, case-insensitive 
token per query.  Some example tokens are:
  ```
  baseball
  baseball,
  full-time
  fun!
  ```
  
### Example Output
 
 ```
 …
indexing  http://nicherecruitingreviews.appspot.com/FFE91BED0E9841B28906D20C215FF84B.txt  
indexing  http://nicherecruitingreviews.appspot.com/FFEDAA3CAD704665A78294741630C287.txt

Finished downloading & indexing 1250 colleges in 1.52 seconds

Enter a search token: baseball    
In 2 reviews for Dawson Community College
In 1 review for Avila University 
In 1 review for California State University Chico  
In 1 review for California State University Fresno  
In 1 review for City Colleges of Chicago KennedyKing College  
In 1 review for Concordia University Wisconsin  
In 1 review for Concordia University Irvine  
In 1 review for Franklin & Marshall College  
In 1 review for Georgia Institute of Technology 
In 1 review for Lake Michigan College  
In 1 review for Manhattanville College  
In 1 review for Mercer County Community College  
In 1 review for North Dakota State University  
In 1 review for North Greenville University  
In 1 review for Northwood University West Palm Beach  
In 1 review for Pearl River Community College  
In 1 review for Tacoma Community College  
In 1 review for University of Miami  
In 1 review for University of New Hampshire at Manchester  
In 1 review for University of South Alabama  
In 1 review for University of Wisconsin Stout

Enter a search token: baseball,
In 1 review for California Baptist University
In 1 review for Daniel Webster College
In 1 review for Northwestern Oklahoma State University
In 1 review for Oregon State University
In 1 review for Ozark Christian College


Enter a search token: fun!
In 2 reviews for Webber International University
In 1 review for Concordia University - Montreal
In 1 review for Minnesota State University
In 1 review for National College of Natural Medicine
In 1 review for Texas State University
In 1 review for Warren County Community College

Enter a search keyword: graduated.
In 1 review for Antonelli Institute - Erdenheim
In 1 review for Bryant & Stratton College - Virginia Beach
In 1 review for Heartland Community College
In 1 review for Kaplan Career Institute
In 1 review for Laney College
In 1 review for Miles College
In 1 review for Texas State Technical College - Harlingen

Enter a search token: full-time
In 2 reviews for Three Rivers Community College - Connecticut
In 1 review for Argosy University - Twin Cities
In 1 review for Bainbridge College
In 1 review for Berkeley College - Woodland Park
In 1 review for Brandman University
In 1 review for Brookhaven College
In 1 review for Centenary College - New Jersey
In 1 review for Chattanooga State Community College
In 1 review for Collins College
In 1 review for CUNY New York City College of Technology
In 1 review for Everest College - Anaheim
In 1 review for Everest University - North Orlando
In 1 review for Fashion Institute of Design & Merchandising - Los Angeles
In 1 review for Hinds Community College
In 1 review for Joliet Junior College
In 1 review for Jones International University
In 1 review for Lincoln College of Technology - Franklin
In 1 review for Linfield College - Adult Degree Program
In 1 review for Los Angeles Southwest College
In 1 review for New York Law School
In 1 review for Ohio University - Eastern
In 1 review for Pierce College - Los Angeles
In 1 review for Rasmussen College - Green Bay
In 1 review for Rich Mountain Community College
In 1 review for Richard Bland College of the College of William & Mary
In 1 review for Rochester Community & Technical College
In 1 review for Rosalind Franklin University of Medicine & Science
In 1 review for Sheridan Technical Center - Adult Education
In 1 review for St. Cloud Technical & Community College
In 1 review for SUNY Delhi
In 1 review for The Illinois Institute of Art - Chicago
In 1 review for University of St. Augustine for Health Sciences
In 1 review for Warren Wilson College
In 1 review for Washburn University
In 1 review for West Virginia University at Parkersburg

 ```
   
## Instructions
 - Create a branch in this repository to contain your work
 - Implement your solution any language you like, as long as it is well suited to the task at hand.
   Pick a language which you are comfortable with, and which will best allow you to demonstrate your ability.  
 - When ready, submit your solution by making a Github Pull Request from your branch to the `main`
 branch.
 - We ask that you submit your solution within 7 days.
 
## What to focus on
 - Use appropriate data structures for the task at hand. There is no need to code exotic data structures 
 to support full-text search. 
  - Try to minimize the elapsed time from running your program to the user being able to search.  We would 
 like to see that you understand where bottlenecks and latency exist and that you can implement techniques 
 to mitigate their effects.
 - Ensure your code is well structured, readable, and appropriately commented.
 - Include documentation on how to build/run your solution, as well as any an explanation of your thought 
 process or any design decisions you made. Feel free to replace this README.md in your branch.


## Questions?
If you have any questions, feel free to email us (vivan.shah@niche.com).  We are happy to clarify anything that is unclear, but 
we may politely decline to answer any specific questions related to design or implementation.

