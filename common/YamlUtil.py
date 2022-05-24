"""
 @编写人:冯爱军
 @开发时间:2021/12/24 15:39
 @功能模块:
 @模块备注：
"""
import yaml


class YamlUtil:
    #读取yaml文件
    def read_yaml(self):
        with open(os.getcwd()+'/extract.yml',encoding="utf-8") as f:
            value=yaml.load(stream=f,loader=yaml.FullLoader)
            return value

    #写入yaml文件
    def write_yaml(self,data):
        with open(os.getcwd+'/extract.yml',encoding="utf-8") as f:
            # value=yaml.load(stream=f,Loader=yaml.FullLoader)
            yaml.dump(data,stream=f,allow_unicode=True)

    #清空yaml文件
    def write_yaml(self,data):
        with open(os.getcwd+'/extract.yml',encoding="utf-8",mode='w') as f:
            f.truncate()
