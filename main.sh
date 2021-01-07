spark-submit\
  --master local\
  --deploy-mode client\
  Script/pi_estimator.py $1 \

res=$?
echo "Job finished with status" res$
exit $res
