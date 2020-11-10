from graphene import ObjectType, String, Schema, Mutation, ID, Int

class Query(ObjectType):
    hello = String(name=String(default_value="名無しさん"))

    def resolve_hello(self, info, name):
        return f'こんにちは {name}さん'

class CreatePerson(Mutation):
    # created_id、created_name、created_ageが戻り値
    created_id = ID()
    created_name = String()
    created_age = Int()

    # name, ageが引数
    class Arguments:
        name = String()
        age  = Int()

    # mutateメソッドの引数はself,infoの次に引数が並ぶ
    def mutate(self, info, name, age):
        # ここで永続化する

        # Mutationを継承したクラスをインスタンス化して返す
        return CreatePerson(
            created_id=1,
            created_name=f'{name}さん',
            created_age=age + 10,
        )

class MyMutation(ObjectType):
    create_person = CreatePerson.Field()

schema = Schema(query=Query, mutation=MyMutation)

query_string = '{ hello }'
result = schema.execute(query_string)
print(result.data['hello'])

query_string_with_argument = '{ hello (name: "なんしー") }'
result = schema.execute(query_string_with_argument)
print(result.data['hello'])