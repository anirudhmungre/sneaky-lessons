from mimesis import Person


person = Person("En")
data = []
for i in range(100):
    data.append({
        "fullName": person.full_name(),
        "age": person.age(),
        "bloodType": person.blood_type()
    })
print(data)
