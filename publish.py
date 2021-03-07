from datetime import datetime
import database_access as db
import insta_graph_apis as ig


def start_publishing_process():
    try:
        db_client = db.get_db_client()
        collection = db_client.get_database('datahunkbot').get_collection('instabot')
        serial = str(get_pic_serial_for_publishing(collection))
        print(serial)
    except Exception as ex:
        db.log_script_error(str(datetime.utcnow()), str(ex))
        return False

    try:
        published_pic_id = publish_pic_using_serial(collection, serial)
        print(published_pic_id)

    except Exception as ex:
        db.log_graph_api_error(collection, str(datetime.utcnow()), "serial " + serial, str(ex),
                               'error occured while '
                               'publishing')
        db_client.close()
        return False
    try:
        db.log_published_content(collection, serial, str(datetime.utcnow()), published_pic_id)
        db.set_last_published_pic_serial(collection, serial)
    except Exception as ex:
        db.log_script_error(str(datetime.utcnow()), str(ex))
        db_client.close()
        return True
    db_client.close()
    return True


def get_pic_serial_for_publishing(collection):
    last_published_serial = db.get_last_published_pic_serial(collection)
    total_pics_available = db.get_pic_array_count(collection)
    if total_pics_available == 0:
        return
    if (int(last_published_serial) % total_pics_available) != 0:
        return int(last_published_serial) + 1
    else:
        return 1


def publish_pic_using_serial(collection, serial):
    pic_details = db.get_pic_using_serial(collection, serial)
    url = pic_details['url']
    caption = pic_details['caption']
    container = ig.get_container_id_pic(image_url=url, caption=caption)
    published_pic_id = ig.publish_pic(container)
    return published_pic_id



