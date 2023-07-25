"""
Routes and views for the bottle application.
"""

from bottle import route, view, error, run, template, response, request, redirect, auth_basic
from datetime import datetime
import CsvDB
import eventDB


@route('/')
@view('front_pg')
def landing():
    """Renders the contact page."""
    return dict(
        title='Chennai Culture & Heritage Club',
        message='Sign in to continue.',
        year=datetime.now().year
    )

@route('/membership')
@view('membership')
def membership():
    """Renders the contact page."""
    ty=None
    username=None
    fname=None
    return dict(
        title='Chennai Culture & Heritage Club',
        message='Sign in to continue.',
        year=datetime.now().year,
        ty=ty,
        username=username,
        fname=fname
    )


@route('/loginPage')
@view('login')
def loginPage():
    """Renders the contact page."""
    name = request.cookies.username or 'Guest'
    return dict(
        title='Chennai Culture & Heritage Club',
        message='Sign in to continue.',
        year=datetime.now().year,
        name=name,
        errmsg=''
    )

@route('/registrationPage')
def registrationPage():
    """Renders the contact page."""
    name = request.cookies.username or 'Guest'
    return template('reg_form',
        title='Chennai Culture & Heritage Club',
        message='Create your account.',
        year=datetime.now().year,
        errormessage='',
        record = None
    )

@route('/login', method='POST')
def do_login():
    username = request.forms.get('email')
    password = request.forms.get('pwd')
    if CsvDB.check_credentials(username, password) is True:
        record = CsvDB.DISPLAY(username)
        response.set_cookie("account", username, secret='some-secret-with-Harish')
        response.set_cookie("pwd", password, secret='some-secret-with-Harish')
        response.set_cookie("fname", record[0], secret='some-secret-with-Harish')
        response.set_cookie("mt", record[11], secret='some-secret-with-Harish')
        response.set_cookie("ty", record[12], secret='some-secret-with-Harish')
        return redirect('/home')
    else:
        return template('login',
                title = 'Heritage of Tamil Nadu',
                message='Sign in to continue.',
                year = datetime.now().year,
                errmsg = "Login failed. Wrong User name or password."
                )

@route('/logout')
def do_logout():
   response.delete_cookie("account")
   response.delete_cookie("fname")
   response.delete_cookie("ty")
   response.delete_cookie("mt")
   return redirect('/')

@route('/home')
@view('index')
def home():
    """Renders the home page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        return dict(
            username = username,
            fname = fname,
            mt = mt,
            ty=ty,
            year=datetime.now().year
        )
    else:
         return redirect('/loginPage')


@route('/create', method='POST')
def create():
    """Create new user."""
    fnam = request.forms.get('first_name')
    lnam = request.forms.get('last_name')
    eid = request.forms.get('email')
    gender = request.forms.get('gender')
    pno = request.forms.get('phone')
    dob = request.forms.get('birthday')
    add1 = request.forms.get('street')
    city = request.forms.get('city')
    region = request.forms.get('region')
    pc = request.forms.get('pc')
    country = request.forms.get('country')
    mt = request.forms.get('membership')
    heritage = request.forms.get('heritage')
    dance = request.forms.get('dance')
    music = request.forms.get('music')
    print(heritage)
    print(dance)
    print(music)
    ty=""
    if heritage != None:
        ty += str(3)
    if dance != None:
        ty +=str(2)
    if music != None:
        ty +=str(1)
    pw = request.forms.get('pwd')

    if CsvDB.check(eid) is False:
        CsvDB.CREATE(fnam,lnam, eid, gender, pno, dob, add1, city, region, pc, country, mt, ty, pw)
        return redirect('/loginPage')
    else:
        return template('reg_form',
        title = 'Heritage of Tamil Nadu',
        year = datetime.now().year,
        errormessage = "This user already exist",
        record = (fnam,lnam, eid, gender, pno, dob, add1, city, region, pc, country, mt, ty, pw)
        )


@route('/update', method='POST')
def update():
    """update new user."""
    fnam = request.forms.get('first_name')
    lnam = request.forms.get('last_name')
    eid = request.forms.get('email')
    gender = request.forms.get('gender')
    pno = request.forms.get('phone')
    dob = request.forms.get('birthday')
    add1 = request.forms.get('street')
    city = request.forms.get('city')
    region = request.forms.get('region')
    pc = request.forms.get('pc')
    country = request.forms.get('country')
    mt = request.forms.get('membership')
    heritage = request.forms.get('heritage')
    dance = request.forms.get('dance')
    music = request.forms.get('music')
    print(heritage)
    print(dance)
    print(music)
    ty=""
    if heritage != None:
        ty += str(3)
    if dance != None:
        ty +=str(2)
    if music != None:
        ty +=str(1)
    pw = request.forms.get('pwd')
    CsvDB.EDIT(fnam,lnam, eid, gender, pno, dob, add1, city, region, pc, country, mt, ty, pw)
    return redirect('/home')


@route('/select', method='GET')
@view('reg_form_session')
def select():
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        record = CsvDB.DISPLAY(username)
        print(record)
        return dict(
            title='Heritage of India',
            message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
            username = username,
            fname = fname,
            mt = mt,
            ty=ty,
            record=record,
            year=datetime.now().year
        )
    else:
         return redirect('/loginPage')


@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        return dict(
            title='Heritage of India',
            message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
            username = username,
            fname = fname,
            mt = mt,
            ty=ty,
            year=datetime.now().year
        )
    else:
         return redirect('/loginPage')

@route('/heritage')
@view('heritage_v2')
def heritage():
    """Renders the heritage page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        return dict(
            title='Heritage of Tamil Nadu',
            message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
            year=datetime.now().year,
            fname = fname,
            mt = mt,
            ty=ty,
            username=username
        )
    else:
         return redirect('/loginPage')

@route('/heritage/<name>')
def heritage(name):
    """Renders the heritage page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        return template(name,
            title='Heritage of Tamil Nadu',
            message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
            year=datetime.now().year,
            fname = fname,
            mt = mt,
            ty=ty,
            username=username
        )
    else:
        return redirect('/loginPage')

@route('/dance')
@view('dance_v2')
def dance():
    """Renders the dance page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        return dict(
            title='Heritage of India',
            message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
            year=datetime.now().year,
            fname = fname,
            mt = mt,
            ty=ty,
            username=username
        )
    else:
         return redirect('/loginPage')

@route('/dance/<name>')
def dance(name):
    """Renders the heritage page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        return template(name,
            title='Heritage of India',
            message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
            year=datetime.now().year,
            fname = fname,
            mt = mt,
            ty=ty,
            username=username

        )
    else:
        return redirect('/loginPage')

@route('/music')
@view('music')
def music():
    """Renders the music page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        return dict(
            title='Heritage of India',
            message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
            year=datetime.now().year,
            fname = fname,
            mt = mt,
            ty=ty,
            username=username
        )
    else:
         return redirect('/loginPage')

@route('/music/<name>')
def music(name):
    """Renders the music page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        return template(name,
            title='Heritage of India',
            message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
            year=datetime.now().year,
            fname = fname,
            mt = mt,
            ty=ty,
            username=username
        )
    else:
        return redirect('/loginPage')


@route('/aboutus')
@view('cvsaptharangini')
def aboutus():
    """Renders the music page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        return dict(
            title='Heritage of India',
            message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
            year=datetime.now().year,
            fname = fname,
            mt = mt,
            ty=ty,
            username=username
        )
    else:
         return redirect('/loginPage')

@route('/delete', method='POST')
def delete():
    """update new user."""
    eid = request.forms.get('email')
    CsvDB.DELETE(eid)
    return redirect('/')

@error(404)  # changed from OP
def error404(error):
   return template('404',e=response.status_code)

@route('/eventform')
def registrationPage():
    """Renders the contact page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    name = request.cookies.username or 'Guest'
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        return template('eventform',
                        title='Heritage of India',
                        message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
                        year=datetime.now().year,
                        fname=fname,
                        mt=mt,
                        ty=ty,
                        username = name,

                        )

@route('/creates', method='POST')
def creates():
    """Event creating."""
    fnam = request.forms.get('Event name')
    lnam = request.forms.get('ID')
    eid = request.forms.get('place')
    gender = request.forms.get('time')
    pno = request.forms.get('event')
    dob = request.forms.get('Event Description')
    add1 = request.forms.get('phone')
    '''city = request.forms.get('etype')'''
    '''heritage = request.forms.get('heritage')
    dance = request.forms.get('dance')
    music = request.forms.get('music')
    print(heritage)
    print(dance)
    print(music)'''
    type=request.forms.get('etype')
    ty = ""
    if type!= None and type=="heritage":
        ty += str(3)
    if type!= None and type=="dance":
        ty += str(2)
    if type!= None and type=="music":
        ty += str(1)
    eventDB.CREATE(fnam,lnam, eid, gender, pno, dob, add1,ty)
    return redirect('/eventform')

@route('/events')
def events():
    """Renders the music page."""
    username = request.get_cookie("account", secret='some-secret-with-Harish')
    password = request.get_cookie("pwd", secret='some-secret-with-Harish')
    if CsvDB.check_credentials(username, password) is True:
        fname = request.get_cookie("fname", secret='some-secret-with-Harish')
        ty = request.get_cookie("ty", secret='some-secret-with-Harish')
        mt = request.get_cookie("mt", secret='some-secret-with-Harish')
        print(ty[0])
        print(mt)
        r = eventDB.DISPLAY(ty,mt)
        print(r)
        return template('eventshtml',
                        title='Heritage of India',
                        message='The state is also home to a large number of historic buildings, religious sites and heritage monuments, designated as UNESCO World Heritage Sites.',
                        year=datetime.now().year,
                        fname=fname,
                        mt=mt,
                        ty=ty,
                        username=username,
                        r=r
                        )

    else:
         return redirect('/loginPage')
