class Nrql:
    __from = []
    __select = "*"
    __where = ""
    __since = ""
    __until = ""
    __limit = ""
    __order_by = ""
    __order_dir = "ASC"
    
    def __init__(self, *from_clause):
        self.__from = list(from_clause)
    
    def select(self, clause):
        self.__select = clause
        return self
    
    def where(self, clause):
        self.__where = clause
        return self
    
    def since(self, clause):
        self.__since = clause
        return self
    
    def until(self, clause):
        self.__until = clause
        return self
    
    def limit(self, clause):
        self.__limit = clause
        return self
    
    def order_by(self, clause):
        self.__order_by = clause
        return self
    
    def asc(self):
        self.__order_dir = "ASC"
        return self
    
    def desc(self):
        self.__order_dir = "DESC"
        return self
    
    def build(self):
        if len(self.__from) > 0:
            query = "SELECT " + self.__select + " FROM " + ','.join(self.__from)
            if self.__where:
                query += " WHERE " + self.__where
            if self.__since:
                query += " SINCE " + str(self.__since)
            if self.__until:
                query += " UNTIL " + str(self.__until)
            if self.__limit:
                query += " LIMIT " + str(self.__limit)
            if self.__order_by:
                query += " ORDER BY " + self.__order_by + " " + self.__order_dir
            return query
        else:
            raise Exception("Clause 'from' not specified")