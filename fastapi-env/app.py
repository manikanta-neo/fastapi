'''
GitHub
strawberry-graphql/strawberry
Last Release
1 day ago
Stars
1k
License
MIT License

Strawberry is a Python library for implementing code first GraphQL servers using modern
Python features like type hints.

Then run strawberry server app and you will have a basic schema server running on http://localhost:8000/.

Strawberry also has views for ASGI, Flask and Django and provides utilities like dataloaders and tracing.
'''
import strawberry

@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: str = "World") -> str:
        return f"Hello {name}"

schema = strawberry.Schema(query=Query)