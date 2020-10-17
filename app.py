from sqlalchemy import create_engine
import psycopg2
import config
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

conn_string = os.environ['DATABASE_URL']

# rows = cur.fetchall()
# # print(rows)

# print("\nShow me the databases:\n")
# for row in rows:
#     print("   ", row[9])


@app.route("/")
@cross_origin()
def location():
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM potholes""")
    # cur.close()
    locationrows= cur.fetchall()
    # print(locationrows)
    # print(locationrows)

    # new_dict = {}
    # for row in results:
    #     new_dict[row.location] = row.category
    # print(new_dict)
    return jsonify({"location":locationrows})
        

if __name__ == '__main__':
    app.run(debug=True, port=5001)