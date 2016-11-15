from invoke import task

@task
def clean(ctx):
    ctx.run('find . -name *.pyc | xargs rm')
    ctx.run('rm -rf build')
    ctx.run('rm -rf dist')
    ctx.run('rm -rf *.egg-info')

@task(clean)
def build(ctx):
    ctx.run('python setup.py build')

@task(clean)
def install(ctx):
    ctx.run('python setup.py install')
