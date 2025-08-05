# from infra.repository.user_repository import UserRepository

# repo = UserRepository()

# #repo.insert('Teste','teste@gmail.com','54321','teste')
# #repo.insert('Teste1','teste1@gmail.com','54321','teste1')

# repo.delete('teste1')

# data = repo.select()

# # print(data)

# for row in data:
#     print(row)


#=====================================================================================================
from infra.repository.proprietarios_repository import ProprietariosRepository
from infra.repository.user_repository import UserRepository

repo = ProprietariosRepository()
response = repo.select()
# print(response)
for row in response:
    print(row)

repo2 = UserRepository()
response2 = repo2.select()
user = response2[0]
print(user.proprietarios)
print('#====='*10)
for row in response2:
    if row.proprietarios: # Essa linha alimina no print dados que estão vazio no loop (linhas no DB que não possuem user na tabela proprietario)
        print(row.proprietarios)
