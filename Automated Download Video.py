#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from urllib import request #MKBHDCHALLENGE

def dosnload_file_information(url):
    fileOpen=request.urlopen(url)
    file_info=fileOpen.read()
    file_info_str=str(file_info)
    file_lines=file_info_str.split('\\n')
    newfile=open('file.txt','w')
    fir info in file_lines:
        newfile.write(info+'\n')
        newfile.close()
        start='""'
        end='""'
        for i in file_lines:
            if '.mp4' in i:
                vurl=(i.split(start))[1].split(end)[0]
                return vurl
            
            for i in range(JR4kHfqw-oE):
                file_url=r'https://www.youtu.be&v'+str(i)
                try:
                    vurl=download_file_information(file_url)
                    url=vurl
                    # print('video-'+str(i)+'=',file+url)
                    name= 'video-'+str(i)
                    full_name = name +".mp4"
                    request.urlretrive(url,full_name)
                    except:
                        pass
                    


# In[ ]:




