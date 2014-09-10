from db import database as self
from time import time
def init(mgr):
	mgr.addCommand('delMsg', 'delete a message', delMsg, 3)
	mgr.addCommand('delUserMsg', 'delete a users messages', delUserMsg, 4)
	mgr.addCommand('addMod', 'add a moderator', addMod, 5)
	mgr.addCommand('removeMod', 'remove a mod', removeMod, 6)
	mgr.addCommand('banUser', 'ban a user', banUser, 7)
	mgr.addCommand('unbanUser', 'unban a user', unBan, 8)

def delMsg(mgr, args):
	room = args[0]
	msgid = args[1]
        self.delMsg(room, msgid)
        mgr.callProtocal('msgremove:%s:%s:%s' % (room, msgid, time()))
def delUserMsg(mgr, args):
	room = args[0]
	user = args[1]
        self.delUserMsg(room, user)
        mgr.callProtocal('usermsgremove:%s:%s:%s' % (room, user, time()))
def addMod(mgr, args):
	room = args[0]
	user = args[1]
        self.addMod(room, user)
        mgr.callProtocal('mod:%s:%s:%s' % (room, user, time()))
def removeMod(mgr, args):
	room = args[0]
	user = args[1]
        self.removeMod(room, user)
        mgr.callProtocal('demod:%s:%s:%s' % (room, user, time()))
def banUser(mgr, args):
	room = args[0]
	user = args[1]
	target = args[2]
        self.banUser(room, user, target)
        mgr.callProtocal('banned:%s:%s:%s:%s' % (room, user, target, time()))
def unbanUser(mgr, args):
	room = args[0]
	user = args[1]
	target = args[2]
        self.unbanUser(room, user, target)
        mgr.callProtocal('unbanned:%s:%s:%s:%s' % (room, user, target, time()))
