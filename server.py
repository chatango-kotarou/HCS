'''
status: UNFINSHED
gotta give credit for peaces of code thats not mine
cred: lumirayz code used addcommand functions/classes
CONNECTION TYPE: HTML5
EMAIL: yuri9911324@gmail.com
contributers: Kotarou
'''

import glob
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
class server(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        self.modDirectory = 'modules/*.py'
        self.files = glob.glob(self.modDirectory)
	#print(self.files)
        #CALL ON INIT
	self.modules = dict()
        self.commands = list()
	self.msg = dict()
	self.ip = self.request.remote_ip
	self.uip = {}
        self.loadModules()
        data = message.split(':', 1)
        if len(data) == 1:
            cmd, args = data[0]
        else:
            cmd, args = data
        key = cmd
        self.getCommand(cmd)
        cmd = self.getCommand(key)
        if cmd:
            if cmd:
                cmd.check(self, args)
    def loadModules(self):
        '''
        load modules that are found in self.files>glob.glob('directory/*.py')
        '''
	self.modules = {}
	self.commands = []
        for f in self.files:
	    execfile(f, self.modules)
	for key, value in self.modules.items():
	   if key == 'init':
		value(self)
    def callProtocal(self, evt):
        '''
        sends the protocals
        '''
	self.write_message(evt)
    def clearCommands(self):
        '''
        clears protocal list
        '''
        self.commands = list()
    def addCommand(self, *args, **kw):
        '''
        add the protocal to the list protocal>description>function>id
        '''
        co = Command(*args, **kw)
        self.commands.append(co)
    def getCommand(self, name):
        '''
        search for the protocal then returns the result
        '''
        name = name.lower()
        for command in self.commands:
            if command.name == name:
                return command
	return None
class Command(object):
        def __init__(self, name, desc, func, number = 0):
            self.name = name
            self.desc = desc
            self.number = int(number)
            self.func = func
            
        def run(self, mgr, args):
            
            if not args: return False
            else: return True
        def check(self, mgr, args):
            if not self.run(mgr, args): return
            else: self.func(mgr, args)
if __name__=="__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', server)])
    __SERVER__ = tornado.httpserver.HTTPServer(app)
    __SERVER__.listen(address='localhost', port=6444)
    tornado.ioloop.IOLoop.instance().start()
