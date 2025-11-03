from g4f.client import Client

def generate():
    return Client().images.generate(model="flux",prompt=input("Введите промпт: "),response_format="url")

print(generate().data[0].url)
