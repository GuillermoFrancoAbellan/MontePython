RUN=chains/LCDM/LCDM_SPT_ACT_PlTT650TEEE_BAO_Pan+
RUNold=chains/LCDM/LCDM_SPT_ACT_PlTT650TEEE_BAO_Pan+

echo $RUN $RUNold 
###STEP 1
cp $RUN/*.bestfit $RUN/bf_mcmc.minimized
python montepython/MontePython.py info   $RUNold --minimal --keep-non-markovian --want-covmat
OMP_NUM_THREADS=8 python montepython/MontePython.py run  -p $RUN/*.param  -o $RUN -c $RUNold/*.covmat -b $RUNold/*.bestfit -N 10000 --update 50  --conf guillermo.conf --lklfactor 10 -f 0.5

###STEP 2
python montepython/MontePython.py info   $RUN --minimal --keep-non-markovian
OMP_NUM_THREADS=8 python montepython/MontePython.py run  -p $RUN/*.param -o $RUN -c $RUNold/*.covmat -b $RUN/*.bestfit -N 10000 --update 50  --conf guillermo.conf --lklfactor  200 -f 0.1

###STEP 3
python montepython/MontePython.py info  $RUN --minimal --keep-non-markovian
OMP_NUM_THREADS=8 python montepython/MontePython.py run  -p $RUN/*.param -o $RUN -c $RUNold/*.covmat -b $RUN/*.bestfit -N 10000 --update 50  --conf guillermo.conf --lklfactor 1000 -f 0.05
python montepython/MontePython.py info  $RUN --minimal --keep-non-markovian

mv $RUN/*.bestfit $RUN/bf_nils.minimized
rm $RUN/*_10000_*

python montepython/MontePython.py info  $RUN --minimal --keep-non-markovian

#TO RUN
#sudo chmod 777 run_minimizer.sh
#./run_minimizer.sh

#TO CHECK THAT THE MINIMIZATION HAS WORKED WELL, compare the total chi2_min (and per experiment) obtained from the mcmc and from this method, the latter should be clearly smaller

#python montepython/MontePython.py run  -p $RUN/*.param -o chains/test_run1 -b $RUN/bf_mcmc.minimized -f 0 --conf guillermo.conf --display-each-chi2
#python montepython/MontePython.py run  -p $RUN/*.param -o chains/test_run2 -b $RUN/bf_nils.minimized -f 0 --conf guillermo.conf --display-each-chi2
#rm -r chains/test_run1
#rm -r chains/test_run2


#NOTE: Ideally, RUNold and RUN should correspond to different folders, where the first stores the original long chain files and the latter stores the short chain files used for the 
#minimisation. In practice, it doesn't matter if RUNold=RUN, even if this implies that info will analyze both long and short chains. Indeed, in steps 2 and 3 we do info without 
# --want-covmat  (and the chains are too short to be affected by the update method in the runs), so we always keep the same covmat produced in step 1. When doing info, the code
# searches for the point corresponding to the maximum likelihood (in all the chains, but the short chains are the relevant in this case), and this works even with the --minimal flag.
#However, it's good to remove the short chains once the minimisation is completed, otherwise analysing both short and long chains can lead to weird R-1, and lead to problems if we want
# to recompute the posteriors or the covmat.
