from selene import have

from demoqa_tests.data.users import User


class ProfilePage:
    def __init__(self, name, email, gender, number, date_of_birth, subject, hobby, photo, address, city, state):
         self.name = name
         self.email = email
         self.gender = gender
         self.number = number
         self.date_of_birth = date_of_birth
         self.subject = subject
         self.hobby = hobby
         self.photo = photo
         self.address = address
         self.city = city
         self.state = state


    def should_have_data(self, user: User):
        self.name.should(have.text(user.name))
        self.email.should(have.text(user.email))
        self.gender.should(have.text(user.gender))
        self.number.should(have.text(user.number))
        self.date_of_birth.should(have.text(user.date_of_birth))
        self.subject.should(have.text(user.subject))
        self.hobby.should(have.text(user.hobby))
        self.photo.should(have.text(user.photo))
        self.address.should(have.text(user.address))
        self.city.should(have.text(user.city))
        self.state.should(have.text(user.state))
        return self



    student = User(full_name='Yasha YA', email='name@example.com', gender='Female', number=1234567891, date_of_birth='11 May,1999', subject='Computer Science', hobby='Reading', photo='foto.jpg', address='Moscowskaya Street 18', city='NCR', state='Delhi')