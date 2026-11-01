from database.DB_connect import DBConnect
from model.artista import Artista


class DAO():
    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct g.Name as genere
                    from genre g  """

        cursor.execute(query)

        for row in cursor:
            results.append(row["genere"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllNodes(genere):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct a.*
                    from genre g , artist a ,album al, track t 
                    where g.Name =%s and g.GenreId =t.GenreId 
                    and t.AlbumId =al.AlbumId and al.ArtistId  =a.ArtistId   """
            cursor.execute(query, (genere,))

            for row in cursor:
                result.append(Artista(**row))

            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getClientiPerArtista(idA, genere):
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct i.CustomerId 
                    from  album al, track t , invoice i , invoiceline inv, genre g
                    where i.InvoiceId =inv.InvoiceId and t.TrackId =inv.TrackId 
                    and t.AlbumId  =al.AlbumId and al.ArtistId =%s
                      and t.GenreId = g.GenreId
                and g.Name = %s"""

        cursor.execute(query, (idA,genere ))
        for row in cursor:
            results.append(row["CustomerId"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getPopolarita(idA,genere):
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select sum(inv.Quantity) as quantity
                    from  album al, track t ,  invoiceline inv, genre g 
                    where inv.TrackId =t.TrackId and al.ArtistId =%s
                    and t.AlbumId =al.AlbumId and t.GenreId = g.GenreId
                and g.Name = %s
                      """

        cursor.execute(query, (idA,genere))
        row = cursor.fetchone()
       # for row in cursor:
        #    results.append(row["quantity"])

        cursor.close()
        conn.close()
        # Se non ci sono vendite sum() restituisce None, quindi usiamo or 0
        if row and row["quantity"] is not None:
            return int(row["quantity"])
        return 0

       # return results