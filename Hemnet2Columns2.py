# -*- coding: ISO-8859-1 -*-

# Reformat data slutpriser laegenheter from Hemnet.se
# createdBy Frank Schliephacke, 2019

### -*- coding: utf-8 -*-


import numpy as np
import pandas as pd

#import matplotlib.pyplot as plt

import warnings




def CountLines(fn):
  cnt = 0
  with open(fn) as f:
     line = f.readline()
     data = line.strip().split(',')
     print(len(data))   
     while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       #data = line.strip().split(',')[1:]
       cnt += 1
       line = f.readline() 
  f.close()
  #print(cnt)
  return cnt
 

def hemnet2csv20(fn1, fn2):
  # Version 2.0
  #
#L1 Fyrvaktarkroken 26
#L2 Bostadsrättslägenhet Blåsut, Stockholm
#L3 47 m²   2 rum
#L4 3 133 kr/man
#L5 Slutpris 3 100 000 kr
#L6 Såld 13 juli 2019
#L7 95 652 kr/m²
#L8 +19 %
#L9 
#L10 Fastighetsbyran Enskede
  #
  linelast = ["" for x in range(22)]
  lc = -1
  cnt = 0
  with open(fn2,mode='w') as fout:
    fout.write('A,B,C,D,E,F,G,H')
    fout.write("\n")
    with open(fn1,mode='r') as f:
      line  = f.readline().replace('\n', '') # read first line - dummy line / comment
      while line:
        line  = f.readline()
        #line  = f.readline().replace('\n', '')
        #lineRaw  = f.readline()
        testline = line.strip()
		#line  = lineRaw.replace('\n', '')
        #if testline.find('Slutpris')>=0:
        #  print('TEST', cnt,' ',lc,' ',testline,' ',(testline.find('Slutpris')>=0),'TXT',line)
        #		  
        if (testline.find('Slutpris')>=0):
          #lineout=line.strip()
          #line6 = f.readline().replace('\n', '')
          #line7 = f.readline().replace('\n', '')
          #line8 = f.readline().replace('\n', '')
          #line9 = f.readline().replace('\n', '')
          #line10 = f.readline().replace('\n', '')
          #
          #line6 = f.readline().strip()
          #line7 = f.readline().strip()
          #line8 = f.readline().strip()
          #line9 = f.readline().strip()
          #line10 = f.readline().strip()
          #
          lc +=1
          linelast[lc] = line.strip()
          linelast[lc+1] = f.readline().strip()
          linelast[lc+2] = f.readline().strip()
          linelast[lc+3] = f.readline().strip()
          linelast[lc+4] = f.readline().strip()
          #linelast[lc+5] = f.readline().strip()
          #linelast[lc]= f.readline().replace('\n', '')
          #
          cnt += 1
          fout.write(linelast[lc-4]) # line1
          fout.write(',')
          fout.write(linelast[lc-3]) # line2
          fout.write(',')
          fout.write(linelast[lc-2]) # line3
          fout.write(',')
          fout.write(linelast[lc-1])  #4
          fout.write(',')
          fout.write(linelast[lc])  #?
          #fout.write(',')
          #fout.write(lineout)  #5
          #fout.write(',')
          #fout.write(line6)  #6
          #fout.write(',')
          #fout.write(line7)  #7
          #fout.write(',')
          #fout.write(line8)  #8
          #fout.write(',')
          #fout.write(line9)  #9
          #fout.write(',')
          #fout.write(line10)  #10
          fout.write(',')
          fout.write(linelast[lc+1])  #10
          fout.write(',')
          fout.write(linelast[lc+2]) 
          fout.write(',')
          fout.write(linelast[lc+3]) 
          fout.write(',')
          fout.write(linelast[lc+4]) 
          #fout.write(',')
          #fout.write(linelast[lc+5]) 
          fout.write('\n')
          print('OUT',lc,' ',cnt,linelast[lc-4],linelast[lc-3],linelast[lc-2],linelast[lc-1],linelast[lc],linelast[lc+1],linelast[lc+2],linelast[lc+3],linelast[lc+4],linelast[+5])
          lc = -1
          linelast = ["" for x in range(22)] # reset
        else:
          lc +=1
          linelast[lc]=line.replace('\n', '')
          print(lc,'linelast',linelast[lc])
  #
  f.close()
  fout.close()
  return cnt


def hemnet2csv30(fn1, fn2):
  # Version 3.0
  #
#L1 Fyrvaktarkroken 26
#L2 Bostadsrättslägenhet Blåsut, Stockholm
#L3 47 m²   2 rum
#L4 3 133 kr/man
#L5 Slutpris 3 100 000 kr
#L6 Såld 13 juli 2019
#L7 95 652 kr/m²
#L8 +19 %
#L9 
#L10 Fastighetsbyran Enskede
  #
  linelast = ["" for x in range(22)]
  lc = -1
  cnt = 0
  with open(fn2,mode='w') as fout:
    fout.write('Street,ApType,Area,Monthcost,Finalprice,Fpricesqm,dummy1,Estateagent')
    fout.write("\n")
    with open(fn1,mode='r') as f:
      line  = f.readline() # read first line - dummy line / comment
      line  = f.readline() # read second line - dummy line / comment
      while line: # and cnt<5:
        line  = f.readline()
        #line  = f.readline().replace('\n', '')
        #lineRaw  = f.readline()
        testline = line.strip()
		#line  = lineRaw.replace('\n', '')
        #if testline.find('Slutpris')>=0:
        #  print('TEST', cnt,' ',lc,' ',testline,' ',(testline.find('Slutpris')>=0),'TXT',line)
        #		  
        if (testline.find('Slutpris')>=0):
          #lineout=line.strip()
          #line6 = f.readline().replace('\n', '')
          #line7 = f.readline().replace('\n', '')
          #line8 = f.readline().replace('\n', '')
          #line9 = f.readline().replace('\n', '')
          #line10 = f.readline().replace('\n', '')
          #
          #line6 = f.readline().strip()
          #line7 = f.readline().strip()
          #line8 = f.readline().strip()
          #line9 = f.readline().strip()
          #line10 = f.readline().strip()
          #
          lc +=1
          linelast[lc] = line.strip()
          linelast[lc+1] = f.readline().strip()
          linelast[lc+2] = f.readline().strip()
          linelast[lc+3] = f.readline().strip()
          linelast[lc+4] = f.readline().strip()
          #linelast[lc+5] = f.readline().strip()
          #linelast[lc]= f.readline().replace('\n', '')
		  #
          for xc in range(lc+4+1):
            #print(xc)
            temptext=linelast[xc].split(' ')
            if linelast[xc].find('Slutpris')>=0:
              tmpstr=linelast[xc]
              linelast[xc]='SlutprisSEK ' + str(int(tmpstr[8:-3].replace(' ', '')))
              print('Process SLUTPRIS',linelast[xc],' ',tmpstr,' ',int(tmpstr[8:-3].replace(' ', '')),'\n')
            if linelast[xc].find('kr/m2')>=0:
              tmpstr=linelast[xc]
              linelast[xc]=str(int(tmpstr[:-6].replace(' ', '')))+' kr/m2'
            if linelast[xc].find('kr/man')>=0:
              tmpstr=linelast[xc]
              linelast[xc]=str(int(tmpstr[:-7].replace(' ', '')))+' kr/man'
            if linelast[xc].find('Bostadsrat')>=0:
              tmpstr=linelast[xc].split(' ')
              print(len(tmpstr),' ',tmpstr)
              if len(tmpstr)>1:
                linelast[xc]=""
                for ic in range(1,len(tmpstr)):
                  linelast[xc]+=tmpstr[ic]
            if linelast[xc].find(' tr')>=0:
              tmpstr=linelast[xc].split(',')
              print(len(tmpstr),' ',tmpstr)
              if len(tmpstr)>1:
                linelast[xc]=""
                for ic in range(0,len(tmpstr)-1):
                  linelast[xc]+=tmpstr[ic]
              print('NEW',linelast[xc])
            if linelast[xc].find(' tr')>=0:
              tmpstr=linelast[xc].split(' ')
              print(len(tmpstr),' ',tmpstr)
              if len(tmpstr)>1:
                linelast[xc]=""
                for ic in range(0,len(tmpstr)-2):
                  linelast[xc]+=tmpstr[ic]
              print('NEW',linelast[xc])
          #
          cnt += 1
          if lc<5:
          #  lc += 1
            fout.write(linelast[0]) # line1
            fout.write(',')
          fout.write(linelast[lc-4]) # line1
          fout.write(',')
          fout.write(linelast[lc-3]) # line2
          fout.write(',')
          fout.write(linelast[lc-2]) # line3
          fout.write(',')
          fout.write(linelast[lc-1])  #4
          fout.write(',')
          fout.write(linelast[lc])  #?
          #fout.write(',')
          #fout.write(lineout)  #5
          #fout.write(',')
          #fout.write(line6)  #6
          #fout.write(',')
          #fout.write(line7)  #7
          #fout.write(',')
          #fout.write(line8)  #8
          #fout.write(',')
          #fout.write(line9)  #9
          #fout.write(',')
          #fout.write(line10)  #10
          fout.write(',')
          fout.write(linelast[lc+1])  #10
          fout.write(',')
          fout.write(linelast[lc+2]) 
          fout.write(',')
          fout.write(linelast[lc+3]) 
          fout.write(',')
          fout.write(linelast[lc+4]) 
          #fout.write(',')
          #fout.write(linelast[lc+5]) 
          fout.write('\n')
          if lc<5:
            print('OUT',lc,' ',cnt,linelast[lc-5],linelast[lc-4],linelast[lc-3],linelast[lc-2],linelast[lc-1],linelast[lc],linelast[lc+1],linelast[lc+2],linelast[lc+3],linelast[lc+4])
          else:
            print('OUT',lc,' ',cnt,linelast[lc-4],linelast[lc-3],linelast[lc-2],linelast[lc-1],linelast[lc],linelast[lc+1],linelast[lc+2],linelast[lc+3],linelast[lc+4],linelast[+5])
          lc = -1
          linelast = ["" for x in range(22)] # reset
		  #
          #f.close()
          #fout.close()
          #exit()
        else:
          lc +=1
          linelast[lc]=line.replace('\n', '')
          #print(lc,'linelast',linelast[lc])
  #
  f.close()
  fout.close()
  return cnt

nsales=0  
#nsales=hemnet2csv20('Hemnet_slutpriser_July2019_cleaned.txt', 'HemnetTable.txt')
#nsales=hemnet2csv30('Hemnet_slutpriser_July2019_cleaned2.txt', 'HemnetTable.txt')
print('No of sales=',nsales)

def deleteTrappa(str1):
  # delete tr, in str1
  txt=str1.split(',')
  newtxt=txt[0]
  for ic in range(1,len(txt)):
    tmpstr=txt[ic].upper()
    print('tmpstr ',tmpstr)
    if len(tmpstr)>=2:
      if (tmpstr[-2]=='T') and (tmpstr[-1]=='R') :
        print('Remove tr ',tmpstr)
      else:
        newtxt+=','+txt[ic]
  #
  print('NEW ',newtxt)
  return newtxt

def deleteVaning(str1):
  # delete tr, in str1
  txt=str1.split(',')
  newtxt=txt[0]
  for ic in range(1,len(txt)):
    tmpstr=txt[ic].upper()
    print('tmpstr ',tmpstr)
    if (tmpstr.find(' VAN')>=0):
      print('Remove VAN ',tmpstr)
    else:
      newtxt+=','+txt[ic]
  #
  print('NEW ',newtxt)
  return newtxt


#newtrappa=deleteTrappa('Bergslagsvagen 76, 4tr,akeshov,Stockholm,64 m2   2 rum,3576 kr/man,SlutprisSEK 3195000,Sald 2 juli 2019,49922 kr/m2,,Fastighetsbyran Bromma')


#!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

def GetLatLong(myaddress):
    geolocator = Nominatim(user_agent="ny_explorer")
    location = geolocator.geocode(myaddress)
    latitude = location.latitude
    longitude = location.longitude
    return latitude, longitude

# test geocoder
streetaddress= 'Torsgatan 3, Stockholm, Sweden'
latitude, longitude = GetLatLong(streetaddress)
print('The geograpical coordinate of {} are {}, {}.'.format(streetaddress, latitude, longitude))


def hemnetlocationtable(fn1, fn2):
  # Version 1.0
  #
# Fyrvaktarkroken 26, Fyrvaktarkroken 26,Blasut,Stockholm,47 m2   2 rum,3133 kr/man,SlutprisSEK 3100000,Sald 13 juli 2019,65957 kr/m2,+19 %,
# Sibeliusgangen 50,Kista,Stockholm,80,9 m2   3 rum,4634 kr/man,SlutprisSEK 1995000,Sald 13 juli 2019,24660 kr/m2,,Notar
  #
  lc = -1
  cnt = 0
  with open(fn2,mode='w') as fout:
    fout.write('Lat,Long,Street,PriceSEK,PriceSQM,Size')
    fout.write("\n")
    with open(fn1,mode='r') as f:
      line  = f.readline().replace('\n', '') # read first line - dummy line / comment
      while line:
        #line  = f.readline()
        line  = f.readline().strip()
		#line  = f.readline().replace('\n', '')
        if (line.find('tr,')>=0):
          tmpline=line
          line=deleteTrappa(tmpline)
		#
        line=line.upper()
        #line=tmpline
        if (line.find(' VAN')>=0):
          line=deleteVaning(line)
		#
		#
        print('LINE: ',line)
        if (line.find('SLUTPRISSEK')>=0):
          linelast = line.split(',')
          #
          if len(linelast)>3:
             tmpstr=linelast[0]
             if linelast[0].find(linelast[1])<0:
               tmpstr+=','+linelast[1]
               tmpstr+=','+linelast[2]+',Stockholm,Sweden'
             else:
               tmpstr+=','+linelast[2]
               tmpstr+=','+linelast[3]+',Stockholm,Sweden'
			 #
			 #tmpstr+=','+linelast[3]+',Stockholm,Sweden'
			 #
			 # get geolocation
             streetaddress=tmpstr
             latitude=0.0
             longitude=0.0
			 latitude, longitude = GetLatLong(streetaddress)
             print('Address',streetaddress,latitude,longitude)
          #
          cnt += 1
		  #
          fout.write(str(latitude)) # line1
          fout.write(',')
          fout.write(str(longitude)) # line2
          fout.write(',')
          fout.write(streetaddress) # line3
		  #
          for xc in range(3,len(linelast)):
            if (linelast[xc].find('SLUTPRISSEK')>=0):
              fout.write(',')
              fout.write(linelast[xc])
              print(',',linelast[xc])
            if (linelast[xc].find('KR/M2')>=0):
              fout.write(',')
              fout.write(linelast[xc])
              print(',',linelast[xc])			  
          fout.write('\n')
          #print('OUT',lc,' ',cnt,linelast[lc-4],linelast[lc-3],linelast[lc-2],linelast[lc-1],linelast[lc],linelast[lc+1],linelast[lc+2],linelast[lc+3],linelast[lc+4],linelast[+5])
          #
  #
  f.close()
  fout.close()
  return cnt


nstreets=0
nstreets=hemnetlocationtable('HemnetTable.txt','HemnetGeoLocations.txt')
print('No of street locations ',nstreets)
