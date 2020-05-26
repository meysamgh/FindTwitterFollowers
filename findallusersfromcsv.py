#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:20:27 2018

@author: meysam
"""
import time
import tweepy
import csv


#Your Twitter Credentials here
consumer_key ='X'
consumer_secret='X'
access_token='X'
access_token_secret='X'
users=[];
def getallfollowers(screenname):
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    ids = []
# first crawled profile: ricardorossello
#second: agarciapadilla
# third:salpr 
   
    for page in tweepy.Cursor(api.followers_ids, screen_name=screenname).pages():
        #while True:
         #   try:
                ids.extend(page)
                api.wait_on_rate_limit
                for e in ids:
                    api.wait_on_rate_limit
                    user=api.get_user(e);
                    #print(user.screen_name, user.location,user.statuses_count, user.followers_count)
                    users.append([user.screen_name, user.location,user.statuses_count, user.followers_count])                    
                        #print (user.name , user.screen_name, user.location)
                        #print("********************")
                    #time.sleep(60)
              #  except tweepy.TweepError:
               #     time.sleep(60 * 15)
                #    continue
                #except StopIteration:
                 #   break
if __name__ == '__main__':
       with open('twitterusers.csv', 'r') as csvfile:
        reader=csv.DictReader(csvfile)
        count=1;
        for row in reader:
            flag=0;
            count=count+1
            #print(row['name'])
			# Get a subset of the followers of the users from your CSV file
            if row['location'] and count<1000 and count>=100:
			# This will filter some users based on their location and minimum number of followers before trying to get their followers
                if (row['location'].find("PR") !=-1 or row['location'].find("Rico")!=-1 or row['location'].find("Puerto")!=-1 or row['location'].find("san juan")!=-1):
                    #print("***************",row['name'], "    ", row['location'],"***************************************************")                               
                    print("count=", count)
                    if int(row['followers'])>5 and (flag==0):                
                        try:
                            getallfollowers(row['name'])                    
                           
                        except tweepy.TweepError: 
                            flag=1
							# sleeping for rate limit
                            time.sleep(60 * 15)
                            continue
                        except StopIteration:                      
                            break
		# Writing the list of extracted users information into the csv file
        with open("twitter1.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(["name", "location","tweets", "followers"])
            writer.writerows(users)



