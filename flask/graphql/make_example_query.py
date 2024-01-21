from graphql import graphql
import schema as schema_module

query_string = '{ hello }'
result = graphql(schema_module.schema, query_string)

print(result.data['hello'])  # Output: Hello, World!
