#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[27]:


def MaintainanceCals(Age, AGAB, exerciseFrequency, BodyMassIndex):
    AvgCals=2000
    StDevCals=math.sqrt((MaintainCals-AvgCals)**2)
    if Age<18:
        print("Error: Values may be out of range. This calculator is meant for adults. Dieting can be unsafe for those under 18.")
    elif AGAB=='M':
        if Age>=18:
            if exerciseFrequency=='1':
               MaintainCals=2400 
            elif exerciseFrequency=='2':
                MaintainCals=2800
            elif exerciseFrequency=='3':
                MaintainCals=3200
        elif Age>=19 and Age<=20:
            if exerciseFrequency=='1':
                MaintainCals=2600
            elif exerciseFrequency=='2':
                MaintainCals=2800
            elif exerciseFrequency=='3':
                MaintainCals=3000
        elif Age>=21 and Age<=25:
            if exerciseFrequency=='1':
                MaintainCals=2400
            elif exerciseFrequency=='2':
                MaintainCals=2800
            elif exerciseFrequency=='3':
                MaintainCals=3000
        elif Age>=26 and Age<=30:
            if exerciseFrequency=='1':
                MaintainCals=2400
            elif exerciseFrequency=='2':
                MaintainCals=2600
            elif exerciseFrequency=='3':
                MaintainCals=3000
        elif Age>=31 and Age<=35:
            if exerciseFrequency=='1':
                MaintainCals=2400
            elif exerciseFrequency=='2':
                MaintainCals=2600
            elif exerciseFrequency=='3':
                MaintainCals=3000
        elif Age>=36 and Age<=40:
            if exerciseFrequency=='1':
                MaintainCals=2400
            elif exerciseFrequency=='2':
                MaintainCals=2600
            elif exerciseFrequency=='3':
                MaintainCals=3000
        elif Age>=41 and Age<=45:
            if exerciseFrequency=='1':
                MaintainCals=2200
            elif exerciseFrequency=='2':
                MaintainCals=2600
            elif exerciseFrequency=='3':
                MaintainCals=2800
        elif Age>=46 and Age<=50:
            if exerciseFrequency=='1':
                MaintainCals=2200
            elif exerciseFrequency=='2':
                MaintainCals=2200
            elif exerciseFrequency=='3':
                MaintainCals=2800
        elif Age>=51 and Age<=55:
            if exerciseFrequency=='1':
                MaintainCals=2200
            elif exerciseFrequency=='2':
                MaintainCals=2400
            elif exerciseFrequency=='3':
                MaintainCals=2800
        elif Age>=56 and Age<=60:
            if exerciseFrequency=='1':
                MaintainCals=2200
            elif exerciseFrequency=='2':
                MaintainCals=2400
            elif exerciseFrequency=='3':
                MaintainCals=2600
        elif Age>=61 and Age<=65:
            if exerciseFrequency=='1':
                MaintainCals=2000
            elif exerciseFrequency=='2':
                MaintainCals=2400
            elif exerciseFrequency=='3':
                MaintainCals=2600
        elif Age>=66 and Age<=70:
            if exerciseFrequency=='1':
                MaintainCals=2000
            elif exerciseFrequency=='2':
                MaintainCals=2200
            elif exerciseFrequency=='3':
                MaintainCals=2600
        elif Age>=71 and Age<=75:
            if exerciseFrequency=='1':
                MaintainCals=2000
            elif exerciseFrequency=='2':
                MaintainCals=2200
            elif exerciseFrequency=='3':
                MaintainCals=2600
        elif Age>75:
            if exerciseFrequency=='1':
                MaintainCals=2000
            elif exerciseFrequency=='2':
                MaintainCals=2200
            elif exerciseFrequency=='3':
                MaintainCals=2400
    elif AGAB=='F':
        if Age>=18:
            if exerciseFrequency=='1':
               MaintainCals=1800 
            elif exerciseFrequency=='2':
                MaintainCals=2000
            elif exerciseFrequency=='3':
                MaintainCals=2400
        elif Age>=19 and Age<=20:
            if exerciseFrequency=='1':
                MaintainCals=2000
            elif exerciseFrequency=='2':
                MaintainCals=2200
            elif exerciseFrequency=='3':
                MaintainCals=2400
        elif Age>=21 and Age<=25:
            if exerciseFrequency=='1':
                MaintainCals=2000
            elif exerciseFrequency=='2':
                MaintainCals=2200
            elif exerciseFrequency=='3':
                MaintainCals=2400
        elif Age>=26 and Age<=30:
            if exerciseFrequency=='1':
                MaintainCals=1800
            elif exerciseFrequency=='2':
                MaintainCals=2000
            elif exerciseFrequency=='3':
                MaintainCals=2400
        elif Age>=31 and Age<=35:
            if exerciseFrequency=='1':
                MaintainCals=1800
            elif exerciseFrequency=='2':
                MaintainCals=2000
            elif exerciseFrequency=='3':
                MaintainCals=2200
        elif Age>=36 and Age<=40:
            if exerciseFrequency=='1':
                MaintainCals=1800
            elif exerciseFrequency=='2':
                MaintainCals=2000
            elif exerciseFrequency=='3':
                MaintainCals=2200
        elif Age>=41 and Age<=45:
            if exerciseFrequency=='1':
                MaintainCals=1800
            elif exerciseFrequency=='2':
                MaintainCals=2000
            elif exerciseFrequency=='3':
                MaintainCals=2200
        elif Age>=46 and Age<=50:
            if exerciseFrequency=='1':
                MaintainCals=1800
            elif exerciseFrequency=='2':
                MaintainCals=2000
            elif exerciseFrequency=='3':
                MaintainCals=2200
        elif Age>=51 and Age<=55:
            if exerciseFrequency=='1':
                MaintainCals=1600
            elif exerciseFrequency=='2':
                MaintainCals=1800
            elif exerciseFrequency=='3':
                MaintainCals=2200
        elif Age>=56 and Age<=60:
            if exerciseFrequency=='1':
                MaintainCals=1600
            elif exerciseFrequency=='2':
                MaintainCals=1800
            elif exerciseFrequency=='3':
                MaintainCals=2200
        elif Age>=61 and Age<=65:
            if exerciseFrequency=='1':
                MaintainCals=1600
            elif exerciseFrequency=='2':
                MaintainCals=1800
            elif exerciseFrequency=='3':
                MaintainCals=2000
        elif Age>=66 and Age<=70:
            if exerciseFrequency=='1':
                MaintainCals=1600
            elif exerciseFrequency=='2':
                MaintainCals=1800
            elif exerciseFrequency=='3':
                MaintainCals=2000
        elif Age>=71 and Age<=75:
            if exerciseFrequency=='1':
                MaintainCals=1600
            elif exerciseFrequency=='2':
                MaintainCals=1800
            elif exerciseFrequency=='3':
                MaintainCals=2000
        elif Age>75:
            if exerciseFrequency=='1':
                MaintainCals=1600
            elif exerciseFrequency=='2':
                MaintainCals=1800
            elif exerciseFrequency=='3':
                MaintainCals=2000
    elif AGAB!='M' or AGAB!='F':
        print("Error: Values may be out of range.")

    if BMI=='underweight':
        return MaintainCals+(StDevCals*1.5)
    elif BMI=='healthy':
        return MaintainCals+(StDevCals)
    elif BMI=='overweight':
        return MaintainCals+(StDevCals*-1.5)
    elif BMI=='obese':
        return MaintainCals+(StDevCals*-2)
    elif BMI=='extremely obese':
        return MaintainCals+(StDevCals*-2.5)   
    
def BodyMassIndex(Height, Weight):
    if Height<56 and Weight<90:
        print("Error: Values may be out of range. This calculator is meant for adults. Dieting can be unsafe for those under 18.")
    elif Height==56:
        if Weight<90:
            BMI='underweight'
        elif Weight>=90 and Weight<=109:
            BMI='healthy'
        elif Weight>=110 and Weight<=139:
            BMI='overweight'
        elif Weight>=140 and Weight<=179:
            BMI='obese'
        elif Weight>=180:
            BMI='extremely obese'
    elif Height==57:
        if Weight<90:
            BMI='underweight'
        elif Weight>=90 and Weight<=119:
            BMI='healthy'
        elif Weight>=120 and Weight<=139:
            BMI='overweight'
        elif Weight>=140 and Weight<=189:
            BMI='obese'
        elif Weight>=190:
            BMI='extremely obese'
    elif Height==58:
        if Weight<90:
            BMI='underweight'
        elif Weight>=90 and Weight<=119:
            BMI='healthy'
        elif Weight>=120 and Weight<=149:
            BMI='overweight'
        elif Weight>=150 and Weight<=199:
            BMI='obese'
        elif Weight>=200:
            BMI='extremely obese'
    elif Height==59:
        if Weight<99:
            BMI='underweight'
        elif Weight>=100 and Weight<=129:
            BMI='healthy'
        elif Weight>=130 and Weight<=149:
            BMI='overweight'
        elif Weight>=150 and Weight<=199:
            BMI='obese'
        elif Weight>=200:
            BMI='extremely obese'
    elif Height==60:
        if Weight<99:
            BMI='underweight'
        elif Weight>=100 and Weight<=129:
            BMI='healthy'
        elif Weight>=130 and Weight<=159:
            BMI='overweight'
        elif Weight>=160 and Weight<=209:
            BMI='obese'
        elif Weight>=210:
            BMI='extremely obese'
    elif Height==61:
        if Weight<99:
            BMI='underweight'
        elif Weight>=100 and Weight<=129:
            BMI='healthy'
        elif Weight>=130 and Weight<=159:
            BMI='overweight'
        elif Weight>=100 and Weight<=209:
            BMI='obese'
        elif Weight>=210:
            BMI='extremely obese'
    elif Height==62:
        if Weight<109:
            BMI='underweight'
        elif Weight>=110 and Weight<=139:
            BMI='healthy'
        elif Weight>=140 and Weight<=169:
            BMI='overweight'
        elif Weight>=170 and Weight<=219:
            BMI='obese'
        elif Weight>=220:
            BMI='extremely obese'
    elif Height==63:
        if Weight<109:
            BMI='underweight'
        elif Weight>=110 and Weight<=139:
            BMI='healthy'
        elif Weight>=140 and Weight<=169:
            BMI='overweight'
        elif Weight>=170 and Weight<=229:
            BMI='obese'
        elif Weight>=230:
            BMI='extremely obese'
    elif Height==64:
        if Weight<109:
            BMI='underweight'
        elif Weight>=110 and Weight<=149:
            BMI='healthy'
        elif Weight>=150 and Weight<=179:
            BMI='overweight'
        elif Weight>=180 and Weight<=239:
            BMI='obese'
        elif Weight>=240:
            BMI='extremely obese'
    elif Height==65:
        if Weight<119:
            BMI='underweight'
        elif Weight>=120 and Weight<=149:
            BMI='healthy'
        elif Weight>=150 and Weight<=179:
            BMI='overweight'
        elif Weight>=180 and Weight<=239:
            BMI='obese'
        elif Weight>=240:
            BMI='extremely obese'
    elif Height==66:
        if Weight<119:
            BMI='underweight'
        elif Weight>=120 and Weight<=159:
            BMI='healthy'
        elif Weight>=160 and Weight<=189:
            BMI='overweight'
        elif Weight>=190 and Weight<=249:
            BMI='obese'
        elif Weight>=250:
            BMI='extremely obese'
    elif Height==67:
        if Weight<119:
            BMI='underweight'
        elif Weight>=120 and Weight<=159:
            BMI='healthy'
        elif Weight>=160 and Weight<=189:
            BMI='overweight'
        elif Weight>=190 and Weight<=259:
            BMI='obese'
        elif Weight>=260:
            BMI='extremely obese'
    elif Height==68:
        if Weight<129:
            BMI='underweight'
        elif Weight>=130 and Weight<=169:
            BMI='healthy'
        elif Weight>=170 and Weight<=199:
            BMI='overweight'
        elif Weight>=200 and Weight<=259:
            BMI='obese'
        elif Weight>=260:
            BMI='extremely obese'
    elif Height==69:
        if Weight<129:
            BMI='underweight'
        elif Weight>=130 and Weight<=169:
            BMI='healthy'
        elif Weight>=170 and Weight<=199:
            BMI='overweight'
        elif Weight>=200 and Weight<=269:
            BMI='obese'
        elif Weight>=270:
            BMI='extremely obese'
    elif Height==70:
        if Weight<129:
            BMI='underweight'
        elif Weight>=130 and Weight<=179:
            BMI='healthy'
        elif Weight>=180 and Weight<=209:
            BMI='overweight'
        elif Weight>=210 and Weight<=279:
            BMI='obese'
        elif Weight>=280:
            BMI='extremely obese'
    elif Height==71:
        if Weight<139:
            BMI='underweight'
        elif Weight>=140 and Weight<=179:
            BMI='healthy'
        elif Weight>=180 and Weight<=219:
            BMI='overweight'
        elif Weight>=220 and Weight<=289:
            BMI='obese'
        elif Weight>=290:
            BMI='extremely obese'
    elif Height==72:
        if Weight<139:
            BMI='underweight'
        elif Weight>=140 and Weight<=189:
            BMI='healthy'
        elif Weight>=190 and Weight<=219:
            BMI='overweight'
        elif Weight>=220 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==73:
        if Weight<149:
            BMI='underweight'
        elif Weight>=150 and Weight<=189:
            BMI='healthy'
        elif Weight>=190 and Weight<=229:
            BMI='overweight'
        elif Weight>=230 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==74:
        if Weight<149:
            BMI='underweight'
        elif Weight>=150 and Weight<=199:
            BMI='healthy'
        elif Weight>=200 and Weight<=229:
            BMI='overweight'
        elif Weight>=230 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==75:
        if Weight<149:
            BMI='underweight'
        elif Weight>=150 and Weight<=199:
            BMI='healthy'
        elif Weight>=200 and Weight<=239:
            BMI='overweight'
        elif Weight>=240 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==76:
        if Weight<159:
            BMI='underweight'
        elif Weight>=160 and Weight<=209:
            BMI='healthy'
        elif Weight>=210 and Weight<=249:
            BMI='overweight'
        elif Weight>=250 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==77:
        if Weight<159:
            BMI='underweight'
        elif Weight>=160 and Weight<=209:
            BMI='healthy'
        elif Weight>=210 and Weight<=249:
            BMI='overweight'
        elif Weight>=250 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==78:
        if Weight<169:
            BMI='underweight'
        elif Weight>=170 and Weight<=219:
            BMI='healthy'
        elif Weight>=220 and Weight<=259:
            BMI='overweight'
        elif Weight>=260 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==79:
        if Weight<169:
            BMI='underweight'
        elif Weight>=170 and Weight<=219:
            BMI='healthy'
        elif Weight>=220 and Weight<=269:
            BMI='overweight'
        elif Weight>=270 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==80:
        if Weight<169:
            BMI='underweight'
        elif Weight>=170 and Weight<=229:
            BMI='healthy'
        elif Weight>=230 and Weight<=269:
            BMI='overweight'
        elif Weight>=270 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==81:
        if Weight<179:
            BMI='underweight'
        elif Weight>=180 and Weight<=229:
            BMI='healthy'
        elif Weight>=230 and Weight<=279:
            BMI='overweight'
        elif Weight>=280 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==82:
        if Weight<179:
            BMI='underweight'
        elif Weight>=180 and Weight<=239:
            BMI='healthy'
        elif Weight>=240 and Weight<=289:
            BMI='overweight'
        elif Weight>=290 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    elif Height==83:
        if Weight<189:
            BMI='underweight'
        elif Weight>=190 and Weight<=239:
            BMI='healthy'
        elif Weight>=240 and Weight<=289:
            BMI='overweight'
        elif Weight>=290 and Weight<=299:
            BMI='obese'
        elif Weight>=300:
            BMI='extremely obese'
    else:
        print("Error: Values may be out of range.")

    return BMI

def Protein(BMI,RatioCheck):
    ProteinMax=0.35
    ProteinMin=0.1
    StDevProtein=math.sqrt((ProteinMax-ProteinMin)**2)

    if BMI=='underweight':
        IdealProtein=ProteinMin+(StDevProtein*1.5)*100
        round(IdealProtein,2)
    elif BMI=='healthy':
        IdealProtein=ProteinMin+(StDevProtein)*100
        round(IdealProtein,2)
    elif BMI=='overweight':
        IdealProtein=ProteinMin+(StDevProtein*-1.5)*100
        round(IdealProtein,2)
    elif BMI=='obese':
        IdealProtein=ProteinMin+(StDevProtein*-2)*100
        round(IdealProtein,2)
    elif BMI=='extremely obese':
        IdealProtein=ProteinMin+(StDevProtein*1.5)*100
        round(IdealProtein,2)

    RatioCheck(IdealProtein,IdealFats,IdealCarbs)
    return IdealProtein

def Fats(BMI,RatioCheck):
    FatsMax=0.35
    FatsMin=0.2
    StDevFats=math.sqrt((FatsMax-FatsMin)**2)

    if BMI=='underweight':
        IdealFats=FatsMin+(StDevFats*1.5)*100
        return round(IdealFats,2)
    elif BMI=='healthy':
        IdealFats=FatsMin+(StDevFats)*100
        return round(IdealFats,2)
    elif BMI=='overweight':
        IdealFats=FatsMin+(StDevFats*-1.5)*100
        return round(IdealFats,2)
    elif BMI=='obese':
        IdealFats=FatsMin+(StDevFats*-2)*100
        return round(IdealFats,2)
    elif BMI=='extremely obese':
        IdealFats=FatsMin+(StDevFats*-2.5)*100
        return round(IdealFats,2)

    RatioCheck(IdealProtein,IdealFats,IdealCarbs)
    return IdealFats

def Carbs(BMI,RatioCheck):
    CarbsMax=0.65
    CarbsMin=0.45
    StDevCarbs=math.sqrt((CarbsMax-CarbsMin)**2)

    if BMI=='underweight':
        IdealCarbs=CarbsMin+(StDevCarbs*1.5)*100
        return round(IdealCarbs,2)
    elif BMI=='healthy':
        IdealCarbs=CarbsMin+(StDevCarbs)*100
        return round(IdealCarbs,2)
    elif BMI=='overweight':
        IdealCarbs=CarbsMin+(StDevCarbs*-1.5)*100
        return round(IdealCarbs,2)
    elif BMI=='obese':
        IdealCarbs=CarbsMin+(StDevCarbs*-2)*100
        return round(IdealCarbs,2)
    elif BMI=='extremely obese':
        IdealCarbs=CarbsMin+(StDevCarbs*-2.5)*100
        return round(IdealCarbs,2)

    RatioCheck(IdealProtein,IdealFats,IdealCarbs)
    return IdealCarbs

def RatioCheck(IdealProtein,IdealFats,IdealCarbs):
    if IdealProtein>0.35:
        IdealProtein=0.35
    elif IdealFats>0.35:
        IdealFats=0.35
    elif IdealCarbs>0.65:
        IdealCarbs=0.65
        
def main():
    Age=int(input("Input age in years: "))
    AGAB=input("Input assigned gender at birth: M/F").upper()
    exerciseFrequency=int(input("On a scale from 1-3, rate how frequently you exercise (1 being not at all and 3 being frequently):"))
    Height=float(input("Input height in inches: "))
    Weight=float(input("Input weight in pounds: "))
    N=1
    print(f'Your BMI indicates that you are {BodyMassIndex(Height, Weight)}.\n'
    'Your ideal macronutrient ratio should be:\n'
    f'Protein: {Protein(BodyMassIndex,RatioCheck)}\n'
    f'Fats: {Fats(BodyMassIndex,RatioCheck)}\n'
    f'Carbs: {Carbs(BodyMassIndex,RatioCheck)}')


# In[28]:


main()


# In[ ]:




