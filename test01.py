'''
Test for NSO tail-f maapi python code

Maagic API

Created on March 30,2017
'''


import ncs

with ncs.maapi.Maapi() as m:
    with ncs.maapi.Session(m,'admin','python'):
	#the first transaction 
	print dir(m)
	with m.start_read_trans() as t:
	    address=t.get_elem('/ncs:devices/device{n9k_1}/address')
	    print ("The 1st read : address = %s"% address)
	    root=ncs.maagic.get_root(t)
	    print root.devices
	    print (root.devices.device['n9k_1'].config.nx__interface.loopback['3'].description)
	    node=ncs.maagic.get_node(t,'/ncs:devices/device{n9k_1}')

	    ne_type=node.device_type.ne_type
            if ne_type=='cli':
                print "type is cli"
	    if ne_type=='netconf':
		print "type is netconf"
	    if ne_type=='generic':
		print "type is generic"
	    else:
		pass
		#do nothing	

        #the 2nd transaction
        with m.start_write_trans() as t:
	    node=ncs.maagic.get_node(t,'/ncs:devices/device{n9k_1}')
	    node.config.nx__interface.loopback['3'].description='Alex Test from NSO maapi python'
	    print node.config.nx__interface.loopback['3'].description
	    t.apply()
