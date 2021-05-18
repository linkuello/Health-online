class Mydb2Router:
    def db_for_read(model, **hint):
        if model._meta.app_label == 'mobilemarket':
            return 'mydb2'
        return None

    def db_for_write(model, **hint):
        if model._meta.app_label == 'mobilemarket':
            return 'mydb2'
        return None

    def allow_relation(obj1, obj2, **hint):
        if obj1._meta.app_label == 'mobilemarket' or obj2._meta.app_label == 'mobilemarket':
            return True
        return None

    def allow_migrate(db, app_label, model_name=None, **hint):
        if app_label == 'mobilemarket':
            return db == 'mydb2'  # If db is mydb2, i will return true.
        elif db == 'mydb2':
            return False  # IF the request is not db2 and it want migrate to db2, this will stop it.
        return None


class Mydb3Router:
    def db_for_read(model, **hint):
        if model._meta.app_label == 'mysite':
            return 'mydb3'
        return None

    def db_for_write(model, **hint):
        if model._meta.app_label == 'mysite':
            return 'mydb3'
        return None

    def allow_relation(obj1, obj2, **hint):
        if obj1._meta.app_label == 'mysite' or obj2._meta.app_label == 'mysite':
            return True
        return None

    def allow_migrate(db, app_label, model_name=None, **hint):
        if app_label == 'mysite':
            return db == 'mydb3'  # If db is mydb3, i will return true.
        elif db == 'mydb3':
            return False  # IF the request is not db3 and it want migrate to db3, this will stop it.
        return None


class BoardRouter:
    def db_for_read(model, **hint):
        if model._meta.app_label == 'board':
            return 'mydb_board'
        return None

    def db_for_write(model, **hint):
        if model._meta.app_label == 'board':
            return 'mydb_board'
        return None

    def allow_relation(obj1, obj2, **hint):
        if obj1._meta.app_label == 'board' or obj2._meta.app_label == 'board':
            return True
        return None

    def allow_migrate(db, app_label, model_name=None, **hint):
        if app_label == 'board':
            return db == 'mydb_board'
        elif db == 'mydb_board':
            return False
        return None
