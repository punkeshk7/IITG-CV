import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

urlnew=["https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/kolkata-knight-riders-vs-punjab-kings-42nd-match-1426280/full-scorecard"]

def toss(url):
    webpage = requests.get(url)
    web=webpage.content
    soup=BeautifulSoup(web, "html.parser")
    for m in soup.find_all("span"):
        n=m.text
        if"elected" in n:
            print(n)
winner=[toss(url) for url in urlnew]

def matchwinner(url):
    webpage = requests.get(url)
    web=webpage.content
    soup=BeautifulSoup(web, "html.parser")
    for m in soup.find_all("span"):
        n=m.text
        if"won" in n:
            print(n)
winner=[matchwinner(url) for url in urlnew]

def matchwinner(url):
    webpage = requests.get(url)
    web=webpage.content
    soup=BeautifulSoup(web, "html.parser")
    for m in soup.find_all("p",{"class":"ds-text-tight-s"}):
        for span in m.find_all ("span"):
            print(span.text)
winner=[matchwinner(url) for url in urlnew]

def scores(url):
    webpage = requests.get(url)
    web=webpage.content
    soup=BeautifulSoup(web, "html.parser")
    for m in soup.find_all("div",{"class":"ci-team-score"}):
        for s in m.find_all ("strong"):
            print(s.text)
winner=[scores(url) for url in urlnew]

def teamname(url):
    webpage = requests.get(url)
    web=webpage.content
    soup=BeautifulSoup(web, "html.parser") 
    for m in soup.find_all("span",{"class":"ds-text-tight-l"}):
            print(m.text)
winner=[teamname(url) for url in urlnew]





