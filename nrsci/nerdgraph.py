import requests
import json

class NerdGraph:
    
    class Endpoint:
        EU = "https://api.eu.newrelic.com/graphql"
        US = "https://api.newrelic.com/graphql"
    
    __account_id = ""
    __key = ""
    __endpoint = ""
    
    def __init__(self, accid, key, endpoint = Endpoint.US):
        self.__account_id = accid
        self.__key = key
        self.__endpoint = endpoint
    
    # Code from https://newrelic.com/blog/how-to-relic/python-export-data
    def query(self, nrql_query):
        # GraphQL query to NerdGraph
        query = """
        {
            actor { account(id: %s) 
            { nrql
            (query: "%s")
            { results } } } 
        }"""  % (self.__account_id, nrql_query)

        # NerdGraph endpoint
        headers = {'API-Key': f'{self.__key}'}
        response = requests.post(self.__endpoint, headers=headers, json={"query": query})

        if response.status_code == 200:
            return response.json()["data"]["actor"]["account"]["nrql"]["results"]
        else:
            # raise an exepction with a HTTP response code, if there is an error
            raise Exception(f'Nerdgraph query failed with code {response.status_code} : {response.content}')
