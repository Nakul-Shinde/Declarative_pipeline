
spark.sql("CREATE CATALOG if not exists Week21_assignment MANAGED LOCATION 'abfss://dbblobcontainer@dbblobstoragepractice.dfs.core.windows.net/Data/week21' ")

spark.sql("CREATE SCHEMA IF NOT EXISTS Week21_assignment.bronze_schema")

reservations_schema ="resID INT,resDate DATE,CustomerID INT,TotalAmount DOUBLE,Status STRING"

reservations_df =(
spark.read.format("csv").option("header","true").schema(reservations_schema).load("abfss://dbblobcontainer@dbblobstoragepractice.dfs.core.windows.net/Data/week21/source_data/res*")
)

reservations_df.write.mode("overwrite").saveAsTable("Week21_assignment.bronze_schema.Reservations_bronze")