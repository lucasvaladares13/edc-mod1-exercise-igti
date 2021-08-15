#comentario para modificar o arquivo .py
from pyspark.sql.functions import mean,max,min,col
from pyspark.sql import SparkSession

spark = (
            SparkSession.builder.appName("ExerciseSpark")
            .get0rCreate()
        )

# Ler os dados do enem 2019
enem = ( spark
        .read
        .format("csv")
        .option("header",True)
        .option("inferSchema",True)
        .option("delimiter",";")
        .load("s3://datalake-lucas-516190547158/raw-data/")
       )

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-lucas-516190547158/raw-data/")
)