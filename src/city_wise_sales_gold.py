

import pyspark.sql.functions as F

customers_silver_df = spark.read.table("week21_assignment.silver_schema.customers_silver")

reservations_silver_df = spark.read.table("week21_assignment.silver_schema.reservations_silver")

combined_df = customers_silver_df.join(
    reservations_silver_df,
    customers_silver_df.customer_id == reservations_silver_df.customer_id,
    "left"
)

city_wise_sales_gold_df = combined_df.groupBy("state","customer_address").agg(F.sum("total_amount").alias("total_sales")).sort("total_sales")

city_wise_sales_gold_df.write.mode("overwrite").saveAsTable("week21_assignment.gold_schema.city_wise_sales")

