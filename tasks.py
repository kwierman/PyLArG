from invoke import task

@task
def clean(ctx):
    try:
       ctx.run('find . -name *.pyc | xargs rm')
    except:
        pass
    ctx.run('rm -rf build')
    ctx.run('rm -rf dist')
    ctx.run('rm -rf *.egg-info')

@task(clean)
def build(ctx):
    ctx.run('python setup.py build')

@task(clean)
def install(ctx):
    ctx.run('python setup.py install')
