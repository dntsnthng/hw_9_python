import dataclasses


@dataclasses.dataclass
class User:
    name: str
    email: str
    gender: str
    number: str
    date_of_birth: str
    subject: str
    hobby: str
    photo: str
    address: str
    city: str
    state: str




user = User(name='Yasha YA', email='name@example.com', gender='Female', number='1234567891',
            date_of_birth='11 May,1999', subject='Computer Science', hobby='Reading',
            photo='foto.jpg', address='Moscowskaya Street 18', city='NCR', state='Delhi')


