import yaml



print("A python file which imports yml file")
with open('config\config.yml','r') as f:
    config = yaml.safeload(f)
    
print("A python file which imports yml file")

