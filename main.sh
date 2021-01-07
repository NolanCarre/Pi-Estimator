spark-submit\
  --master local\
  --deploy-mode client\
  pi_estimator.py $1 \

res=$?
echo "Job finished with status" res$
exit $res
