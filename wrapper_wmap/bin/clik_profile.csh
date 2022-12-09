# this code cannot be run directly
# do 'source /home/fabellan/montepython_public/wrapper_wmap/bin/clik_profile.csh' from your csh shell or put it in your profile

 

if !($?PATH) then
setenv PATH /home/fabellan/montepython_public/wrapper_wmap/bin
else
set newvar=$PATH
set newvar=`echo ${newvar} | sed s@:/home/fabellan/montepython_public/wrapper_wmap/bin:@:@g`
set newvar=`echo ${newvar} | sed s@:/home/fabellan/montepython_public/wrapper_wmap/bin\$@@` 
set newvar=`echo ${newvar} | sed s@^/home/fabellan/montepython_public/wrapper_wmap/bin:@@`  
set newvar=/home/fabellan/montepython_public/wrapper_wmap/bin:${newvar}                     
setenv PATH /home/fabellan/montepython_public/wrapper_wmap/bin:${newvar} 
endif
if !($?PYTHONPATH) then
setenv PYTHONPATH /home/fabellan/montepython_public/wrapper_wmap/lib/python2.7/site-packages
else
set newvar=$PYTHONPATH
set newvar=`echo ${newvar} | sed s@:/home/fabellan/montepython_public/wrapper_wmap/lib/python2.7/site-packages:@:@g`
set newvar=`echo ${newvar} | sed s@:/home/fabellan/montepython_public/wrapper_wmap/lib/python2.7/site-packages\$@@` 
set newvar=`echo ${newvar} | sed s@^/home/fabellan/montepython_public/wrapper_wmap/lib/python2.7/site-packages:@@`  
set newvar=/home/fabellan/montepython_public/wrapper_wmap/lib/python2.7/site-packages:${newvar}                     
setenv PYTHONPATH /home/fabellan/montepython_public/wrapper_wmap/lib/python2.7/site-packages:${newvar} 
endif
if !($?LD_LIBRARY_PATH) then
setenv LD_LIBRARY_PATH /home/fabellan/montepython_public/wrapper_wmap/lib
else
set newvar=$LD_LIBRARY_PATH
set newvar=`echo ${newvar} | sed s@:/home/fabellan/montepython_public/wrapper_wmap/lib:@:@g`
set newvar=`echo ${newvar} | sed s@:/home/fabellan/montepython_public/wrapper_wmap/lib\$@@` 
set newvar=`echo ${newvar} | sed s@^/home/fabellan/montepython_public/wrapper_wmap/lib:@@`  
set newvar=/home/fabellan/montepython_public/wrapper_wmap/lib:${newvar}                     
setenv LD_LIBRARY_PATH /home/fabellan/montepython_public/wrapper_wmap/lib:${newvar} 
endif
if !($?LD_LIBRARY_PATH) then
setenv LD_LIBRARY_PATH /home/fabellan/montepython_public/wrapper_wmap
else
set newvar=$LD_LIBRARY_PATH
set newvar=`echo ${newvar} | sed s@:/home/fabellan/montepython_public/wrapper_wmap:@:@g`
set newvar=`echo ${newvar} | sed s@:/home/fabellan/montepython_public/wrapper_wmap\$@@` 
set newvar=`echo ${newvar} | sed s@^/home/fabellan/montepython_public/wrapper_wmap:@@`  
set newvar=/home/fabellan/montepython_public/wrapper_wmap:${newvar}                     
setenv LD_LIBRARY_PATH /home/fabellan/montepython_public/wrapper_wmap:${newvar} 
endif
setenv CLIK_DATA /home/fabellan/montepython_public/wrapper_wmap/share/clik

setenv CLIK_PLUGIN 

