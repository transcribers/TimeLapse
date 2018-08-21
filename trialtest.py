import os,shutil
import subprocess

##while testing please change the path below uptil the folder 08 inside 000006


month_directory = 'D:\\000006\\08\\'
for folder_name in os.listdir(month_directory):
            print folder_name
            i=0 
            for i in range(4):
                    j = 0
                    os.chdir(os.path.join(month_directory,folder_name))
                    os.mkdir(str(i))
                    for j in range(24):
                            k = 0
                            if j>=0 and j<=9:
                                     hour = '0'+ str(j)
                            else:
                                     hour = str(j)
                                     
                            for k in range(4):
                                      if k == 0:
                                             minutes = '0' + str(k)
                                      else:
                                             minutes = str(k*15)
                                             
                                      f = os.path.join(month_directory,folder_name)+'\\'+str(i)+'-'+ hour + minutes +'.jpg'
                                      print(f)
                                      dest_folder = os.path.join(month_directory,folder_name)+'\\'+ str(i)
                                      print(dest_folder)
                                      shutil.copy(f,dest_folder)

            for m in range(4):
                    n = 0
                    current_directory = os.path.join(month_directory,folder_name)+'\\' + str(m) + '\\'
                    for file_name in os.listdir(current_directory):
                            os.rename(os.path.join(current_directory,file_name),os.path.join(current_directory,str(n)+'.jpg'))
                            n = n + 1
##                    cmd = 'ffmpeg -r 2 -f image2 -start_number 0 -i %01d.jpg -codec:v prores -profile:v 2 output'+str(m)+'.mov'
##
##                    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell = True)
##                    (output , error)= p.communicate()
##
##                    p_status = p.wait()
##                    print "Command output" + output
	
        
       
              



           
    
