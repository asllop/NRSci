from .nerdgraph import NerdGraph
from .nrql import Nrql
import pandas as pd
import datetime as dt

class Mapper:
    MAX_LIMIT = 2000
        
    __event_types = None
    __since_date = None
    __until_date = None
    __limit = MAX_LIMIT
    __select = "*"
    __ng = None

    def __init__(self, nerd_graph, *event_types):
        self.__ng = nerd_graph
        self.__event_types = list(event_types)
        self.__since_date = dt.datetime.now() - dt.timedelta(minutes = 60)
        self.__until_date = dt.datetime.now()
        
    def since(self, date):
        self.__since_date = date
        return self
    
    def until(self, date):
        self.__until_date = date
        return self
    
    def select(self, clause):
        self.__select = clause
        return self
    
    def limit(self, limit):
        if limit > self.MAX_LIMIT:
            limit = self.MAX_LIMIT
        if limit <= 0:
            limit = 1
        self.__limit = limit
        return self
    
    #TODO: create 'sample()' method, to sample events from each request using a condition
    
    def request(self):
        df = pd.DataFrame([])
        since = to_ts(self.__since_date)
        while True:
            # Generate NRQL request
            nrql = Nrql(*self.__event_types).select(self.__select).since(since).until(to_ts(self.__until_date)).limit(self.__limit).order_by("timestamp")
            # Get data and create DataFrames
            query_result = self.__ng.query(nrql.build())
            curr_df = pd.DataFrame(query_result)
            prev_df_len = len(df)
            # Generate dataframe
            if df.empty:
                df = curr_df
            else:
                df = pd.concat([df, curr_df], ignore_index=True)
                df.drop_duplicates(inplace=True, ignore_index=True)
            # Calculate next "since" value, getting the last timestamp of current dataframe. Or end if empty
            if len(df) > prev_df_len:
                since = curr_df.iloc[-1]["timestamp"]
            else:
                break
        return df

def to_ts(date):
    return int(date.timestamp())