Toy project to get a feel of the different components that go into modern software development.

For example, take a look at /v1/movie in flask app.py, which is restful, which stitches relational (carefully curated) and non-relational data (from scrapping).

There's potential to add kafka logging layer (maybe grpc to it from rust), and maybe graphql, etc.

Useful cleanup commands:

* git rm --cached $(git ls-files -i --exclude-from=.gitignore)