from nl2sql import nl_to_sql
from main import execute_query

def execute_nl_query(nl_query):
    sql_query = nl_to_sql(nl_query)
    
    print("Сгенерированный SQL:", sql_query)
    execute_query(sql_query)
# example
# nl_query = "Show all students who have a GPA greater than 3.5"
# execute_nl_query(nl_query)