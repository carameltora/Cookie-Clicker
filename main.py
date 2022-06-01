# MODULES
from replit import db
from getkey import getkey
from guide import guide_txt
from news import *
import os
import timeit
import random

# FUNCTIONS
def rgb(r,g,b):
  return f"\033[38;2;{r};{g};{b}m"

def clear():
  os.system('clear')

def redeem_code():
  redeemcode1 = "COOKIES4LIFE"
  redeemcode2 = "TASTYDOUGH"
  redeemcode3 = "COOKIEMONSTA"

def sort_shop():
  for item in shop:
    if cookies < item.cost:
      break

  index = shop.index(item)

  if index <= 4:
    return shop[:5]

  elif cookies >= 1000000000000:
    return shop[-5:]

  return shop[index-3:index+2]

# STYLES
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible = "\033[08m"
reverse = "\033[07m"
reset = "\033[0m"

light_blue = rgb(82,180,255)
light_brown = rgb(190,140,100)
brown = rgb(170,120,80)
golden = rgb(219,180,107)

# STATS
username = os.environ['REPL_OWNER']

upgrades = []
cookies = 0

reset_cps = True # flag for CPS

headline = f"Welcome back, {username}!"

golden_cookie = 0
golden_cookie_content = ""

if username == 'five-nine':
  print("Login to Replit to play this game.")

  exit()

if username not in db:
  db[username] = cookies

else:
  cookies = db[username]

#SHOP
class Upgrade:
  def __init__(self, name, cost, cps, cpc):
    self.name = name

    self.cost = cost
    
    self.cps = cps # cookies per second
    self.cpc = cpc # cookies per click

  def update_cost(self):
    self.cost += int(self.cost/6)

Cursor = Upgrade('Cursor', 15, 0.1, 0)
Grandma = Upgrade('Grandma', 100, 1, 0)
Fingers = Upgrade('Fingers', 400, 1, 1)
Farm = Upgrade('Farm', 1100, 8, 1)
Mine = Upgrade('Mine', 12000, 47, 1)
Factory = Upgrade('Factory', 130000, 260, 2)
Bank = Upgrade('Bank', 1400000, 1400, 0)
Temple = Upgrade('Temple', 2000000, 7800, 1)
Wizard_Tower = Upgrade('Wizard Tower', 330000000, 44000, 4)
Shipment = Upgrade('Shipment', 5100000000, 260000, 0)
Alchemy_Lab = Upgrade('Alchemy Lab', 75000000000, 1600000, 3)
Portal = Upgrade('Portal', 1000000000000, 10000000, 6)
Time_Machine = Upgrade('Time Machine', 14000000000000, 65000000, 6)
Cookie_Monster = Upgrade('Cookie Monster', 180000, 350, 70)
Blaster = Upgrade('Blaster', 20000000, 0, 3500)

shop = [Cursor,Grandma,Fingers,Farm,Mine,Factory,Bank,Temple,Wizard_Tower,Shipment,Alchemy_Lab,Portal,Time_Machine,Cookie_Monster,Blaster]

print(f"""\n{light_brown}░█████╗░░█████╗░░█████╗░██╗░░██╗██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║██╔════╝
██║░░╚═╝██║░░██║██║░░██║█████═╝░██║█████╗░░
██║░░██╗██║░░██║██║░░██║██╔═██╗░██║██╔══╝░░
╚█████╔╝╚█████╔╝╚█████╔╝██║░╚██╗██║███████╗
░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝

{brown}░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝{reset}
      
Made by {light_blue}@UltimateCoder40{reset}, {light_blue}@CodingElf66{reset}, {light_blue}@PhantomPython{reset}, {light_blue}@rickysong{reset}, and {light_blue}@SilentFoxy78{reset}, and {light_blue}@JakeHu2020\n""")

print("Press [ENTER] to start the game\nPress [G] for guide\n")

keyInput = getkey()

clear()

if keyInput.lower() == 'g':
  print(guide_txt)

  input('\nPress [ENTER] to continue')

clear()

# GAME
while True: # loop forever
  shop_list = sort_shop()

  news_change = random.randint(1,10)
  
  if news_change == 1:
    if cookies < 100:
      headline = random.choice(starter_news)

    elif cookies >= 100 and cookies < 1000:
      headline = random.choice(intermediate_news)

    elif cookies >= 1000 and cookies < 15000:
      headline = random.choice(pro_news)

    elif cookies >= 15000 and cookies < 200000:
      headline = random.choice(legendary_news)

    else:
      headline = random.choice(mythical_news)
  
  if reset_cps:
    cps_start = timeit.default_timer()
  
  cps = 0
  cpc = 1
  
  items = len(upgrades)
  
  for upgrade in upgrades:
    cps += upgrade.cps
  
  for upgrade in upgrades:
    cpc += upgrade.cpc

  cps = round(cps,1)
  cpc = round(cpc,1)

  cookies = round(cookies,2)

  print(f"""\n                {bold}{light_brown}Cookie {brown}Clicker 🍪{reset}                 {bold}Stats 📈{reset}
    ───────────────────────────────────────────────────────────────────────────────
           {bold}{cookies} 🍪{reset}{(36-len(str(cookies)))*' '}{bold}CPS:{reset} {cps} (cookies per second)
                                                  {bold}CPC:{reset} {cpc} (cookies per click)
                                                  {bold}Items:{reset} {items}
          
          
                    {bold}Shop 🛒{reset}                       {bold}News 📰{reset}
    ───────────────────────────────────────────────────────────────────────────────
          {bold}[1]{reset} {shop_list[0].name}: {shop_list[0].cost} 🍪{(23-len(shop_list[0].name)-len(str(shop_list[0].cost)))*' '}{bold}{headline[:35]}{reset}        
          {bold}[2]{reset} {shop_list[1].name}: {shop_list[1].cost} 🍪{(23-len(shop_list[1].name)-len(str(shop_list[1].cost)))*' '}{bold}{headline[35:]}{reset}
          {bold}[3]{reset} {shop_list[2].name}: {shop_list[2].cost} 🍪
          {bold}[4]{reset} {shop_list[3].name}: {shop_list[3].cost} 🍪{(23-len(shop_list[3].name)-len(str(shop_list[3].cost)))*' '}{golden_cookie_content}
          {bold}[5]{reset} {shop_list[4].name}: {shop_list[4].cost} 🍪

        
                                    {bold}Leaderboard 🏆{reset}
    ───────────────────────────────────────────────────────────────────────────────
          🥇 {bold}Martinez10:{reset} 4.3235e+33 🍪
          🥈 {bold}twinnturbo:{reset} 3.62265e+22 🍪
          🥉 {bold}GreenHexagon:{reset} 2.56e+22 🍪

        
                        {bold}Make sure to press [S] to save your progress!{reset}""")

  
  start = timeit.default_timer()
    
  click = getkey()
  
  end = timeit.default_timer()
   
  if click == "\n" and end - start > 0.04: # prevent spam
    cookies += cpc
        
    for upgrade in upgrades:
      cookies += upgrade.cpc

  elif click in ['1','2','3','4','5']:
    index = int(click)-1

    upgrade = shop_list[index]

    if cookies >= upgrade.cost:
      cookies -= upgrade.cost
      
      upgrades.append(upgrade)

      upgrade.update_cost()

  elif click.lower() == 'g' and golden_cookie == 1 and end - start > 0.04: # prevent spam
    amount = int(cookies/(4/3))

    cookies += amount

  elif click.lower() == 's':
    db[username] = cookies

  cps_end = timeit.default_timer()

  if cps_end - cps_start >= 1:
    times = cps_end - cps_start

    cookies += times * cps

    reset_cps = True

  else:
    reset_cps = False

  golden_cookie = random.randint(1,100)

  if golden_cookie == 1:
    golden_cookie_content = f"{golden}[G] GOLDEN COOKIE!!!{reset}"

  else:
    golden_cookie_content = ""

  if '.0' == str(cookies)[-2:]:
    cookies = int(str(cookies)[:-2])

  clear()
