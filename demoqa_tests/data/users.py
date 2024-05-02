import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_of_birth_year: str
    date_of_birth_month: str
    date_of_birth_day: str
    subject: str
    hobby: str
    photo: str
    address: str
    city: str
    state: str




user = User(first_name='Yasha', last_name= 'YA', email='name@example.com', gender='Female', number='1234567891',
            date_of_birth_year='1999', date_of_birth_month='May', date_of_birth_day='11', subject='Computer Science', hobby='Reading',
            photo='foto.jpg', address='Moscowskaya Street 18', city='Delhi', state='NCR')