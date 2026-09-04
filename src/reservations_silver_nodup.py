reservations_silver_cleaned_df = spark.read.table("week21_assignment.silver_schema.reservations_silver_cleaned")


reservations_silver_cleaned_df.write.mode("overwrite").saveAsTable("week21_assignment.silver_schema.reservations_silver")