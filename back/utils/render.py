from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('../views'))

def render(template, data):
    template = env.get_template(template)
    return template.render(data=data)


if __name__ == '__main__':
    name='teste.jinja'
    print(render(name, {'names':['Julia','Joao','Maria']}))