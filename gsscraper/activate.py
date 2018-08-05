##import os
##import commands
##onAC_Power=True if commands.getstatus("on_ac_power")==0 else False
##os.system("echo 'hello world'")
##print onAC_Power

from google import search
        for url in search('"Breaking Code" WordPress blog', stop=20):
            print(url)
