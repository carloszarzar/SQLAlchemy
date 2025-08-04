from infra.repository.user_repository import UserRepository

repo = UserRepository()

#repo.insert('Teste','teste@gmail.com','54321','teste')
#repo.insert('Teste1','teste1@gmail.com','54321','teste1')

repo.delete('teste1')

data = repo.select()

# print(data)

for row in data:
    print(row)