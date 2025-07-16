def transform(json_df:dict):

    transformed={}

    for filename, df in json_df.items():

        if filename =="sales_fact.json":
            transformed["Sales"]=df

        elif filename == "store_dimension.json":
            transformed["Stores"]=df

        elif filename == "time_dimension.json":
            transformed["Time"]=df

        elif filename =="product_dimension.json":
            transformed["Product"]=df

        elif filename == "sales_dimensions.json":

            columns=df.columns

            if "supplier_id" in columns:
                df_supplier=df[["supplier_id","supplier_name","supplier_country","contact_email","reliability_score"]].drop_duplicates()
                if "supplier_id" in df_supplier.columns:
                    transformed["Suppliers"]=df_supplier


            if "region_id" in columns:
                df_region=df[["region_id","region_name","region_country","regional_manager"]].drop_duplicates()
                if "region_id" in df_region.columns:
                    transformed["Region"]=df_region

            if "promotion_id" in columns:
                df_promotion=df[["promotion_id","promotion_name","discount_percentage","start_date","end_date"]].drop_duplicates()
                if "promotion_id" in df_promotion.columns:
                    transformed["Promotion"]=df_promotion
            
            used_cols={"supplier_id","supplier_name","supplier_country","contact_email","reliability_score",
                       "region_id","region_name","region_country","regional_manager",
                       "promotion_id","promotion_name","discount_percentage","start_date","end_date"}
            
            left_cols=[col for col in columns if col not in used_cols]

            # ============== Foreign Key Creation ==================

            fk_cols=["supplier_id","region_id","promotion_id"]
            for fk in fk_cols:
                if fk not in left_cols and fk in df.columns:
                    left_cols.append(fk)

            if left_cols:
                df_sales_dimension=df[left_cols]
                transformed["Sales_Dimension"]=df_sales_dimension

    return transformed               


