from database.DB_connect import DBConnect
from model.hub import Hub
from model.tratta import Tratta

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def read_hub():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM hub"
        cursor.execute(query)
        for row in cursor:
            result.append(Hub(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_spedizione(hubs_dict):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT 
                         LEAST(id_hub_origine, id_hub_destinazione) AS hub1,
                         GREATEST(id_hub_origine, id_hub_destinazione) AS hub2,
                         SUM(valore_merce)/COUNT(*) AS peso
                    FROM spedizione
                    GROUP BY LEAST(id_hub_origine, id_hub_destinazione),
                             GREATEST(id_hub_origine, id_hub_destinazione)"""
        cursor.execute(query)
        for row in cursor:
            hub1 = hubs_dict[row['hub1']]
            hub2 = hubs_dict[row['hub2']]
            peso = row['peso']
            result.append(Tratta(hub1,hub2,peso))
        cursor.close()
        conn.close()
        return result






