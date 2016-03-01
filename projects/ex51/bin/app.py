import web

urls = (
    '/', 'index',
    '/hello', 'Index', 
    '/topdog', 'topdog',
    '/bottomdog', 'bottomdog',
    '/foo', 'foo'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):    
        form = web.input(greet="Hiya", name='Nobody')
        greeting = '%s, %s' % (form.greet, form.name)
        return render.index(greeting = greeting)

class topdog:
    def GET(self):
        truth = "You're a cool guy."
        return render.goodbud(coolguy = truth)

class bottomdog:
    def GET(self):
        return render.goodbud('')

class foo:
    def GET(self):
        return render.foo()

if __name__ == "__main__":
    app.run()
