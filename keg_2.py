from collections import defaultdict

random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "world", 412, 5.5, "AI"]

# Pisahkan data berdasarkan ketentuan
def pisahkan_data(data):
    int_data = defaultdict(list)
    float_data = []
    string_data = []

    for item in data:
        if isinstance(item, int):
            satuan = item % 10
            puluhan = (item // 10) % 10
            ratusan = item // 100
            int_data['satuan'].append(satuan)
            int_data['puluhan'].append(puluhan)
            int_data['ratusan'].append(ratusan)
        elif isinstance(item, float):
            float_data.append(item)
        elif isinstance(item, str):
            string_data.append(item)

    return {
        'int_data': dict(int_data),
        'float_data': tuple(float_data),
        'string_data': string_data
    }

hasil_pemisahan = pisahkan_data(random_list)

# Tampilkan data integer dalam bentuk dict
print("Data Integer:")
print(hasil_pemisahan['int_data'])

# Tampilkan data float dalam bentuk tuple
print("Data Float:")
print(hasil_pemisahan['float_data'])

# Tampilkan data string dalam bentuk list
print("Data String:")
print(hasil_pemisahan['string_data'])