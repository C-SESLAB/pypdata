
import requests
from .Dataset import Dataset

class Connected():
    def __init__(self,key) -> None:
        self.key = {"access_token": key}
        self.URL = "https://api.pyphasorusach.dispersiondigital.cl/dev/phasors"
        pass

    def get_all_phasors(self):
        return requests.get(url=self.URL, params= self.key)

    def get_pmu_names(self):
        response = []
        r =  requests.get(url=self.URL, params= self.key)
        data = r.json()
        b = data[0]
        json_object = json.dumps(b, indent = 4) 
        a = data[0]['PMU']
        print(json_object)
        for  x in  a:
            print(x["nombre"])
        
    def info(self):
        response = []
        r =  requests.get(url=self.URL, params= self.key)
        data = r.json()
        b = data[0]
        for x in range(len(data)):
            response.append({"id":data[x]['id'], "nombre":data[x]['nombre']})

        return response
    
    def get_dataset(self,id):
        response = []
        r =  requests.get(url=self.URL+"/"+id, params= self.key)
        data = r.json()
        jsonDataset = Dataset(**data)
        return jsonDataset
        