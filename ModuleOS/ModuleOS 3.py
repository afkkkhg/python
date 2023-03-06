"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""

import os
name=0
for i in os.listdir("/Scrathes/python/Downloads/target"):
    if int(i)%2==0:
        os.rename("/Scrathes/python/Downloads/target/"+i, "/Scrathes/python/Downloads/target/"+"python"+str(name))