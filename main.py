#!/usr/bin/python

import urllib2
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#global variables

data=[]
words=[]
url=""
filename='bettercloud.txt'
keyword1='David Hardwick'#where to start saving data from the webpage
keyword2='Bart Hacking'#where to stop saving data from the webpage

#go to bettercloud website hover over company navigate to management wait till management completely loads up and then read the necessary data and write it to a file
def navigate_webpage():
	driver = webdriver.Firefox()
	driver.get("https://www.bettercloud.com")
	element_to_hover_over=driver.find_element_by_class_name('menu-item-4286')
	element_to_click=driver.find_element_by_id('menu-item-4418')
	actions = ActionChains(driver)
	actions.move_to_element(element_to_hover_over)
	actions.click(element_to_click)
	actions.perform()	
	url=str(driver.current_url)
	html = driver.page_source
	html = html.encode('ascii','ignore')
	with open(filename,'w') as myfile:
		myfile.write(html)	
	

#reads the data from bettercloud.txt and extracts the necessary data about David Hardwick
def read_file():
	with open(filename,'r') as f:
		for line in f:
			if keyword1 in line:
				break		
		for line in f:
			if keyword2 in line:
				break
			if '.' in line:
				if '<p></p>\n' in line:
					break
				data.append(line)


#extracts the last word from each sentence about david hardwick
def read_words():  
	temp = (''.join(data)).split('.')
	for element in temp:
		words_list=element.split()
		if len(words_list)>4:
			words.append(words_list[len(words_list)-1])

                
def main():
	navigate_webpage()
	read_file()
	read_words()
	print ' , '.join(sorted(words,key=str.lower))#sorts the last words
	
if __name__ == "__main__":
	main()

