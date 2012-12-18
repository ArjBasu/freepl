# Create your views here.
from django.shortcuts import render
from simulator.models import players,performance,users
from django.http import HttpResponse,HttpResponseRedirect
from pyquery import PyQuery as pq

def landing(request):
    return render(request,"index.html",{
        "title":"Welcome to Freepl",
                                 })
    
def extract(request):
    teams = [1,2,3,5,6,8]
    for team in teams:
        link = "http://www.espncricinfo.com/india/content/player/country.html?country="+str(team)
        page = pq(url = link)
        players = page("#rectPlyr_Playerlistodi .playersTable td a")
        country = page(".ciGblSectionHead").eq(0).html()
        country = country.split(":")
        country = country[1]
        country = country[1:]
        for counter,f in enumerate(players):
            player = players.eq(counter)
            name = player.html()
            playerlink = "http://www.espncricinfo.com"+player.attr("href")
            pl = pq(url = playerlink)
            matches = pl(".engineTable").eq(0).find(".data1").eq(1).find("td").eq(1).html()
            runs = pl(".engineTable").eq(0).find(".data1").eq(1).find("td").eq(4).html()
            if(runs == "-"):
                runs = 0
            battingavg = pl(".engineTable").eq(0).find(".data1").eq(1).find("td").eq(6).html()
            if(battingavg == "-"):
                battingavg = 0
            info = pl(".ciPlayerinformationtxt")
            for counter,f in enumerate(info):
                infotitle = info.eq(counter).find("b").html()
                if(infotitle == "Playing role"):
                    role = info.eq(counter).find("span").html()
                    break
                
            catches = pl(".engineTable").eq(0).find(".data1").eq(1).find("td").eq(13).html()
            wickets = pl(".engineTable").eq(1).find(".data1").eq(1).find("td").eq(5).html()
            bowlavg = pl(".engineTable").eq(1).find(".data1").eq(1).find("td").eq(8).html()
            if(bowlavg == "-"):
                bowlavg = 0 
            
        
    response = "<html></html>"
    return HttpResponse(response)

def team(request):
    return render(request,"team.html")
