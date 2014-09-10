from db import database as self
import random
def init(mgr):
    mgr.addCommand('bmsg', 'send a message to the room', message, number=1)
    mgr.addCommand('bauth', 'login', login, number=2)
def message(mgr, args):
    if self.isConnected(args[1]):
    	user = args[1]
    	room = args[2]
	if self.getRoom(room) != False:
    		msg = args[3]
    		_ip = self.ip(self.uid(user))
    		params = "b:%s:%s:%s:%s:%s" % (user, room, msg, _ip, self.uid(user))
    		mgr.callProtocal(params + '<br />')
	else:
		mgr.callProtocal('NROOM:NO ROOM FOUND')
    else:
		mgr.callProtocal('NROOM:NO ROOM FOUND')
		mgr.callProtocal('NT_CONNECTED:%s' % ('YOU ARE NOT SIGNED IN'))
def login(mgr, args):
	status =args[0]
	if status == 'bauth':
		room = args[1]
		usern = args[2]
		password = args[3]
		st = self.check(usern, password)
		if st == 'ok':
			id = self.uid(usern)
			conip = mgr.ip
			self.setConnected(usern, mgr.ip, room)
			_ip = self.ip(id)
			mgr.callProtocal('LGN_OK:%s:%s:%s:%s' % (room, usern, id, _ip))
		elif st == 'denied':
			anonid = mgr.setSsid(ip=_ip, room=room)	
			user = 'anon%s' % anonid
			self.setConnected(user, mgr.ip, room)
			mgr.callProtocal('LGN_DENIED:%s:%s' % (usern, _ip))
	if status == 'blogAnon' and not self.getRoom(room) == False:
		anonid = random.randrange(1000, 9000)
                self.setSsid(_ip, anonid)
                user = 'anon%i' % anonid
                self.setAnon(user ,_ip)
                mgr.callProtocal('anon_login:%s:%s' % (user, _ip))
