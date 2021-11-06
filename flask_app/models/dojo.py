from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        return connectToMySQL("dojos_and_ninjas").query_db(query)

    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL("dojos_and_ninjas").query_db(query,data)

    @classmethod
    def get_dojo_ninjas(cls,data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = %(id)s WHERE dojo_id = %(id)s"
        all_dojo_ninjas = connectToMySQL("dojos_and_ninjas").query_db(query,data)

        dojo = cls(all_dojo_ninjas[0])

        for dojo_ninjas in all_dojo_ninjas:
            ninja_data = {
                "id": dojo_ninjas["ninjas.id"],
                "first_name": dojo_ninjas["first_name"],
                "last_name": dojo_ninjas["last_name"],
                "age": dojo_ninjas["age"],
                "created_at": dojo_ninjas["ninjas.created_at"],
                "updated_at": dojo_ninjas["ninjas.updated_at"],
                "dojo_id": dojo_ninjas["dojo_id"]
            }
            dojo.ninjas.append(Ninja(ninja_data))

        return dojo