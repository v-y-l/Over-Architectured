from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(description="A simple 'Hello World' query")

    def resolve_hello(self, info):
        return "Hello, World!"

schema = Schema(query=Query)
