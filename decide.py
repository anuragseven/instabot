import datetime as dt

state_dict = {
    '4:30': {
        'published': False,
        'failed': False,

    },
    '7:0': {
        'published': False,
        'failed': False,

    },
    '9:0': {
        'published': False,
        'failed': False,

    },
    '13:0': {
        'published': False,
        'failed': False,

    },
    '16:0': {
        'published': False,
        'failed': False,

    },

}


def should_start_publishing_process():
    utc_time = dt.datetime.utcnow()
    utc_hr = utc_time.hour
    utc_min = utc_time.minute

    if utc_hr == 4 and utc_min == 30:
        reset_state_dict_except('4:30')
        if not (state_dict['4:30']['failed']) and not (state_dict['4:30']['published']):
            return True, '4:30'
        else:
            return False, '4:30'

    elif utc_hr == 7 and utc_min == 0:
        reset_state_dict_except('7:0')
        if not (state_dict['7:0']['failed']) and not (state_dict['7:0']['published']):
            return True, '7:0'
        else:
            return False, '7:0'
    elif utc_hr == 9 and utc_min == 0:
        reset_state_dict_except('9:0')
        if not (state_dict['9:0']['failed']) and not (state_dict['9:0']['published']):
            return True, '9:0'
        else:
            return False,'9:0'
    elif utc_hr == 13 and utc_min == 0:
        reset_state_dict_except('13:0')
        if not (state_dict['13:0']['failed']) and not (state_dict['13:0']['published']):
            return True, '13:0'
        else:
            return False, '13:0'
    elif utc_hr == 16 and utc_min == 0:
        reset_state_dict_except('16:0')
        if not (state_dict['16:0']['failed']) and not (state_dict['16:0']['published']):
            return True, '16:0'
        else:
            return False, '16:0'
    else:
        return False, ''


def reset_state_dict_except(utc_time_str):
    for utc_time in state_dict:
        if utc_time == utc_time_str:
            pass
        else:
            state_dict[utc_time]['failed'] = False
            state_dict[utc_time]['published'] = False

