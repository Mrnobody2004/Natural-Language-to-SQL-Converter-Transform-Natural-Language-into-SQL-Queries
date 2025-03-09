import torch
import sqlparse
from transformers import pipeline

gpt_model = "EleutherAI/gpt-neo-2.7B"
sql_gen = pipeline("text-generation", model=gpt_model)

def get_sql(query):
    
    try:
        res = sql_gen(query, max_length=150, num_return_sequences=1, temperature=0.7, top_p=0.9)
        return res[0]['generated_text'].strip()
    
    except Exception as err:
        
        print("Gen Error:", err)
        return None

def is_valid_sql(query):
    
    try:
        return len(sqlparse.parse(query)) > 0
    
    except Exception as err:
        print("SQL Error:", err)
        return False

def nl_to_sql(nl_query):
    
    prompt = (
        "Convert this natural language query to SQL. Use best practices. Examples:\n\n"
        "Q: Show all customers who have placed an order.\n"
        "A: SELECT * FROM customers WHERE customer_id IN (SELECT customer_id FROM orders);\n\n"
        "Q: Find total sales per product.\n"
        "A: SELECT product_id, SUM(sales) FROM orders GROUP BY product_id;\n\n"
        f"Q: {nl_query}\nA:"
    )
    sql = get_sql(prompt)
    return sqlparse.format(sql, reindent=True) if sql and is_valid_sql(sql) else "Error: Invalid SQL. Try again."

if __name__ == "__main__":
    user_query = input("Enter your query : ")
    print("SQL Query:\n", nl_to_sql(user_query))
