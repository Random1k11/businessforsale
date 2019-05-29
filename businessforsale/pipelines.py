# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from businessforsale.models import (db_connect, create_table, Businesses, check_existence_row_in_db,
                                    get_value_from_databse, update_values)
from scrapy.utils.project import get_project_settings



class BusinessforsalePipeline(object):


    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        session = self.Session()
        BusinessesDB = Businesses()
        BusinessesDB.title                = item['title']
        BusinessesDB.location             = item['location']
        BusinessesDB.price                = item['price']
        BusinessesDB.revenue              = item['revenue']
        BusinessesDB.cash_flow            = item['cash_flow']
        BusinessesDB.business_description = item['business_description']
        BusinessesDB.dictionary_details   = item['dictionary_details']
        BusinessesDB.listing_id           = item['listing_id']
        BusinessesDB.SOURCE               = item['SOURCE']
        BusinessesDB.section              = item['section']
        BusinessesDB.URL                  = item['URL']

        try:
            if check_existence_row_in_db(BusinessesDB.listing_id) == None:
                session.add(BusinessesDB)
                session.commit()
            culumns_BusinessesDB = [i for i in dir(BusinessesDB) if not i.startswith('_') and i != 'metadata' and i != 'id' and i != 'dictionary_details' and i != 'created_date'\
                                    and i != 'listing_id' and i != 'URL']
            if get_project_settings().get('UPDATE_VALUES_IN_DATABASE') == True:
                for column in culumns_BusinessesDB:
                    if getattr(BusinessesDB, column) != getattr(get_value_from_databse(BusinessesDB.listing_id), column):
                        print(getattr(BusinessesDB, column), '||||', getattr(get_value_from_databse(BusinessesDB.listing_id), column))
                        result = [BusinessesDB.title, BusinessesDB.location, BusinessesDB.price, BusinessesDB.revenue, BusinessesDB.cash_flow, BusinessesDB.business_description]
                        update_values(BusinessesDB.listing_id, result)
        except:
            session.rollback()
            raise
        finally:
            session.close()
