import time
import random
lag_inducer=0
time.sleep(0.5)

print(f"LOADING... PLEASE WAIT")
loading_animation=[
    "[         ]",
    "[=        ]",
    "[==       ]",
    "[===      ]",
    "[ ===     ]",
    "[  ===    ]",
    "[   ===   ]",
    "[    ===  ]",
    "[     === ]",
    "[      ===]",
    "[       ==]",
    "[        =]",
    "[         ]"
]
for aaaaaaaa in range(random.randint(32,55)):
        print(f"\r{loading_animation[round(lag_inducer)%12]}", end = "")
        lag_inducer+=1
        time.sleep(random.randint(50,100)/500)
time.sleep(0.3)
print("\nLOADING FINISHED")
print(" ")


print("EVAN WANG PRESENTS...")
time.sleep(0.5)
print("""    ____  __________   ____________    ______   __________  _________  __________  ____ 
   / __ )/  _/ ____/  / ____/  _/ /   / ____/  / ____/ __ \/ ____/   |/_  __/ __ \/ __ \ 
  / __  |/ // / __   / /_   / // /   / __/    / /   / /_/ / __/ / /| | / / / / / / /_/ /
 / /_/ // // /_/ /  / __/ _/ // /___/ /___   / /___/ _, _/ /___/ ___ |/ / / /_/ / _, _/ 
/_____/___/\____/  /_/   /___/_____/_____/   \____/_/ |_/_____/_/  |_/_/  \____/_/ |_|                                                                                          
""")
y=int(input("Input the amount of megabytes you want(might be a bit off): "))
a=1
r=input("Input the file name:")
t=int(input("how much times do you want to repeat?"))
print("CREATING FILE")
for u in range(t):
    with open(f"{y} ({u+1})", "w") as f:
        for x in range(y):
            for z in range(10000):
                f.write("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
                print(f"{a}/{y} done", end="\r")
            a+=1
        print(f"{y}/{y} done")
        print(f"FILE {u+1} CREATED")
print("")
time.sleep(0.5)
if y==0 or t==0:
    print("ur supposed to put something lmao")
if y=="rickroll":
    print("""
Never gonna give you up,
Never gonna let you down,
Never gonna run around and desert you,
Never gonna make you cry,
Never gonna say goodbye,
Never gonna tell a lie and hurt you,
""")
if y=="iulg h6o7uykhjtjbuijh bnhlukjmn mgjbyinjnvf bvnjkbytughjbnhgf ghnb":
    print("""SPAM ALERT *alert sound effect*""")

time.sleep(0.5)
print("also. yes this is mine so no copying")
