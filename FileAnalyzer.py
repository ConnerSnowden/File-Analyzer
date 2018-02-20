
import sys
import os
import time

print  """
     _______________________________
   < Ethical Hackers Vs Noobs Team >
     -------------------------------
       \                                                          
        \                                                         
         \                                                        
                                      .::!!!!!!!:.                
     .!!!!!:.                        .:!!!!!!!!!!!!               
     ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$               
         :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P               
         $$$$$##WX!:      .<!!!!UW$$$     $$$$$$$$#               
         $$$$    $$UX   :!!UW$$$$$$$*     *$$$$$*                 
         $$$B    $$\     $$$$$$$$$$$$     d$$R                    
            *$bd$$$$      '*$$$$$$$$$$$o+#**                      
                                                                  
     [*] +--------------------------------------------+"
     [*] |           Ethical Hackers Vs Noobs         |"
     [*] |           #Conner Snowden 0x00             |"
     [*] |               File Analyzer 1.0            |"
     [*] | https://www.facebook.com/conner.snowden.50 |" """


print ("""
    1. \x1b[1;32;40m Display and monitor your file \x1b[0m """)

choice = input("""    
    \x1b[1;33;40m Enter your choice: \x1b[0m """)
		
if choice == 1:
   file =raw_input("\x1b[1;32;40m {*}Enter your file path  : \x1b[0m ")

   file_size = os.path.getsize(file)

   print  "\t\t\t \033[1m \033[93m Your total File size is ",file_size

   size = file_size 

while file_size == size:

    print('\x1b[0;32;70m' "{*}--No suspicious activities has been detected on " + time.ctime() + '\x1b[0m')
    time.sleep(1)
    file_size = os.path.getsize(file)

else:

	print('\x1b[1;32;41m' + "{*}-----Warning !!! your file has been modified on " + time.ctime() + '\x1b[0m')
