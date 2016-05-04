#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

class RezultatHandler(MainHandler): 
    def post(self):
        stevec = (self.request.get("stevec"))

        stevec = 0

        odgovor_slo = str(self.request.get("odgovor_slo"))
        odgovor_it = str(self.request.get("odgovor_it"))
        odgovor_at = str(self.request.get("odgovor_at"))
        odgovor_fr = str(self.request.get("odgovor_fr"))
        odgovor_sr = str(self.request.get("odgovor_sr"))
        odgovor_sp = str(self.request.get("odgovor_sp"))

    
        
        if odgovor_slo == "Ljubljana":
            stevec += 1   
        else: 
            stevec -= 1
        
        if odgovor_it == "Rim":
            stevec += 1   
        else: 
            stevec -= 1

        if odgovor_at == "Dunaj":
            stevec += 1   
        else: 
            stevec -= 1

        if odgovor_fr == "Pariz":
            stevec += 1   
        else: 
            stevec -= 1

        if odgovor_sr == "Beograd":
            stevec += 1   
        else: 
            stevec -= 1
    
        if odgovor_sp == "Madrid":
            stevec += 1   
        else: 
            stevec -= 1


        view_vars = {
            "stevec": stevec,
            "odgovor_slo": odgovor_slo,
            "odgovor_it": odgovor_it,
            "odgovor_at": odgovor_at, 
            "odgovor_fr": odgovor_fr,
            "odgovor_sr": odgovor_sr,
            "odgovor_sp": odgovor_sp,
}
   
        return self.render_template("rezultat.html", view_vars)



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
     webapp2.Route('/rezultat', RezultatHandler)
], debug=True)
