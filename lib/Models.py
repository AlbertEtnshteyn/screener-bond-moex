

class Bond():
    name = "Bond"

#     """
#     https://www.moex.com/ru/listing/securities.aspx
#     https://www.moex.com/ru/issue.aspx?code=secid
#     https://www.moex.com/ru/issue.aspx?code=RU000A1047S3

#     К сож. в беспл ISS MOEX не доступны orderbook ни в каком видео
#     """
#     __tablename__ = "bonds"
#     id = Column(Integer, primary_key=True)
#     secid = Column(String)
#     shortname = Column(String)

#     price = Column(Float) # цена в проц от номинала
#     tradedate = Column(DateTime) # дата посл торгов, если при последней проверке торгов не было - заношу дату проверки
#     yieldsec = Column(Float) # расчитанная мосбиржей доходность в соотв. запросе (может отличаться нюансами)
#     volume = Column(Integer) # объем торгов на посл сессиий в выбраном режиме торгов (board)
#     matdate = Column(DateTime) # Дата погашения
#     couponfrequency = Column(Integer) # частота выплаты купона
#     couponpercent = Column(Float) # купон %
#     listlevel = Column(Integer) # Уровень листинга - 1 круто, 3 - нет

#     updated = Column(DateTime)

#     is_traded = Column(Boolean)
#     emitent_id = Column(Integer)
#     type = Column(String) # тип облиги (корп, офз, муниц)
#     primary_boardid = Column(String) # осн. режим торгов (board)

#     issuedate = Column(DateTime) # Дата начала торгов
#     initialfacevalue = Column(Integer) # Первоначальная номинальная стоимость
#     faceunit = Column(String) # валюта
#     issuesize = Column(Integer) # объем выпуска
#     facevalue = Column(Float) # Номинальная стоимость
#     coupondate = Column(DateTime) # дата след купона (при условии обновленной базы)
#     couponvalue = Column(Float) # купон нв деньгах
#     isqualifiedinvestors = Column(Boolean) # только для квалов
#     earlyrepayment = Column(Boolean) # Возможен досрочный выкуп
