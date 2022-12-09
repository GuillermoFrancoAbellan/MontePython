# this code cannot be run directly
# do 'source /rwthfs/rz/cluster/home/ns302248/montepython_p18sys/montepython/wrapper_wmap/bin/clik_profile.sh' from your sh shell or put it in your profile

# function addvar () {
# local tmp="${!1}" ;
# tmp="${tmp//:${2}:/:}" ; tmp="${tmp/#${2}:/}" ; tmp="${tmp/%:${2}/}" ;
# export $1="${2}:${tmp}" ;
# } 

if [ -z "${PATH}" ]; then 
PATH=/rwthfs/rz/cluster/home/ns302248/montepython_p18sys/montepython/wrapper_wmap/bin
else
PATH=$PATH:/rwthfs/rz/cluster/home/ns302248/montepython_p18sys/montepython/wrapper_wmap/bin
fi
export PATH
if [ -z "${PYTHONPATH}" ]; then 
PYTHONPATH=/rwthfs/rz/cluster/home/ns302248/montepython_p18sys/montepython/wrapper_wmap/lib/python2.7/site-packages
export PYTHONPATH
else
PYTHONPATH=$PYTHONPATH:/rwthfs/rz/cluster/home/ns302248/montepython_p18sys/montepython/wrapper_wmap/lib/python2.7/site-packages
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/lib
export LD_LIBRARY_PATH
else
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/lib
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/rwthfs/rz/cluster/home/ns302248/montepython_p18sys/montepython/wrapper_wmap/lib
export LD_LIBRARY_PATH
else
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/rwthfs/rz/cluster/home/ns302248/montepython_p18sys/montepython/wrapper_wmap/lib
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/lib64
export LD_LIBRARY_PATH
else
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/lib64
fi
if [ -z "$CLIK_DATA" ]; then
CLIK_DATA=/rwthfs/rz/cluster/home/ns302248/montepython_p18sys/montepython/wrapper_wmap/share/clik
else
CLIK_DATA=$CLIK_DATA:/rwthfs/rz/cluster/home/ns302248/montepython_p18sys/montepython/wrapper_wmap/share/clik
fi
export CLIK_DATA

