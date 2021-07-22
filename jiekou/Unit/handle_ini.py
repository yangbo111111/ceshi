import os
import configparser

base_path = os.getcwd()
# sys.path.append(base_path)


class HandleInit:

    def load_ini(self):
        file_path = base_path + "/Config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    def get_value(self, key, node=None):
        '''
        获取ini里面的value
        '''
        cf = self.load_ini()
        if node == None:
            node = 'server'
            try:
                data = cf.get(node, key)
            except Exception:
                print("没有获取到值")
                data = None
        else:
            try:
                data = int(cf.get(node, key))
            except Exception:
                print("没有获取到值")
                data = None
        return data

hanle_ini = HandleInit()
if __name__ == '__main__':
    ha = HandleInit().get_value("is_run")

