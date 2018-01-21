import pyyaml

def readcfg(configfile):
    try:
        with open(configfile, 'r', encoding='utf-8') as stream:
            config = yaml.load(stream)
            return config
    except Exception as e:
        print(e)
