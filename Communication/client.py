import sys
import pickle
class Message:
	def __init__(self, mod_id, mes_type, data):
		self.module_id = mod_id
		self.message_type = mes_type
		self.data = data
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
fifo = open("testFifo", "r")
print "fifo opened"
mes_str = fifo.read()
print mes_str

m_list = pickle.loads(mes_str)
m = Message(m_list[0], m_list[1], m_list[2])
print "recieved message with id=" + str(m.module_id)

if id["basestation"] == m.module_id:
	print "message is for basestation"
