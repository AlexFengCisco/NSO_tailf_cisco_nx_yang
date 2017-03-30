'''
test 02 for single transaction 
high level MAAPI 

'''

import ncs

with ncs.maapi.single_write_trans('admin','python') as t:
    t.set_elem2('Alex test pushed by python maapi NSO ','/ncs:devices/device{n9k_1}/config/nx:interface/loopback{3}/description')
    t.apply()



with ncs.maapi.single_read_trans('admin','python') as t:
    desc=t.get_elem('/ncs:devices/device{n9k_1}/config/nx:interface/loopback{3}/description')
    print desc
