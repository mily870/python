# pessoas = {'nome' : 'kamily' , 'sexo' : 'f' , 'idade' : 17}
# print (pessoas['nome'])
# print (f'a {pessoas ["nome"]} tem {pessoas ["idade"]} anos')
# print (pessoas . keys())
# print (pessoas . values ())
# print (pessoas . items ())

# brasil = []
# estado1 = {'uf' : 'rio de janeiro' , 'sigla' : 'rj'}
# estado2 = {'uf' : 'são paulo' , 'sigla' : 'sp'}
# brasil . append (estado1)
# brasil . append (estado2)
# print (estado1)
# print (estado2)
# print (brasil)
# print (brasil [0])
# print (brasil [1])
# print (brasil [0] ['uf'])
# print (brasil [1] ['sigla'])

estado = {}
brasil = []
for c in range (0,3):
    estado ['uf'] = str (input('unidade federativa'))