import json

class DataLoad:
    
    def json_load_regi(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
            return [
                (
                
                    item["firstname"], 
                    item["lastname"], 
                    item["address"], 
                    item["city"], 
                    item["state"], 
                    item["zip"], 
                    item["phone"], 
                    item["ssn"], 
                    item["username"], 
                    item["password"], 
                    item["c_ps"]
                )      
            for item in data["users"]  
    ]
    
    def json_load_forget(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
            return [
                (
                
                    item["firstname"], 
                    item["lastname"], 
                    item["address"], 
                    item["city"], 
                    item["state"], 
                    item["zip"],
                    item["ssn"]
                )      
            for item in data["users"]  
    ]
 
 
    
    def json_load_login(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
            return [
                (
                
                    item["username"], 
                    item["password"] 
                )      
            for item in data["users"]  
    ] 