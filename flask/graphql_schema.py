from graphene import ObjectType, String, ID, Schema, Field

class Movie(ObjectType):
    id = ID(required=True)
    name = String()
