FILENAME = "EMAIL.LOG"

email_file = None

def log(name, email_address, photo_file):
    global email_file
    if email_file is None or email_file.closed:
        email_file = open(FILENAME, "a")
    print >> email_file, '%s::%s::%s' % (name, email_address, photo_file)
    email_file.flush()
def log__test__():
    log("Justin Shaw", "wyojustin@gmail.com",'photo.jpg')
    log("WyoLum", "info@wyolum.com",'photo.jpg')
    email_file.close()
    f = open(FILENAME)
    print f.read()
    
