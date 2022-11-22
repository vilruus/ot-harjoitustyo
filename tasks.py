from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

##TODO: Implement tests
@task
def test(ctx):
    ctx.run("pytest src", pty=True)

##Todo: Implement coverage
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)