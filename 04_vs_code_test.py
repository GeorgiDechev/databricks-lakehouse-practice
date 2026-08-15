# Databricks автоматично разпознава .py файловете като тетрадки, 
# ако имат специален коментар за разделяне на клетките:
# COMMAND ----------

print("Здравей от локалния VS Code!")

# COMMAND ----------

df = spark.sql("SELECT 'VS Code Integration Works!' as test_column")
display(df)