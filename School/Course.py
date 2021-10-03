class Course:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.enrolled = []

    def enroll(self):
        raise 'Class must have students'

class Art(Course):
    def __init__(self, art_type, *args, **kwargs):
        self.art_type = art_type
        super(Course, self).__init__(*args, **kwargs)


a = Art(art_type=paint)

print(a)










