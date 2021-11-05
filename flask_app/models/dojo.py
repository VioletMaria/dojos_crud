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
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = %(id)s"
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

    @classmethod
    def get_dojos_ninjas(cls):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = dojo_id"
        all_dojos_ninjas = connectToMySQL("dojos_and_ninjas").query_db(query)

        dojos_ninjas = []

        for do_ns in all_dojos_ninjas:
            dojo_instance = Dojo(do_ns)

            ninja_data = {
                "id": do_ns["ninjas.id"],
                "first_name": do_ns["first_name"],
                "last_name": do_ns["last_name"],
                "age": do_ns["age"],
                "created_at": do_ns["ninjas.created_at"],
                "updated_at": do_ns["ninjas.updated_at"],
                "dojo_id": do_ns["dojo_id"]
            }
            dojo_instance.ninja = Ninja(ninja_data)
            dojos_ninjas.append(dojo_instance)

        return dojos_ninjas

    @classmethod
    def create_ninja(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s); SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id;"
        return connectToMySQL("dojos_and_ninjas").query_db(query,data)