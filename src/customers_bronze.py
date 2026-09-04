
spark.sql("CREATE CATALOG if not exists Week21_assignment MANAGED LOCATION 'abfss://dbblobcontainer@dbblobstoragepractice.dfs.core.windows.net/Data/week21' ")

spark.sql("CREATE SCHEMA IF NOT EXISTS Week21_assignment.bronze_schema")

customers_schema ="CustomerID INT,CustomerName STRING,ContactNumber LONG,Email STRING,Address STRING,DateOfBirth DATE,RegistrationDate DATE,EffectiveStartDate DATE,EffectiveEndDate DATE"

customers_df =(
spark.read.format("csv").option("header","true").schema(customers_schema).load("abfss://dbblobcontainer@dbblobstoragepractice.dfs.core.windows.net/Data/week21/source_data/cust*")
)

customers_df.write.mode("overwrite").saveAsTable("Week21_assignment.bronze_schema.customers_bronze")