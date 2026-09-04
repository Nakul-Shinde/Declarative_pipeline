import pyspark.sql.functions as F
from pyspark.sql.window import Window

reservations_silver_cleaned_df = spark.read.table("week21_assignment.silver_schema.reservations_silver_cleaned")

w = Window.partitionBy(F.col("res_id")).orderBy(F.col("res_date").desc())

reservations_rn = reservations_silver_cleaned_df.withColumn("rn",F.row_number().over(w))

reservations_silver_deduped_df = reservations_rn.filter(F.col("rn")==1).drop("rn")

#reservations_rn.filter(F.col("res_id")> 399).show()
reservations_silver_deduped_df.write.mode("overwrite").saveAsTable("week21_assignment.silver_schema.reservations_silver")