# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:40:35 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

Program used for experimental study of (i) political science, specifically a mexican standoff scenario, and (ii) information asymmetry in decision making (business) and risk-taking.

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Mexico's Standoff [Computer software]. Github repository <https://github.com/alanjpan/Mexico-s-Standoff>

Futher expansions may include more complex simulations of variables.

Note this software's license is GNU GPLv3.
"""

import random
import sys
import time

secure_random = random.SystemRandom()

turns = 1
countryid = []
countryname = []
tension = []
resources = []
cultures = []
apocalypse = 0
trumpets = 0

nations = ['aus', 'can', 'arab', 'amer', 'ind', 'rus', 'afr', 'tur', 'arg', 'bra', 'fra', 'ger', 'ita', 'uk', 'chi', 'indo', 'jap', 'kor', 'usa', 'cuba', 'sov', 'spa', 'egy', 'nyc', 'la', 'aust' , 'dal', 'phi', 'ber']
actionlist = ['military', 'economy', 'culture', 'trade', 'war']

def init(n):
    global turns
    global countryid
    global countryname
    global tension
    global resources
    global cultures
    global apocalypse
    global trumpets
    
    turns = 1
    countryid.clear()
    countryname.clear()
    tension.clear()
    resources.clear()
    cultures.clear()
    apocalypse = 0
    trumpets = 0
    
    for i in range(n):
        countryid.append(i)
        countryname.append(secure_random.choice(nations))
        tension.append(0)
        resources.append(100)
        cultures.append(100)
    countryname[0] = 'mexico'

############################################################
def military(n, i):
    global resources
    global tension
    
    print(countryname[n] + ' conducts training drills with ' + countryname[i])
    resources[n] += 20 - int(tension[n] / 100)
    resources[i] += 10 - int(tension[n] / 100)
    for j in range(len(tension)):
        if j != n:
            tension[j] += 10

def economy(n, i):
    global cultures
    global resources
    global tension
    
    print(countryname[n] + ' signs a mutual economic agreement with ' + countryname[i])
    resources[n] += 20 - int(tension[n] / 100)
    resources[i] += 10 - int(tension[n] / 100)
    cultures[n] -= 10 - int(tension[n] / 100)
    cultures[i] += 10 - int(tension[n] / 100)
    for j in range(len(tension)):
        if j != n:
            tension[j] += 10
    
def culture(n, i):
    global cultures
    global resources
    global tension
    
    print(countryname[n] + ' fosters a development of culture with ' + countryname[i])
    cultures[n] += 20 - int(tension[n] / 100)
    resources[n] -= 10 - int(tension[n] / 100)
    for j in range(len(tension)):
        if j != n:
            if j == i:
                tension[j] -= 20
            else:
                tension[j] -= 10

def trade(n, i):
    global cultures
    global resources
    global tension
    
    print(countryname[n] + ' sends a trade mission to ' + countryname[i])
    resources[n] += 10 - int(tension[n] / 100)
    resources[i] += 10 - int(tension[n] / 100)
    cultures[n] += 10 - int(tension[n] / 100)
    cultures[i] += 10 - int(tension[n] / 100)
    tension[n] -= 10
    tension[i] -= 10

def war(n, i):
    global cultures
    global resources
    global tension
    
    print(countryname[n] + ' wars with ' + countryname[i])
    resources[n] -= 30 - int(tension[n] / 100)
    resources[i] -= 20 - int(tension[n] / 100)
    cultures[n] -= 20 - int(tension[n] / 100)
    cultures[i] -= 10 - int(tension[n] / 100)
    for j in range(len(tension)):
        if j == n:
            tension[j] += 40
        elif j == i:
            tension[j] += 40
        else:
            tension[j] += 20
    
############################################################

def dramatype(string):
    for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.10)

def providemap():
    print('\n')
    dramatype('El Presidente, our intelligence sources provide us the following information.')
    print('\nNATION\t\tTENSION\tRES\tCULTURE\n')
    for i in countryid:
        print(str(i) + ')' + countryname[i] + '\t\t' + str(tension[i]) + '\t' + str(resources[i]) + '\t' + str(cultures[i]))

def WORLD():
    print('\n\n(((((( WORLD ACTION ))))))\n')
    
    for i in range(1, len(countryid)):
        print('\n' + countryname[i] + ' actions:')
        for j in range(2):
            action = secure_random.choice(actionlist)
            target = secure_random.choice(countryid)
            try:
                exec(compile(action + '(' + str(i) + ', ' + str(target) + ')', '', 'exec'))
            except Exception:
                print('Shirking!')

def paranoia():
    global tension
    
    paranoiareslow = 1.3
    paranoiareshigh = 1.5
    for i in range(len(resources)):
        high = max(resources)
        if (resources[i] * paranoiareslow) < high:
            tension[i] += 10
        if (resources[i] * paranoiareshigh) < high:
            tension[i] += 20

    paranoiacullow = 1.7
    paranoiaculhigh = 2.0
    for i in range(len(cultures)):
        high = max(cultures)
        if (cultures[i] * paranoiacullow) < high:
            tension[i] += 10
        if (cultures[i] * paranoiaculhigh) < high:
            tension[i] += 20    

def trumpet():
    global trumpets
    
    trumpettension = 1.5
    low = min(tension)
    high = max(tension)
    if high / low >= trumpettension:
        trumpets += 1

def preemptive():
    if min(resources) <= 0:
        print('\n-----------------------------')
        print('\nAn unknown nation launches a pre-emptive strike against the world before it runs out of resources!\n')
        paint = [' ', ' ', '$', '$', '#', 'o']
        line = ''
        for i in range(5):
            for j in range(7):
                line += secure_random.choice(paint)
            print(line)
        gameover()
    if min(cultures) <= 0:
        print('\n-----------------------------')
        print('\nAn unknown nation loses its sanity and watches the world burn!\n')
        paint = [' ', '?', '?', '#', '@', '&']
        line = ''
        for i in range(5):
            for j in range(7):
                line += secure_random.choice(paint)
            print(line)
        gameover()

def REACHFORTHESKY(n):
    global turns
    global trumpet
    
    init(n)
    while apocalypse == 0:
        print()
        dramatype('. . .TURN ' + str(turns))
        providemap()
        for i in range(3):
            dramatype('(ACTION ' + str(i + 1) + ' out of 3) What do you focus on?')
            print('\nMilitary / Economy / Culture / Trade / War\n')
            action = input().lower()            
            try:
                print('\nWith which nation? (0-' + str(n - 1) + ')')
                target = int(input())
                try:
                    exec(compile(action + '(0, ' + str(target) + ')', '', 'exec'))
                except Exception:
                    print('You waste your turn.')
            except Exception:
                print('You should target a nation.')
        WORLD()
        preemptive()
        paranoia()
        trumpet()
        if trumpets >= 7:
            print('!!! A P O C A L Y P S E !!!')
            paint = [' ', ' ', 'X', 'x', '*', '#', '@', '&']
            line = ''
            for i in range(5):
                for j in range(7):
                    line += secure_random.choice(paint)
            gameover()
        if turns >= 10:
            victory()
        turns += 1

def victory():
    print('\n\n^_^)b____~~/| YOU WIN |\\~~____(^_^b\n')
    print('You led mexico to colonize space and survived the Mexican standoff.\n')
    print('Enjoy outer space until the next political gridlock!\n')
    paint = [' ', ' ', '*', '~']
    line = ''
    for i in range(5):
        for j in range(7):
            line += secure_random.choice(paint)
        print(line)
    print('\n\nPlay again? (ye/no)')
    if input().lower().startswith('ye'):
        main()
    else:
        sys.exit()
    
def gameover():
    print('\n\nx_x)_______| YOU LOSE |_______(x_x\n')
    print('You survived ' + str(turns) + ' rounds.\n')    
    print('Play again? (ye/no)')
    if input().lower().startswith('ye'):
        main()
    else:
        sys.exit()
        
def main():    
    print('\n\n-_-)________[MEXICO\'S STANDOFF]________(-_-\n')
    print('You, el Presidente, mishappen to become a world power capable of destroying the world many times over. You face a number of other similarly powered nations. Any one of these nations can trigger a global apocalypse. But in ten turns, space colonization will be achieved in a joint project among world powers. Can you lead your nation to survive this mexican standoff? (ye/no)\n')
    if input().lower().startswith('ye'):
        opp = 0
        op = 0
        while (opp < 2) or (opp > 99):
            print('How many participants (2-99)?')
            op = int(input())
            if 2 <= op <= 99:
                REACHFORTHESKY(op)
            else:
                print('Select a desired number of participants.')
            
            opp = op
    else:
        gameover()
        
main()
