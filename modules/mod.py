from db import database as self
from time import time
def init(mgr):
	mgr.addCommand('delMsg', 'delete a message', delMsg, 3)
	mgr.addCommand('delUserMsg', 'delete a users messages', delUserMsg, 4)
	mgr.addCommand('addMod', 'add a moderator', addMod, 5)
	mgr.addCommand('removeMod', 'remove a mod', removeMod, 6)
	mgr.addCommand('banUser', 'ban a user', banUser, 7)
	mgr.addCommand('unbanUser', 'unban a user', unBan, 8)

def delMsg(room, msgid):
        self.delMsg(room, msgid)
        mgr.callProtocal('msgremove:%s:%s:%s' % (room, msgid, time))
def delUserMsg(room, user):
        self.delUserMsg(room, user)
        mgr.callProtocal('usermsgremove:%s:%s:%s' % (room, user, time))
def addMod(room, user):
        self.addMod(room, user)
        mgr.callProtocal('mod:%s:%s:%s' % (room, user, time))
def removeMod(room, user):
        self.removeMod(room, user)
        mgr.callProtocal('demod:%s:%s:%s' % (room, user, time))
def banUser(room, user, target):
        self.banUser(room, user, target)
        mgr.callProtocal('banned:%s:%s:%s:%s' % (room, user, target, time))
def unbanUser(room, user, target):
        self.unbanUser(room, user, target)
        mgr.callProtocal('unbanned:%s:%s:%s:%s' % (room, user, target, time))
