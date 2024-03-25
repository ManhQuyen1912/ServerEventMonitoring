import configparser

filename = 'config.ini'

DefaultConfig = {
    'SYSTEM':{
        'server': 'localhost',
        'logtype': 'System',
    
    },
    'DATABASE':{
        'user': 'root',
        'password': '1234',
        'host': 'localhost',
        'database': 'hpt-winevntmnt',
        'raise_on_warnings': True
    },
    'TABLENAME':{
        'eventTable': 'events',
        'filterTable': 'filter_backup'
    },
    'COLUMNNAME':{
        'filterTable': {
            'id': 'idfilter_backup',
            'Category': 'evtCategory',
            'dateStart': 'dateStart',
            'dateEnd': 'dateEnd',
            'timeStart': 'timeStart',
            'timeEnd': 'timeEnd',
            'sourceName': 'sourceName',
            'evtID': 'evtID',
            'evtType': 'type',
            'action': 'Action'
        },
        'eventTable': {
            'id': 'idEvents',
            'Category': 'Category',
            'Time generated': '`Time generated`',
            'Source name': '`Source name`',
            'evntID': 'ID',
            'Type': 'Type',
            'Strings': 'Strings'
        }
    },
}

class Configuration:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(filename)
        # if config file is empty, write default config
        if not self.config.sections():
            self.config.read_dict(DefaultConfig)
            with open(filename, 'w') as configfile:
                self.config.write(configfile)

    def get(self, section, key):
        return self.config[section][key]

    def set(self, section, key, value):
        self.config[section][key] = value
        with open(filename, 'w') as configfile:
            self.config.write(configfile)

    def get_all(self, section):
        return self.config[section]
    

    def set_all(self, section, values):
        for key, value in values.items():
            self.config[section][key] = value
        with open(filename, 'w') as configfile:
            self.config.write(configfile)

    def get_sections(self):
        return self.config.sections()

    def get_keys(self, section):
        return self.config[section].keys()

    def get_items(self, section):
        return self.config[section].items()

    def get_sections_keys(self):
        sections = {}
        for section in self.config.sections():
            sections[section] = self.config[section].keys()
        return sections

    def get_sections_items(self):
        sections = {}
        for section in self.config.sections():
            sections[section] = self.config[section].items()
        return sections
    
# config = Configuration()
# if (bool(config.get('DATABASE', 'raise_on_warnings')) == True):
#     print("boolean works")
