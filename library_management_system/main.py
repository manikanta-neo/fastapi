import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from resolvers import Query
from mutations import BookMutations

app = FastAPI()

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=BookMutations)))
