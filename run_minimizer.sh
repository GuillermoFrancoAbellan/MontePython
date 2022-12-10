RUN=chains/EMG_SPT_ACT/HiCLASS_SPT_ACT_PlanckTTTEEE_BAO_Pantheon+_221108
RUNold=chains/EMG_SPT_ACT/HiCLASS_SPT_ACT_PlanckTTTEEE_BAO_Pantheon+_221108


echo $RUN $RUNold
###STEP 1
python montepython/MontePython.py info   $RUNold --minimal --keep-non-markovian --want-covmat
OMP_NUM_THREADS=1 python montepython/MontePython.py run  -p $RUNold/*.param  -o $RUN -c $RUNold/*.covmat -b $RUNold/*.bestfit -N 10000 --update 50  --conf guillermo.conf --lklfactor 10 -f 0.5

###STEP 2
python montepython/MontePython.py info   $RUN --minimal --keep-non-markovian
OMP_NUM_THREADS=1 python montepython/MontePython.py run  -p $RUNold/*.param -o $RUN -c $RUNold/*.covmat -b $RUN/*.bestfit -N 10000 --update 50  --conf guillermo.conf --lklfactor  200 -f 0.1

###STEP 3
python montepython/MontePython.py info  $RUN --minimal --keep-non-markovian
OMP_NUM_THREADS=1 python montepython/MontePython.py run  -p $RUNold/*.param -o $RUN -c $RUNold/*.covmat -b $RUN/*.bestfit -N 10000 --update 50  --conf guillermo.conf --lklfactor 1000 -f 0.05

#TO RUN
#sudo chmod 777 run_minimizer.sh
#./run_minimizer.sh

