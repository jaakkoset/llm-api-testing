from invoke import task
#Black test
bad_list = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a",]

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
