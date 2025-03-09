# NL-to-SQL Converter

## Description
Convert natural language queries into SQL with AI-powered text generation and validation.

## Features
- AI-powered SQL generation using `GPT-Neo-2.7B`
- Few-shot learning for better accuracy
- SQL validation to prevent errors
- Handles errors gracefully

## Installation
```bash
pip install torch transformers sqlparse
```

## Usage
```python
python txt_to_query.py
```
Enter a natural language query, and the script will generate a valid SQL query.

## Example
**Input:**  
```
Find all orders placed by customer ID 5.
```
**Output:**  
```sql
SELECT * FROM orders WHERE customer_id = 5;
```

## License
MIT License

