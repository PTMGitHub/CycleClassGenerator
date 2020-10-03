from psycopg2 import connect
from flask import render_template 
from flask import Flask
from random import randint

t_host = "db"
t_port = "5432" # default postgres port
t_dbname = "D_db"
t_user = "postgres"
t_pw = "root"
db_conn = connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()

app = Flask(__name__)
@app.route('/')
@app.route('/index', methods=['GET'])
def index():

    def query_track_designs_table(desired_aim):
        sql_query = "SELECT * FROM track_designs WHERE aim LIKE '%" + desired_aim + "%';"
        db_cursor.execute(sql_query)

        return db_cursor.fetchall()
        
    def get_one_track(desired_aim):
        returned_tracks = query_track_designs_table(desired_aim)
        num_of_returned_tracks = len(returned_tracks)
        random_index_to_use = randint(0,num_of_returned_tracks-1)

        return returned_tracks[random_index_to_use]

    def get_three_tracks(desired_aim):
        returned_tracks = query_track_designs_table(desired_aim)
        num_of_returned_tracks = len(returned_tracks)
   
        three_diff_indexes = False
        while three_diff_indexes == False:
            first_random_index = randint(0,num_of_returned_tracks-1)
            second_random_index = randint(0,num_of_returned_tracks-1)
            third_random_index = randint(0,num_of_returned_tracks-1)


            if (first_random_index != second_random_index) and (first_random_index != third_random_index) and (second_random_index != third_random_index): 

                three_diff_indexes = True

                
        three_track_list = []

        three_track_list.append(returned_tracks[first_random_index])      
        three_track_list.append(returned_tracks[second_random_index])  
        three_track_list.append(returned_tracks[third_random_index])    
          
        return three_track_list 

    warm_up = get_one_track('warm up')
    three_climbs = get_three_tracks('climb')
    three_endurances = get_three_tracks('endurance')
    three_hovers = get_three_tracks('hover')
    three_sprints = get_three_tracks('sprint')
    recovery = get_one_track('recovery')
    
    return render_template("index.html", warm_up=warm_up, recovery=recovery, three_climbs=three_climbs, three_endurances=three_endurances, three_hovers=three_hovers, three_sprints=three_sprints)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

db_conn.close()