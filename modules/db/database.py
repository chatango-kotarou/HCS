'''
DATABASE MODULE FOR ALL MODULES
'''
import time
import mid
import uid
import hashlib
import sqlite3 as m
db = m.connect('CHAT.sqlite3')
cur = db.cursor()

def ip(id, ip, mode='id'):
	try:
		cur.execute('select * from ip where id like("%s")' % (id))
		ip = ''.join([i[1] for i in cur.fetchall()])
		return ip
	except:
                ssid = ip.replace('anon', '')
                cur.execute('select * from ssid where like("%s")' % ssid)
                ip = ''.join([i[2] for i in cur.fetchall()])
                return ip
                
def setIp(id, ip):
	try:
		cur.execute('delete from ip where id like("%s")' %(id))
		cur.execute('insert into ip(id, ip) values("%s", "%s")' % (id, ip))
		db.commit()
	except:
		cur.execute('insert into ip(id, ip) values("%s", "%s")' % (id, ip))
                db.commit()
def setSsid(room, ip):
	sid = random.randrange(1000, 9000)
	try:
		cur.execute('select room, ssid from ssid room="%s", ssid="%s"' % (room, str(sid)))
		ssid = [ssid[1] for ssid in cur.fetchall()]
		if str(sid) in ssid:
			while True:
				r = random.randrange(1000, 9000)
				if r not in ssid:
					cur.execute('insert into ssid(ssid, room, ip) values("%s", "%s", "%s")' % (r, room, ip))
                			db.commit()
					return r
					break
	except:
		cur.execute('insert into ssid(ssid, room, ip) values("%s", "%s", "%s")' % (r, room, ip))
                db.commit()
		return str(sid)
	
def setConnected(user, ip, room):
	try:
                cur.execute('delete from connected where room="%s", user="%s"' %(room, user))
                cur.execute('insert into connected(user, ip) values("%s", "%s", "%s")' % (user, ip, room))
                db.commit()
        except:
                cur.execute('insert into connected(user, ip) values("%s", "%s", "%s")' % (user, ip, room))
                db.commit()
def getConnected(room, user):
	try:
		 cur.execute('select room, user from connected where room="%s", user="%s"' % (room, user))
                 user = ''.join([i[0] for i in cur.fetchall()])
                 return True
	except: return False
def setMessage(room, user, msg):
        userid = UID(user)
        ip = ip(userid)
	msgid = mid.generate()
	cur.execute('insert into messages(room, user, message, msgid, userid, ip) values("%s", "%s", "%s", "%s", "%s", "%s")' % (room, user, msg, userid, ip))
        db.commit()
def getMessage(user):
        cur.execute('select room, user from messages user="%s"' % user)
        lis = [a[0:] for a in cur.fetchall()]
        return lis
def delMsg(room, msgid):
        cur.execute('delete from messages where room="%s" msgid="%s"' %(room, msgid))
        db.commit()
def delUserMsg(room, user):
        cur.execute('delete from messages where room="%s", user="%s"' %(room, msgid))
        db.commit()

def banUser(room, user, target):
        tid = UID(target)
	try:
		cur.execute('delete from banlist where room="%s", user="%s", target="%s", id="%s", ip="%s"' % (room, user, target, tid, ip))
                cur.execute('insert into banlist(room, user, target, tid, ip, time) values("%s", "%s", "%s", "%s", "%s", "%s")' % (user, target, tid, ip, time.time()))
                db.commit()
        except:
		cur.execute('insert into banlist(room, user, target, tid, ip, time) values("%s", "%s", "%s", "%s", "%s", "%s")' % (user, target, tid, ip, time.time()))
                db.commit()
def unbanUser(room, user, target):
        if UID(target) == 'ip':
                ip = ip(user, mode = 'user')
	try:
		cur.execute('delete from banlist where room="%s", user="%s", target="%s", id="%s", ip="%s"' % (room, user, target, tid, ip))
		db.commit()
	except: pass
def getRoomOwner(room):
        cur.execute('select * from rooms where room="%s"' % room)
        owner = ''.join([n[1] for n in cur.fetchall()])
        return owner
def getBanlist(room):
	cur.execute('select * from banlist room="%s"' % room)
	l = [a[1] for a in cur.fetchall()]
	return l
def addMod(room, user):
	 try:
                cur.execute('delete from mods where room="%s", user="%s"' % (room, user))
		cur.execute('insert into mods(room, user, userid) values("%s", "%s", "%s")' % (room, user, time.time()))
                db.commit()
         except:
                cur.execute('insert into mods(room, user, userid) values("%s", "%s", "%s")' % (room, user, time.time()))
                db.commit()
def removeMod(room, user):
	 try:
		cur.execute('delete from mods where room="%s", user="%s"' % (room, user))
		db.commit()
	 except:
		return False

def register(user, password):
	cur.execute('insert into register(user, password userid, time) values("%s", "%s", "%s")' % (user, hashlib(password).hexdigest(),  uid.generate(), time.time()))
	db.commit()
def UID(user):
	cur.execute('select * from register where user like("%s")' % user)
	Uid = ''.join([n[2] for n in cur.fetchall()])
	return Uid
def check(user, password):
	cur.execute('select * from register where user like("%s")' % user)
	auth = ''.join([n[1] for n in cur.fetchall()])
	if hashlib(password).hexdigest == auth: return 'ok'
	else: return 'denied'
def getMods(room):
	cur.execute('select * from mods where room like("%s")' % mods)
	l = [i[1] for i in cur.fetchall()]
	return l
def getRoom(room, check = True):
	cur.execute('select * from rooms where room like("%s")' % room)
	r = ''.join([n[0] for n in cur.fechall()])
	if check == True:
		if r == room: return True
		elif r != room: return False
	elif check == False:
		return room
