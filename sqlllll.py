# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE employees (
# MAGIC     id INT, 
# MAGIC     first_name VARCHAR(50),
# MAGIC     last_name VARCHAR(50),
# MAGIC     position VARCHAR(50),
# MAGIC     salary DECIMAL(10, 2),
# MAGIC     hire_date DATE
# MAGIC );
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create a table in Databricks
# MAGIC CREATE OR REPLACE TEMPORARY VIEW employees AS
# MAGIC SELECT
# MAGIC     CAST(NULL AS INT) AS id,
# MAGIC     CAST(NULL AS STRING) AS first_name,
# MAGIC     CAST(NULL AS STRING) AS last_name,
# MAGIC     CAST(NULL AS STRING) AS position,
# MAGIC     CAST(NULL AS DECIMAL(10, 2)) AS salary,
# MAGIC     CAST(NULL AS DATE) AS hire_date
# MAGIC
