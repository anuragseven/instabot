import decide as de
import time as tm
from database_access import log_script_error
from publish import start_publishing_process
from datetime import datetime


def main():
    print('inside main')
    try:
        while True:
            start, utc_time = de.should_start_publishing_process()

            if start:
                result = start_publishing_process()
                if result:
                    de.state_dict[utc_time]['published'] = True
                else:
                    de.state_dict[utc_time]['failed'] = True
            tm.sleep(5)

    except Exception as ex:
        log_script_error(str(datetime.utcnow()), str(ex) + ' ,admin remark: error occurred inside main')


if __name__ == '__main__':
    main()
