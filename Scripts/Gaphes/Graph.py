from pandas import DataFrame
from Scripts.Commands.SQLrequests import *

class Graph:
    def __init__(self, db_path):
        req = SQLrequests(db_path)
        self.list_notes = []
        for row in req.get_list():
            self.list_notes.append(row)

    def bar_chart_df(self):
        data = {'Nom':[i[1] for i in self.list_notes], 'Note':[i[2] for i in self.list_notes]}
        df = DataFrame(data, columns=['Nom', 'Note'])
        return df
    
    def pie_chart_list(self):
        reussi = 0
        non_reussi = 0
        for student in self.list_notes:
            if student[2] >= 11:
                reussi += 1
            else:
                non_reussi += 1
        return [reussi, non_reussi]