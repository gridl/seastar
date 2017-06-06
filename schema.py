import graphene

class JobType(graphene.ObjectType):
    name = "Job"
    descrition = "..."

    # Sibling objects
    siblings = graphene.List('self')

    # Child objects
    processes = graphene.List('Process')

class ProcessType(graphene.ObjectType):
    name = "Process"
    description = "..."

    # Child objects
    threads = graphene.List('Thread')

class ThreadType(graphene.ObjectType):
    name = "Thread"
    description = "..."


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, args, context, info):
        return "Hello"

schema = graphene.Schema(query=Query)

