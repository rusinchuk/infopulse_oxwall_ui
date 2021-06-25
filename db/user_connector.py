import json

import pymysql.cursors

from value_objects.user_object import User


def _our_hash(password):
    d = {
        "pass": "592490bd0faa5a417a1aa7cf7aca26e8551a1b2d3238c618a9d17d1bfc4bbbef",
        "test": "a2b84e6c176c01e1aacd3312469e5ac732978f6534af33290882f5aa32be572c",
        "secret": "74210d690a28b4372ca86ff249c472975d860a537d19f0f551cd2c7d908222ea"
    }
    return d[password]


class OxwallDB:
    def __init__(self, host, user, password, db):
        # Connect to the database
        self.connection = pymysql.connect(host=host, user=user, password=password, db=db,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.connection.autocommit(True)

    def close(self):
        self.connection.close()

    def create_user(self, user):
        """ Create a new user in Oxwall db """
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `ow_base_user` (`username`, `email`, `password`, `emailVerify`, `joinIp`) " \
                  "VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (user.username, user.email, _our_hash(user.password), 1, "2130706433"))
        with self.connection.cursor() as cursor:
            sql1 = f"SELECT `id` FROM ow_base_user WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user.id = cursor.fetchone()['id']
            sql = f"""INSERT `ow_base_question_data` (`userId`, `textValue`, `questionName`)
                      VALUES ("{user.id}", "{user.real_name}", "realname")"""
            cursor.execute(sql)
            sql = f"""INSERT `ow_base_question_data`(`userId`, `intValue`, `questionName`)
                      VALUES("{user.id}", {user.gender}, "sex")"""
            cursor.execute(sql)
            sql = f"""INSERT `ow_base_question_data`(`userId`, `dateValue`, `questionName`)
                      VALUES("{user.id}", "{str(user.birthday)}", "birthdate")"""
            cursor.execute(sql)

    def delete_user(self, user):
        with self.connection.cursor() as cursor:
            sql1 = f"SELECT `id` FROM ow_base_user WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user_id = cursor.fetchone()['id']
            sql = f"""DELETE FROM `ow_base_question_data`
                       WHERE `ow_base_question_data`.`userId` = {user_id};"""
            cursor.execute(sql)
        with self.connection.cursor() as cursor:
            sql = f'''DELETE FROM `ow_base_user`
                      WHERE `ow_base_user`.`username` = "{user.username}"'''
            cursor.execute(sql)

    def get_users(self):
        with self.connection.cursor() as cursor:
            sql = f"SELECT `id`, `username`, `password`, `email` FROM `ow_base_user`"
            cursor.execute(sql)
            result = cursor.fetchall()
        # TODO: get other user property from `ow_base_question_data`
        return [User(**user) for user in result]

    def get_last_text_post(self):
        """ Get post with maximum id that is last added """
        with self.connection.cursor() as cursor:
            sql = """SELECT * FROM `ow_newsfeed_action`
                     WHERE `id`= (SELECT MAX(`id`) FROM `ow_newsfeed_action` WHERE `entityType`="user-status")
                     """
            cursor.execute(sql)
            response = cursor.fetchone()
            # print(json.loads(response["data"]))
            data = json.loads(response["data"])["status"]
        return data


if __name__ == "__main__":
    param = {"host": 'localhost',
             "user": 'root',
             "password": 'mysql',
             "db": 'oxwall1'
             }
    db = OxwallDB(**param)
    db.get_last_text_post()
