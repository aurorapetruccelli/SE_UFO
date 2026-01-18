from database.DB_connect import DBConnect
from model.sighting import Sighting
from model.state import State


class DAO:
    @staticmethod
    def get_sightings():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from sighting group by s_datetime ASC"""

        cursor.execute(query)

        for row in cursor:
            result.append(Sighting(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_states():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from state"""

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connessioni(year,shape):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT LEAST(n.state1, n.state2) AS st1,
                           GREATEST(n.state1, n.state2) AS st2, 
                           COUNT(*) as somma
                    FROM sighting s , neighbor n 
                    WHERE year(s.s_datetime) = %s
                          AND s.shape = %s
                          AND (s.state = n.state1 OR s.state = n.state2)
                    GROUP BY st1 , st2 """

        cursor.execute(query,(year,shape,))

        for row in cursor:
            result.append((row["st1"], row["st2"],row["somma"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_states_complete():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from state"""

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result