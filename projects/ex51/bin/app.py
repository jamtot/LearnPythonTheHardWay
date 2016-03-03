import web

urls = (
    #'/', 'index',
    '/hello', 'Index', 
    '/topdog', 'topdog',
    '/bottomdog', 'bottomdog',
    '/foo', 'foo',
    '/pic', 'load_pic',
    '/thank', 'thankyou'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

"""class index:
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)"""

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):    
        form = web.input(greet="Hiya", name='Nobody')
        greeting = '%s, %s' % (form.greet, form.name)
        return render.index(greeting = greeting)

class load_pic(object):
    def GET(self):
        return render.picload()

    def POST(self):
        form = web.input(picfile={})
        savefolder = 'pics/'
        if form.picfile.filename:
            filepath=form.picfile.filename.replace('\\','/') # changes all the \\ to /
            filename=filepath.split('/')[-1] # take the filename (last bit after the last /
            output = open(savefolder+filename, 'w')
            output.write(form.picfile.file.read())
            output.close()
            return render.thanks()
        else:
            return render.boo()

class thankyou:
    def GET(self):
        return render.thanks()

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
