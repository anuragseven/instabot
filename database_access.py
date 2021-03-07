import pymongo
import credentials as cr


def get_db_client():
    client = pymongo.MongoClient(cr.azure_cosmos_db_uri)
    return client


def log_script_error(timestamp, error_description):
    client = get_db_client()
    collection = client.get_database('datahunkbot').get_collection('instabot')
    collection.update_one({'description': 'error_log'}, {'$push':
        {'log.script_error':
            {
                "timestamp": timestamp,
                "error_description": error_description
            }
        }
    }
                          )
    client.close()


def log_graph_api_error(collection, timestamp, error_code, error_description, admin_remark):
    collection.update_one({'description': 'error_log'},
                          {'$push': {'log.instagram_graph_api_error':
                              {
                                  "timestamp": timestamp,
                                  "error_code": error_code,
                                  "error_description": error_description,
                                  "admin_remark": admin_remark

                              }
                          }
                          }
                          )


def log_published_content(collection, serial, timestamp, id_from_graph_api):
    collection.update_one({'description': 'published_contents_history'},
                          {'$push': {
                              'published':
                                  {
                                      "serial": serial,
                                      "timestamp": timestamp,
                                      "id": id_from_graph_api

                                  }
                          }})


def set_last_published_pic_serial(collection, serial):
    collection.update_one({'description': 'maintains_last_published_pic_serial'},
                          {'$set':
                              {
                                  'last_pic_serial': serial
                              }
                          }
                          )


def get_last_published_pic_serial(collection):
    response = collection.find_one({'description': 'maintains_last_published_pic_serial'})
    return response['last_pic_serial']


def get_pic_using_serial(collection, serial):
    response = collection.find_one(
        {
            "description": "contents_for_publishing"},
        {'pics':
             {'$elemMatch':
                  {'serial': serial}
              }
         }
    )
    return response['pics'][0]


def get_pic_array_count(collection):
    response = list(collection.aggregate([{'$project': {'pics': {'$size': "$pics"}}}]))
    return response[0]['pics']


