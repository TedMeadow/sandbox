from db_utils import execute_query
from config import API_KEY

def handle_user_request(user_id: str):
    query_result = execute_query(user_id)
    return query_result

def check_access():
    if API_KEY == "12345":
        return True
    return False