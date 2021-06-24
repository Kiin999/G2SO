import os
 
env_var = input('Por favor, insira o nome da variável de ambiente:\n')
 
env_var_value = input('Por favor, insira o nome da variável de ambiente:\n')
 
os.environ[env_var] = env_var_value
 
print(f'{env_var}={os.environ[env_var]} variável de ambiente foi definida.')
