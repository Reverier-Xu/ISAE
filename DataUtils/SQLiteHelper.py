import sqlite3


# 连接数据库类
class Connect(object):
    # 构造函数
    def __init__(self, dbName=':memory:'):
        self.dbName = dbName
        self.tableObj = {}
        self.conn = sqlite3.connect(dbName)

    # 获取数据库名称
    def getDBName(self):
        return self.dbName

    # 获取 sqlite3 connection
    def getConn(self):
        return self.conn

    # 获取表类
    def table(self, tabl):
        if tabl not in self.tableObj.keys():
            self.tableObj[tabl] = Table()
            self.tableObj[tabl].setConnection(self.getConn())
            self.tableObj[tabl].setTable(tabl)
        return self.tableObj[tabl]

    # 执行SQL语句
    def query(self, sql, commit=False):
        cursor = self.getConn().execute(sql)
        if commit:
            self.getConn().commit()
        return cursor

    # 关闭数据库连接
    def close(self):
        self.getConn().close()


# 表操作类
class Table(object):
    # 获取当前表名
    def getTableName(self):
        return self.tab

    # 设置 sqlite3 connection
    def setConnection(self, conn):
        self.conn = conn

    # 获取 sqlite3 connection
    def getConnection(self):
        return self.conn

    # 设置表名
    def setTable(self, tab):
        self.tab = tab
        self.tableField = self.__getDefaultField()

    # 检查表名是否存在
    def tableExists(self):
        isExist = False
        try:
            self.getConnection().execute("SELECT * FROM " + self.getTableName())
            isExist = True
        except sqlite3.OperationalError:
            isExist = False
        return isExist

    # 创建表
    def create(self, fields, insert=None):
        if (not self.tableExists()):
            QUERY = "CREATE TABLE " + self.getTableName() + " ("
            fields = self.__dataProcess(fields, isCheckKey=False)
            if isinstance(fields, dict) and len(fields) > 0:
                keys = list(fields.keys())
                values = list(fields.values())
                for index in range(len(fields)):
                    QUERY += keys[index] + " " + values[index]
                    if index < len(fields) - 1:
                        QUERY += " , "
                    else:
                        QUERY += ");"
            else:
                return False
            self.__query(QUERY, commit=True)
            self.tableField = self.__getDefaultField()
            if insert != None:
                self.data(insert).add()
            return True
        else:
            return False

    # 添加数据
    def data(self, datas):
        if isinstance(datas, (tuple, list)) and len(datas) > 0:
            self.__delattr('sql_datas')
            for item in datas:
                self.data(item)
        elif isinstance(datas, dict) and len(datas) > 0:
            datas = self.__dataProcess(datas)
            keys = list(datas.keys())
            values = list(datas.values())
            sql_key = " ( "
            sql_value = " ( "
            if hasattr(self, 'sql_datas') == False:
                self.sql_datas = []
            for index in range(len(datas)):
                sql_key += keys[index] + " "
                if isinstance(values[index], str):
                    sql_value += "'" + values[index] + "' "
                else:
                    sql_value += str(values[index]) + " "
                if index < len(datas) - 1:
                    sql_key += ", "
                    sql_value += ", "
            self.sql_datas.append(sql_key + ") VALUES " + sql_value + ") ")
        return self

    # 执行添加数据（需要添加数据的字典）
    def add(self, data=None):
        if data != None:
            self.__delattr('sql_datas')
            self.sql_datas = []
            self.data(data)
        if hasattr(self, 'sql_datas') and len(self.sql_datas) > 0:
            QUERYS = self.__getAddDataSql(self.getTableName(), self.sql_datas)
            if isinstance(QUERYS, str):
                self.getConnection().execute(QUERYS)
                self.__query(QUERYS)
            elif isinstance(QUERYS, (list, tuple)):
                for QUERY in QUERYS:
                    self.getConnection().execute(QUERY)
            self.getConnection().commit()
        self.__reset()

    # 查询操作
    def where(self, params, condition='and'):
        if isinstance(params, str):
            self.sql_where = params
        elif isinstance(params, dict):
            params = self.__dataProcess(params)
            self.sql_where = ' '
            keys = list(params.keys())
            values = list(params.values())
            for index in range(len(params)):
                self.sql_where += str(keys[index]) + " "
                if isinstance(values[index], str):
                    self.sql_where += "= '" + values[index] + "' "
                elif isinstance(values[index], list) and len(values[index]) > 1:
                    self.sql_where += values[index][0]
                    if isinstance(values[index][1], str):
                        self.sql_where += " '" + values[index][1] + "' "
                    else:
                        self.sql_where += " " + str(values[index][1]) + " "
                else:
                    self.sql_where += "= " + str(values[index]) + " "
                if index < len(keys) - 1:
                    if isinstance(condition, str):
                        self.sql_where += condition + " "
                    elif isinstance(condition, list) and len(condition) >= len(keys) - 1:
                        self.sql_where += condition[index] + " "
        return self

    # 指定返回字段
    def field(self, *fields):
        if isinstance(fields, str) and self.__fieldExists(fields):
            self.sql_field = fields
        elif isinstance(fields, (list, tuple)) and len(fields) > 0:
            self.sql_field = " "
            fields = list(fields)
            retList = []
            for index in range(len(fields)):
                if self.__fieldExists(fields[index]):
                    retList.append(fields[index])
            fields = retList
            if len(fields) > 0:
                for index in range(len(fields)):
                    self.sql_field += fields[index]
                    if index < len(fields) - 1:
                        self.sql_field += ' , '
            else:
                self.sql_field = " * "
        else:
            self.sql_field = " * "
        return self

    # 排序操作
    def order(self, orders):
        if isinstance(orders, str) and self.__fieldExists(orders):
            self.sql_order = orders
        elif isinstance(orders, list) and len(orders) > 0:
            self.sql_order = " "
            for index in orders:
                if self.__fieldExists(orders[index]):
                    self.sql_order += orders[index]
                    if index < len(orders) - 1:
                        self.sql_order += ' , '
        elif isinstance(orders, dict) and len(orders) > 0:
            self.sql_order = " "
            keys = list(orders.keys())
            values = list(orders.values())
            for index in range(len(orders)):
                if self.__fieldExists(keys[index]):
                    self.sql_order += keys[index] + ' ' + values[index] + ' '
                    if index < len(orders) - 1:
                        self.sql_order += ', '
        else:
            self.__delattr('sql_order')
        return self

    # 执行查询操作（结果返回个数 - 默认1个）
    def find(self, count=1, page=0):
        cursor = self.__query(self.__getFindSql(self.getTableName(), limit=count, page=page))
        return self.__cursor2dict(cursor.description, cursor.fetchall())

    # 执行查询操作(不建议使用) -> 返回全部结果
    def findAll(self):
        return self.find(0)

    # 统计查询 Count
    def count(self, field='*'):
        if self.__fieldExists(field):
            self.sql_field = " COUNT(" + field + ") "
            cursor = self.__query(self.__getFindSql(self.getTableName()))
            return cursor.fetchone()[0]
        else:
            return 0

    # 统计查询 Max
    def max(self, field):
        if self.__fieldExists(field):
            self.sql_field = " MAX(" + field + ") "
            cursor = self.__query(self.__getFindSql(self.getTableName()))
            return cursor.fetchone()[0]
        else:
            return 0

    # 统计查询 Min
    def min(self, field):
        if self.__fieldExists(field):
            self.sql_field = " MIN(" + field + ") "
            cursor = self.__query(self.__getFindSql(self.getTableName()))
            return cursor.fetchone()[0]
        else:
            return 0

    # 统计查询 Avg
    def avg(self, field):
        if self.__fieldExists(field):
            self.sql_field = " AVG(" + field + ") "
            cursor = self.__query(self.__getFindSql(self.getTableName()))
            return cursor.fetchone()[0]
        else:
            return 0

    # 统计查询 Sum
    def sum(self, field):
        if self.__fieldExists(field):
            self.sql_field = " SUM(" + field + ") "
            cursor = self.__query(self.__getFindSql(self.getTableName()))
            return cursor.fetchone()[0]
        else:
            return 0

    # 执行更新数据操作（需要更新数据字典）
    def save(self, data):
        data = self.__dataProcess(data)
        if isinstance(data, dict) and len(data) > 0:
            sql_updata = ' '
            keys = list(data.keys())
            values = list(data.values())
            for index in range(len(data)):
                sql_updata += keys[index] + " = "
                if isinstance(values[index], str):
                    sql_updata += "'" + values[index] + "' "
                else:
                    sql_updata += str(values[index]) + " "
                if index < len(data) - 1:
                    sql_updata += ", "
            QUERY = "UPDATE " + self.getTableName() + " SET " + sql_updata
            if hasattr(self, 'sql_where') and len(self.sql_where) > 0:
                QUERY += ' WHERE ' + self.sql_where + " ; "
            self.__query(QUERY, commit=True)
        self.__reset()

    # 执行删除数据操作
    def delete(self):
        QUERY = "DELETE FROM " + self.getTableName()
        if hasattr(self, 'sql_where') and len(self.sql_where) > 0:
            QUERY += ' WHERE ' + self.sql_where + " ; "
        self.__query(QUERY, commit=True)

    # 私有方法 ==================================================
    # 复位局部变量,防止二次调用异常
    def __reset(self):
        self.__delattr('insertData')
        self.__delattr('sql_where')
        self.__delattr('sql_field')
        self.__delattr('sql_order')
        self.__delattr('sql_datas')

    # 删除参数函数，防止报错
    def __delattr(self, value):
        if hasattr(self, value):
            delattr(self, value)

    # 获取默认表结构
    def __getDefaultField(self):
        fieldList = []
        try:
            cursor = self.__query(self.__getFindSql(self.getTableName(), 1, 0))
            for item in cursor.description:
                fieldList.append(item[0])
        finally:
            return fieldList

    # 检测字段是否存在
    def __fieldExists(self, key):
        return key in self.tableField

    # 数据处理方法，接收到的数据需要传入该方法后输出标准格式的dict变量
    def __dataProcess(self, dataObj, isCheckKey=True):
        retDict = {}
        retList = []
        if isinstance(dataObj, str):
            return self.__dataProcess(dataObj.strip().split(','), isCheckKey)
        elif isinstance(dataObj, (list, tuple)) and len(dataObj) > 0:
            for index in range(len(dataObj)):
                if isinstance(dataObj[index], dict):
                    retList.append(self.__dataProcess(dataObj[index], isCheckKey))
                elif isinstance(dataObj[index], str):
                    dataList = dataObj[index].strip().stlit(' ', 1)
                    if len(dataList) == 2:
                        retDict[dataList[0].strip()] = dataList[1].strip()
                    else:
                        retDict[dataList[0].strip()] = ''
            if len(retList) > 0:
                return retList
            if len(retDict) > 0:
                return self.__dataProcess(retDict, isCheckKey)
        elif isinstance(dataObj, dict) and len(dataObj) > 0:
            for key in dataObj.keys():
                if not isCheckKey or self.__fieldExists(key):
                    retDict[key] = dataObj[key]
        return retDict

    # 获取查询SQL命令
    def __getFindSql(self, tableName, limit=0, page=0):
        sql_where = getattr(self, 'sql_where', None)
        sql_field = getattr(self, 'sql_field', '*')
        sql_order = getattr(self, 'sql_order', None)
        QUERY = "SELECT " + sql_field
        QUERY += " FROM " + tableName
        if isinstance(sql_where, str) and len(sql_where) > 0:
            QUERY += " WHERE " + sql_where
        if isinstance(sql_order, str) and len(sql_order) > 0:
            QUERY += " ORDER BY " + sql_order
        if limit > 0:
            QUERY += " LIMIT "
            if page > 0:
                QUERY += str(page * limit) + ","
            QUERY += str(limit) + " "
        return QUERY

    # 获取添加数据SQL命令
    def __getAddDataSql(self, tableName, sql_datas):
        if isinstance(sql_datas, list) and len(sql_datas) > 0:
            QUERY = []
            for data in sql_datas:
                QUERY.append(self.__getAddDataSql(tableName, data))
            return QUERY
        elif isinstance(sql_datas, str):
            return "INSERT INTO " + tableName + " " + sql_datas + "; "

    # 执行SQL命令
    def __query(self, sql, commit=False):
        cursor = self.getConnection().execute(sql)
        if commit:
            self.getConnection().commit()
        self.__reset()
        return cursor

    # 查询结果转字典结果
    def __cursor2dict(self, column, row):
        retList = []
        columnList = []
        for item in column:
            columnList.append(item[0])
        for value in row:
            retDict = {}
            for index in range(len(columnList)):
                retDict[columnList[index]] = value[index]
            retList.append(retDict)
        return retList
