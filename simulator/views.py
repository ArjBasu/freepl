# Create your views here.
from django.shortcuts import render
from simulator.models import *
from django.http import HttpResponse,HttpResponseRedirect
from pyquery import PyQuery as pq

def dashboard(request):
    return render(request,"index.html",{
        "title":"Welcome to Freepl",
                                 })
    
def extract(request):
    teams = [1,2,3,5,6,8]
    for team in teams:
        link = "http://www.espncricinfo.com/india/content/player/country.html?country="+str(team)
        page = pq(url = link)
        playerspage = page("#rectPlyr_Playerlistodi .playersTable td a")
        country = page(".ciGblSectionHead").eq(0).html()
        country = country.split(":")
        country = country[1]
        country = country[1:]
        for counter,f in enumerate(playerspage):
            player = playerspage.eq(counter)
            name = player.html()
            playerlink = "http://www.espncricinfo.com"+player.attr("href")
            pl = pq(url = playerlink)
            matches = pl(".engineTable").eq(0).find(".data1").eq(1).find("td").eq(1).html()
            if(matches == "-"):
                matches = 0
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
            
            fullname = pl(".ciPlayernametxt h1").text()
                
            catches = pl(".engineTable").eq(0).find(".data1").eq(1).find("td").eq(13).html()
            if(catches == "-"):
                catches = 0
            wickets = pl(".engineTable").eq(1).find(".data1").eq(1).find("td").eq(5).html()
            if(wickets == "-"):
                wickets = 0
            bowlavg = pl(".engineTable").eq(1).find(".data1").eq(1).find("td").eq(8).html()
            
            if(bowlavg == "-"):
                bowlavg = 0 
                
                
            playertemp = players(
                                 player_code_name = str(name),
                                 player_full_name = str(fullname),
                                 player_country = str(country),
                                 player_role = str(role),
                                 player_bat_avg = float(battingavg),
                                 player_matches = int(matches),
                                 player_runs = int(runs),
                                 player_wickets = int(wickets),
                                 player_bowl_avg = float(bowlavg),
                                 player_catches = int(catches)
                                 )
            playertemp.save() 
            
            
            
        
    response = "<html></html>"
    return HttpResponse(response)

def testingdataentry(request):
    user = users()
    return "<html></html"
def landing(request):
    return render(request,"landing.html",{"title":"FreePL",})

def team(request):
    return render(request,"team.html")
