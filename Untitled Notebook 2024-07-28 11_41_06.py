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
