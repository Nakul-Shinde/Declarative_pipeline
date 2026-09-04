import pyspark.sql.functions as F
from pyspark.sql.window import Window

reservations_df = spark.table("Week21_assignment.bronze_schema.Reservations_bronze")

reservations_df_renamed = reservations_df.select(F.col("resID").alias("res_id"),
                       F.col("resDate").alias("res_date"),
                       F.col("CustomerID").alias("customer_id"),
                       F.col("TotalAmount").alias("total_amount"),
                       F.col("Status").alias("res_status")                       
                       )

reservations_df_renamed.write.mode("overwrite").saveAsTable("Week21_assignment.silver_schema.Reservations_silver_cleaned")


w = Window.partitionBy("res_id").orderBy(F.col("res_date").desc())
reservations_dup = reservations_df_renamed.withColumn("rn",F.row_number().over(w))


record_count =reservations_df_renamed.count()
record_dup_count = reservations_dup.filter(F.col("rn") == 1).count()


duplicate_exists = record_count != record_dup_count

print(record_count)
print(record_dup_count)

dbutils.jobs.taskValues.set(key="has_duplicates", value=duplicate_exists)
