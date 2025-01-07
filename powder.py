from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from PIL import Image,ImageDraw,ImageFont
sad=['https://youtu.be/OMoU0Pfibc4?si=pjfBXfL8-gFtO5Sl','https://youtu.be/Un6uKzrWeg0?si=Auz19oAyl5jL0hfP','https://youtu.be/wuqfOlHmBdQ?si=RAe6W7C7oYY0le8d','https://youtu.be/GiCiEy1ABKM?si=iBFksrR7JAXtnKdZ','https://youtu.be/2IGDsD-dLF8?si=rwXO3xGJrKc-o37D','https://youtu.be/92J9p0VplTo?si=l-lQ69OkphzUwmEw','https://youtu.be/hMy5za-m5Ew?si=D15Grb31aLp_aAW3','https://youtu.be/tLqtnGLfm4Q?si=7kfQMpsp022YGdME','https://youtu.be/0na_SeyhSK4?si=QS5AUO_tQTfmB_v6','https://youtu.be/1TOkoLXvoaw?si=w2LyoTm9dTlixt3x','https://youtu.be/SOessajf_Ik?si=hvBBlYL_ZfOyLwfn','https://youtu.be/6FURuLYrR_Q?si=PxB9s7PYjiU-nOki','https://youtu.be/4BjGoXdpk2o?si=m8qM77aaEViio8tF','https://youtu.be/npwn6KVMtFI?si=hUE8v5KLUF_LdFil','https://youtu.be/HyLCgkQtluw?si=GAHsUmXZ5bZHBKg9','https://youtu.be/HPsxxBhv9kc?si=JIx1r-_codre1-iz','https://youtu.be/VMEXKJbsUmE?si=Xxini2IF3aD6SAXz','https://youtu.be/FIu4lel3S_o?si=ZGOFYAwlF7OToPPd','https://youtu.be/GLvgOSSC3fE?si=dOgu3cGyB5NMP02x','https://youtu.be/jHNNMj5bNQw?si=4bK10Me2Ac3mKvOT','https://youtu.be/-Hb2DeHvvEg?si=jvLylwQPYyrgi7v1','https://youtu.be/4q2zPsZU3dc?si=Cag0pw_1KrjUJLRR','https://youtu.be/P8PWN1OmZOA?si=5YTSYJN9iiiZR2zo','https://youtu.be/6YUoqa9o7y4?si=XkjV33HjiNqZDUzs','https://youtu.be/B72_HsUR0Vc?si=okSZ4HwrHsp0iwxo','https://youtu.be/KSGYVl4ZgRs?si=zjf6SqZx4E24yIrw','https://youtu.be/II4CvWvgIsI?si=JvuJ6Ldb5tFWuj0u','https://youtu.be/-Hb2DeHvvEg?si=YJ7_0dQCaGCfmhrd','https://youtu.be/2bMEe0UYa8E?si=-XYbweJfOrRZl_OA','https://youtu.be/GtPvCa3vvxA?si=8R7GNxyKLE8WoUYT']


love=['https://youtu.be/Q04pjPOAVLc?si=fIV13OLin2f4F_2K','https://youtu.be/6yH5SYpNMr4?si=L-yCSVbI9KNesGMk','https://youtu.be/qpIdoaaPa6U?si=ZirzgeWvMqv8zmbt','https://youtu.be/NDjeeJwI08Q?si=uXZgXMANZPUAhHvc','https://youtu.be/1jjDs69WWUQ?si=oLSkZdqV3EgCcEDQ','https://youtu.be/xrSZLa14haA?si=hC4rF1gbFenBodfl','https://youtu.be/5RT6QMKJTjQ?si=NMuucugkdHjMIHuf','https://youtu.be/SxTYjptEzZs?si=sBhVQTljFAxCS-Ef','https://youtu.be/8v-TWxPWIWc?si=Fpw9QP208ivo-faX','https://youtu.be/u-FaTNxrWhw?si=EuYAH7EdrnBtP9JX','https://youtu.be/fvwyPGBOEgY?si=ALLC6pj7ZjYF2KJ_','https://youtu.be/jXwg9l9D51A?si=8aSMqgVfMOuH8y03','https://youtu.be/WCTro3qabjE?si=Am1BQ0p_T2FjMFGu','https://youtu.be/Qdz5n1Xe5Qo?si=oL7QalbLDd8zFaKm','https://youtu.be/yFibazGpBiI?si=oOn-iV9eTFLCMqfC','https://youtu.be/d8IT-16kA8M?si=RNj5LjHXQzurBwZ2','https://youtu.be/RAKisl-L3CQ?si=LW3DnvhcGva7uozl','https://youtu.be/DK_UsATwoxI?si=mJuU5fDZeVgvmqgd','https://youtu.be/_Q5LH2DLd_8?si=gk9CXDzbQwxiXPtV','https://youtu.be/Etkd-07gnxM?si=aHcd9MWfo0YK4Vrl','https://youtu.be/HrnrqYxYrbk?si=IJC12P2YGpwX2ftb','https://youtu.be/VdyBtGaspss?si=ae6dlhhZgn1vUvcf','https://youtu.be/krJsyb_yf7A?si=nyOpDDCNYnRxopR_','https://youtu.be/Umqb9KENgmk?si=5LZf7o76BgTIjdRl','https://youtu.be/FJ55SHCzt88?si=Nl46x9SCD6vIVEsb','https://youtu.be/inEu2qQuGZ8?si=2DiHePwwVkX_QWOM','https://youtu.be/RHt-h2yawKo?si=FcKGY1YRtrVAbCSH','https://youtu.be/FxAG_11PzCk?si=G-FWlerVo0PREUnk','https://youtu.be/0NFxcNheoLc?si=EYiOW5ZRwx-fGPCx','https://youtu.be/l4BSJZnEX_c?si=LeQp69hjasKPcFPG']

happy=['https://youtu.be/bw7bVpI5VcM?si=QkUclqXiWIefZ7r0','https://youtu.be/Xf1922kJPfU?si=oXn5QMAhARU0vFtE','https://youtu.be/SS3lIQdKP-A?si=CZnmeGDRz-RGf7yB','https://youtu.be/WuMWwPHTSoY?si=dNljczNo-G74IBb6','https://youtu.be/n0PoVxBMUyE?si=2i2Fg7o7MhfTg6tG','https://youtu.be/IIg8H60bRJo?si=lfcoiP42DTCqlwVC','https://youtu.be/TpMSsbzvRe4?si=s-j2kAe5bCvQ1qz2','https://youtu.be/TpMSsbzvRe4?si=2rFnREjfo9o4KT0s','https://youtu.be/VzLG6OqOcn8?si=TzIsBFW5V-5DpcU7','https://youtu.be/oxO0C0Fj7bc?si=PtOmbGanaxhtEuih','https://youtu.be/M03GOY5eINg?si=AXrc07Qz27gkBXfe','https://youtu.be/zz5KauCbjPI?si=X1Vejc5awjI5t7B7','https://youtu.be/vzlXfZlH5dk?si=Ihvelac9dx0iSSV8','https://youtu.be/3rPEWcY6Oww?si=feNWNICHiIXsghEo','https://youtu.be/k09uvR5eUao?si=HUDrgn5xh6acc65G','https://youtu.be/3nA1hmKCRpE?si=gYNblTNIwJi2ef2M','https://youtu.be/bw7bVpI5VcM?si=DzFkPNA53bf3Z0r3','https://youtu.be/ypXROLupeVg?si=oacrKngVAUajoO5N','https://youtu.be/RKioDWlajvo?si=EEdt6tCFzflchf3v','https://youtu.be/f6vY6tYvKGA?si=Sqe2IbGlXsoQq9xr','https://youtu.be/asYxxtiWUyw?si=c4X7NXj4AUP15csY','https://youtu.be/CTmKrwFu7wg?si=H_8zsW514bhlxpht','https://youtu.be/05TA9jNnCdU?si=XseY921vV6znaNBw','https://youtu.be/nJZcbidTutE?si=OvocnHc-xp93umVE','https://youtu.be/nFgsBxw-zWQ?si=5t05zAk-1bW-M66g','https://youtu.be/8LZgzAZ2lpQ?si=_-1e5FB9j91btR8T','https://youtu.be/II2EO3Nw4m0?si=Y0qiLmi1ARr8fWU5','https://youtu.be/DovUEruZ2q4?si=XFJBXl0JXnXp_yku','https://youtu.be/kZqH9Kfv6BI?si=eTxaZKnYkJSCmuaz','https://youtu.be/sONw3dihCRs?si=h2PerzEWsBleyWDD']

calendar = """

"""

assignment = """

"""
flirt=['Do you have a name, or can I just call you \'mine\'?','You\'re so fine, you made me forget my pickup line','Have we met? Because you look exactly like my first love','I never believed in love at first sight, but that\'s before I saw you','Want to go outside for some fresh air? You took my breath away','I bought you a dictionary since you add so much meaning to my life','Are you a Wi-Fi signal? Because I\'m feeling a strong connection with u','I bet your birthday is October 10 because you’re a 10/10','Are you a time traveler? Because I see you in my future','Is your name Google? Because you\'re everything I\'ve been searching for','If you and I were socks, we\'d make a great pair','If I could rearrange the alphabet, I\'d put U and I together','If you were a triangle, you\'d be acute one','Are you a magician? Because when I look at you, everyone else disappears','I\'m not a photographer, but I can definitely picture us together','I\'m not an organ donor, but I\'m ready to give you my heart','On a scale of 1 to 10, you\'re a 9, and I\'m the 1 you need','Are you a camera? Because all I can do is smile when I see you','Did you just come out of an oven? Because you\'re too hot to handle','Did you do something to my eyes? I can\'t seem to take them off you','I think I saw you on Spotify, as the hottest single of the year']

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument(r"user-data-dir=C:/Users/Ruby filename/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument(r"profile-directory=Profile 4")

# Set up the ChromeDriver service
service = Service(r'C:/Users/username/Desktop/chromedriver.exe')

# Initialize the ChromeDriver with options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)

group_name = "IITM Friends meet CLUB,IITM Buddys BS DS MAY 24 Batch"
your_name = '@Powder'

while True:
    y=random.randint(0,20)

    x=random.randint(0,29)
    try:
        # Wait and look for all chats with unread message indicators (green badge)
        unread_chats = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='pane-side']//span[contains(@aria-label, 'unread message')]")))

        # If there are any unread chats
        if unread_chats:
            for chat in unread_chats:
                chat.click()  
                if messages:
                   last_message = messages[-1].text  # Get the last message text
                   print(last_message)
                   message=last_message.split()
    
                try:
                   elements = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._amig > span._ao3e")))
                   for word in elements:
                       print(word.text)
                       chat_title=word.text
                except Exception as e:
                    print("Error retrieving chat title:", e)
                    chat_title = 'randomguy'

                # Check if the chat is a group chat by comparing the title
                if  chat_title in group_name:
                    

                    # Locate recent messages in the group
                        messages = driver.find_elements(By.CSS_SELECTOR, "span.selectable-text")
                    

                        # Check if your name appears in the last message
                        if last_message==your_name:
                           print(f"You were mentioned in the group: {chat_title}")

    # Send an automated reply
                           message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                           message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                           message_box.send_keys("hello how can I help you?!" + Keys.ENTER)

                        if '/Powder command' == last_message:
                                   message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                                   message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                                   message_box.send_keys('provide command:\n study\n fun\n music\n jokes' + Keys.ENTER)
                                   pass
                       #commands for study
                                   
                        elif '/Powder command study' == last_message:
                                   message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                                   message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                                   message_box.send_keys('choose:\n calendar\n assignments_dates\n' + Keys.ENTER)
                                   pass


                        elif '/Powder command study calendar'==last_message:
                                   message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                                   message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                                   message_box.send_keys(calendar + Keys.ENTER)
                                   pass

                        elif '/Powder command study assignment dates' == last_message:
                                   message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                                   message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                                   message_box.send_keys(assignment + Keys.ENTER)
                                   pass

                        elif '/Powder command music'==last_message:
                                   message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                                   message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))

                                   message_box.send_keys('types:\n sad\n love\n happy\n' + Keys.ENTER)
                                   pass
                        #commands for music

                        elif '/Powder command music sad'==last_message:
                                   message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                                   message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))

                                   message_box.send_keys(sad[x] + Keys.ENTER)
                                   pass
                        elif '/Powder command music love'==last_message:
                                   message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                                   message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))

                                   message_box.send_keys(love[x] + Keys.ENTER)
                                   pass
                        elif '/Powder command music happy'==last_message:
                                   message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                                   message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))

                                   message_box.send_keys(happy[x] + Keys.ENTER)
                                   pass
                        #command for fun
                        elif '/Powder command fun'==last_message:
                             message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                             message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                             pass

                             message_box.send_keys('choose:\n slap\n shoot\n hug\n flirt\n troll\n' + Keys.ENTER)
                        elif '/Powder command fun flirt' in last_message:
                            new=str(last_message).split(' ')
                            message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                            message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                            message_box.send_keys(f"{new[4]} to {new[5]}: {flirt[y]}" + Keys.ENTER)
                            pass
                            
                        elif 'slap' in last_message and len(message)==4:
                        # generate image
                          img=Image.open('slap.png')

                          img=img.resize((400,400))
                          draw= ImageDraw.Draw(img)
                          font=ImageFont.truetype('arial.ttf',32)
                          text1=message[1]
                          text2=message[3]
                          draw.text((280,80),text1,font=font)
                          draw.text((120,210),text2,font=font)
                          img.save('new_slap.jpg')
                          attachment_icon = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div[2]/div/div/div/span')))
                          attachment_icon.click()

                      # Upload image
                          image_input = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
                          image_input.send_keys(r'C:\Users\Ruby Kumari\Desktop\new_slap.jpg')

                     # Send image
                          send_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]')))
                          send_button.click()
                          pass
                        elif 'hug' in last_message and len(message)==4:
                        # generate image
                          img=Image.open('hug.jpeg')

                          img=img.resize((400,400))
                          draw= ImageDraw.Draw(img)
                          font=ImageFont.truetype('arial.ttf',32)
                          text1=message[1]
                          text2=message[3]
                          draw.text((170,35),text1,font=font,fill=(0,0,0))
                          draw.text((70,280),text2,font=font,fill=(0,0,0))
                          img.save('new_hug.jpeg')
                          attachment_icon = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div[2]/div/div/div/span')))
                          attachment_icon.click()

                      # Upload image
                          image_input = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
                          image_input.send_keys(r'C:\Users\Ruby Kumari\Desktop\new_hug.jpeg')

                     # Send image
                          send_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]')))
                          send_button.click()
                        elif 'attack' in last_message and len(message)==4:
                        # generate image
                          img=Image.open('attack.jpg')

                          img=img.resize((400,400))
                          draw= ImageDraw.Draw(img)
                          font=ImageFont.truetype('arial.ttf',25)
                          text1=message[3]
                          text2=message[1]
                          draw.text((270,285),text1,font=font,fill=(0,0,0))
                          draw.text((130,200),text2,font=font,fill=(0,0,0))
                          img.save('new_attack.jpg')
                          attachment_icon = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div[2]/div/div/div/span')))
                          attachment_icon.click()

                      # Upload image
                          image_input = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
                          image_input.send_keys(r'C:\Users\Ruby Kumari\Desktop\new_attack.jpeg')

                     # Send image
                          send_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]')))
                          send_button.click()
                          

                        #elif '@Powder command fun shoot' in last_message:
                           # new=str(last_message).split(' ')
                           # message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                           # message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                           # message_box.send_keys(f"{new[4]}  {shoot}  {new[5]}" + Keys.ENTER)
                            
                        
                        elif your_name in last_message and your_name !=last_message:
                                   message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                                   message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                                   message_box.send_keys('unknown command! please provide valid request or contact developer' + Keys.ENTER)
                                   pass

                        time.sleep(2)
                            

                                     
                elif chat_title== 'randomguy':
                    # If it's a personal chat, reply immediately
                    print(f"Unread message in personal chat: {chat_title}")

                    # Send automated reply for personal chats
                    message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                    message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                    message_box.send_keys('sorry!I am yet to be tuned to take commands in personal messages' + Keys.ENTER)
                    pass

    except Exception as e:
        
        time.sleep(2)
        
