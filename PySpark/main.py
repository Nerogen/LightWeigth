from pyspark.sql import SparkSession


def get_product_category_pairs(products_df, categories_df):
    joined_df = products_df.join(categories_df, products_df["product_id"] == categories_df["product_id"], "left_outer")

    result_df = joined_df.select(products_df["product_name"], categories_df["category_name"])
    products_with_no_category_df = products_df.subtract(joined_df.select(products_df["product_id"]))
    products_with_no_category_names = products_with_no_category_df.select("product_name")

    return result_df, products_with_no_category_names


def main():
    spark = SparkSession.builder \
        .appName("ProductCategoryPairs") \
        .getOrCreate()

    products_data = [("1", "Product A"), ("2", "Product B"), ("3", "Product C")]
    products_schema = ["product_id", "product_name"]
    products_df = spark.createDataFrame(products_data, schema=products_schema)

    categories_data = [("1", "Category X"), ("3", "Category Y")]
    categories_schema = ["product_id", "category_name"]
    categories_df = spark.createDataFrame(categories_data, schema=categories_schema)

    result_df, products_with_no_category_names = get_product_category_pairs(products_df, categories_df)

    print("Product-Category Pairs:")
    result_df.show()

    print("Products with no Categories:")
    products_with_no_category_names.show()

    spark.stop()


if __name__ == "__main__":
    main()
