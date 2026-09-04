import pyspark.sql.functions as F

city_state_df = spark.read.format("json").load("abfss://dbblobcontainer@dbblobstoragepractice.dfs.core.windows.net/Data/week21/source_data/city_*")

customers_silver_cleaned_df = spark.table("week21_assignment.silver_schema.customers_silver_cleaned")

#customers_silver_cleaned_df.show(5)
final_df = customers_silver_cleaned_df.join(
  city_state_df,
  customers_silver_cleaned_df.customer_address ==  city_state_df.city,
  "left"
).drop(city_state_df.city,city_state_df._corrupt_record)

final_df.write.mode("overwrite").saveAsTable("Week21_assignment.silver_schema.customers_silver")