import pyspark.sql.functions as F

customers_df = spark.table("Week21_assignment.bronze_schema.customers_bronze")

customers_df_filtered = customers_df.filter(F.col("EffectiveEndDate").isNull())


customers_df_renamed = customers_df_filtered.select(
                       F.col("CustomerID").alias("customer_id"),
                       F.col("CustomerName").alias("customer_name"),
                       F.col("ContactNumber").alias("contact_number"),
                       F.col("Email").alias("customer_email"),
                       F.col("Address").alias("customer_address"),
                       F.col("DateOfBirth").alias("customer_dob"),
                       F.col("RegistrationDate").alias("registration_date"),
                       F.col("EffectiveStartDate").alias("effective_start_date"),
                       F.col("EffectiveEndDate").alias("effective_end_date"),

                       )

customers_df_renamed.write.mode("overwrite").saveAsTable("Week21_assignment.silver_schema.customers_silver_cleaned")

