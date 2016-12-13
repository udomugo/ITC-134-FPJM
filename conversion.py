import cgi

forms = """<html>
 <body>
   <h1>Index Page</h1>
   
   <form  method=post>
   <fieldset>
   <legend>TEMPERATURE CONVERSION</legend>
      <p>
         <input type="radio" name="options" id="option1" value="option1"> Celsius to Fahrenheit <br>
	 <input type="radio" name="options" id="option2" value="option2"> Fahrenheit to Celsius <br>
      </p>
   <ul>
      <li>Enter Temperature: <input name='temp'></li>
   </ul>
   <p><input type='submit' value='CONVERT/clr'></p> 
   </fieldset>
    </form> 
 </body>
</html>
"""    
    
def application(environ, start_response):
    """A WSGI application to show the use of cgi.FieldStorage to
    handle form data"""
    
    # use FieldStorage but we need to pass in the wsgi.input input stream
    # for POST requests and the environ variable for the environment
    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    if 'temp' in form and form.getvalue('options') == 'option1':
        temp = Conversion.CtoF(Conversion(form.getvalue("temp", "")))
        info = "<p>%s Celsius is %s F</p>" % (form.getvalue("temp"),temp)
    elif 'temp' in form and form.getvalue('options') == 'option2':
        temp = Conversion.FtoC(Conversion(form.getvalue("temp", "")))
        info = "<p>%s Fahrenheit is %s C</p>" % (form.getvalue("temp"),temp)
    else:
        info = "<p></p>"

    # No form submitted
    page = [b"<html>", forms.encode(), info.encode(), b"</html>"]
    
    headers = [('content-type', 'text/html')]
    start_response('200 OK', headers)
    return page
	
	
	
class Conversion:
    def __init__(self, temp):
        self.temp = int(temp)

    def CtoF(self):
        return self.temp * (9/5) + 32

    def FtoC(self):
        return (self.temp - 32) * (5 / 9)
