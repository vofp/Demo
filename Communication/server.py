import sys
import pickle

class Message:
	def __init__(self, mod_id, mes_type, data):
		self.module_id = mod_id
		self.message_type = mes_type
		self.data = data


mod_name = raw_input('Module: ')

id = {
	"basestation" : 0,
	"beaglebone"  : 1,
	"wheel1"      : 2,
	"wheel2"      : 3,
	"wheel3"      : 4,
	"wheel4"      : 5,
	"wheel5"      : 6,
	"wheel6"      : 7,
	"arm"         : 8,
	"tripod"      : 9
	}

m = Message(id[mod_name], 0, [1,2,3])

sys.stdout.write("Sending message to module " + mod_name + " (id="+str(m.module_id)+ ")\n")

m = [m.module_id,m.message_type,m.data]
m_str = pickle.dumps(m)
print len(m_str)

fifo = open("testFifo", "w")
print "fifo opened"
fifo.write(m_str)
