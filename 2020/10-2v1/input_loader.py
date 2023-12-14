class input_loader:
    @staticmethod
    def get_input_as_list(file_name):
        f = open(file_name, "r")
        res = f.read().splitlines()
        f.close()
        return res

    @staticmethod
    def get_input_as_string(file_name):
        f = open(file_name, "r")
        res = f.read()
        f.close()
        return res

    @staticmethod
    def get_input_as_int_list(file_name):
        f = open(file_name, "r")
        res = f.read().splitlines()
        res = [int(s) for s in res]
        f.close()
        return res
