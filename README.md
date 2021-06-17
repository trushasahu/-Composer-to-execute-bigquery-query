# Composer-to-execute-bigquery-query
Scheduling to execute the Cloud Bigquery queries from Composer

### Considering that already you have created one dataset in bigquery and two tables.

i.e. one is for source which will have some data.

another one for target ,to load data into this table from source table

### Place the Execute_BQ_query_dag.py file into the dag folder.

The dag folder is created in the cloud storage during Composer instance creation.

### Click on the Airflow link i.e. under 'Airflow webserver' tab of the Composer instance.

### You will find a new dag instance(exeute_bigquery_query) for the new file placed in the cloud storage dag folder.

### Monitor the dag which will be executed at every 5 minutes.
