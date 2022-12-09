# this code cannot be run directly
# do 'source /home/fabellan/montepython_public/wrapper_wmap/bin/clik_profile.sh' from your sh shell or put it in your profile

function addvar () {
local tmp="${!1}" ;
tmp="${tmp//:${2}:/:}" ; tmp="${tmp/#${2}:/}" ; tmp="${tmp/%:${2}/}" ;
export $1="${2}:${tmp}" ;
} 

if [ -z "${PATH}" ]; then 
PATH=/home/fabellan/montepython_public/wrapper_wmap/bin
export PATH
else
addvar PATH /home/fabellan/montepython_public/wrapper_wmap/bin
fi
if [ -z "${PYTHONPATH}" ]; then 
PYTHONPATH=/home/fabellan/montepython_public/wrapper_wmap/lib/python2.7/site-packages
export PYTHONPATH
else
addvar PYTHONPATH /home/fabellan/montepython_public/wrapper_wmap/lib/python2.7/site-packages
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/home/fabellan/montepython_public/wrapper_wmap/lib
export LD_LIBRARY_PATH
else
addvar LD_LIBRARY_PATH /home/fabellan/montepython_public/wrapper_wmap/lib
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/home/fabellan/montepython_public/wrapper_wmap
export LD_LIBRARY_PATH
else
addvar LD_LIBRARY_PATH /home/fabellan/montepython_public/wrapper_wmap
fi
CLIK_DATA=/home/fabellan/montepython_public/wrapper_wmap/share/clik
export CLIK_DATA

CLIK_PLUGIN=
export CLIK_PLUGIN

