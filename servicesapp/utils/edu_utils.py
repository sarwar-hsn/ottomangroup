from blogsapp.models import Blog
class Faq():
    def __init__(self,id,question,answer):
        self.id = id;
        self.question = question;
        self.answer = answer;
faqs = [
    Faq(
        1,
        "Why do I need an agency to get admission to a foreign university?", 
        "You need an agency to get admitted to a foreign university for the following: Proper guidance regarding courses, career prospects, university choices, admission process, accommodation, and much more. education consultants have contacts with universities abroad and can streamline your admission process."
    ),
    Faq(
        2,
        "How much are the university fees approximately?", 
        "Privet universities Start from an annual fee of $2000 and public universities starts from $300 and ranges vary according to the university’s quality, major, student qualification, and language of instruction."
    ),
    Faq(
        3,
        "In which language do universities offer education in Türkiye?", 
        "The medium of instruction at Turkish universities is either English, Turkish, or Arabic."
    ),
    Faq(
        4,
        "I do not have any English proficiency certificate/ Turkish language certificate. Can I apply for the program?", 
        "Yes, you can get admission without a language proficiency certificate but you must enter a language proficiency exam before starting your course. Turkish medium students must complete up to B2 level Turkish before starting their university course."
    ),
    Faq(
        5,
        "Can I work in Turkey after my graduation?", 
        "Yes, you can. International students are allowed to work in Turkey after graduation. Especially when they have graduated from Turkish universities, which increases their chances of landing a job in Türkiye after graduation."
    ),
    Faq(
        6,
        "Can I get any scholarship during my study?",
        "Yes, you can get merit-based scholarships from your university. You can also get other Marot and need-based scholarships from various charitable organizations that provide financial aid to students."
    )
]

pacakge_table=[
    {   
        'title':'Consultation over phone',
        'isAvailable':[
            'yes','yes','yes',
        ],
    },
    {
        'title':'Acquiring an acceptance letter',
        'isAvailable':[
            'yes','yes','yes',
        ]
    },
    {
        'title':'Certificate and mark-sheet translation & Notarization ',
        'isAvailable':[
            'yes','yes','yes',
        ]
    },
    {
        'title':'Assistance with visa procedure',
        'isAvailable':[
            'yes','yes','yes',
        ]
    },
    {
        'title':'Proper academic guidelines throughout the duration of the study',
        'isAvailable':[
            'yes','yes','yes',
        ]
    },
    {
        'title':'Having power of attorney on behalf of the student',
        'isAvailable':[
            'no','yes','yes',
        ]
    },
    {
        'title':'Acquiring the Turkish Student Certificate (Öğrenci Belgesi)',
        'isAvailable':[
            'no','yes','yes',
        ]
    },
        {
        'title':'Language course registration',
        'isAvailable':[
            'no','yes','yes',
        ]
    },
    {
        'title':'Turkish residence permit application ',
        'isAvailable':[
            'no','yes','yes',
        ]
    },
    {
        'title':'Live consultancy meeting via video conferencing',
        'isAvailable':[
            'no','no','yes',
        ]
    },
    {
        'title':'Sending all original documents to students via international cargo',
        'isAvailable':[
            'no','no','yes',
        ]
    },
    
    {
        'title':'Hotel booking/ student dormitory registration',
        'isAvailable':[
            'no','no','yes',
        ]
    },
    {
        'title':'Airport pickup from İstanbul',
        'isAvailable':[
            'no','no','yes',
        ]
    },
    {
        'title':'Health Insurance ',
        'isAvailable':[
            'no','no','yes',
        ]
    },
    
]

services =[
    {
        'title':'Before University Application',
        'body':[
            'Expert consultancy meeting via video conferencing',
            'University and department choice guidelines according to student\'s academic profile and preference',
            'Assistance with gathering all required documents for university application',
            'Draftworks for university application', 
        ]
    },
    {
        'title':'Student Registration',
        'body':[
            'University registration (Paperwork and Admission)',
            'Having power of attorney on behalf of the student',
            'Certificate and mark sheet Translation',
            'Certificate and mark sheet notarization',
            'Acquiring the acceptance letter',
            'Acquiring the Turkish Student Certificate (Öğrenci Belgesi)',
        ]
    },
    {
        'title':'Visa Application & Travel',
        'body':[
            'Getting an appointment for the visa center',
            'Guideline on gathering All required document',
            'Hotel Booking/ Student Dormitory Registration',
            'Air Ticket Reservation',
            'Sending All Original Documents to Students via International Cargo (Only for Premium Services',
        ]
    },
    {
        'title':'Arrival & Post-Arrival Services',
        'body':[
            'Purchasing Air Ticket',
            'Airport pickup with a car (From Türkiye)',
            'One night stay in Istanbul (at a 4-star hotel)',
            'Transportation to campus/city (BUS/AIR)',
            'Health insurance',
            'Turkish Residence Permit Application. (Paperwork and appointment)',
            'Language Courses Registration (Turkish/English/Arabic according to requirements)',
            'Academic Guidelines',
        ]
    },
]
working_process=[
    {
        'icon':'',
        'text':'General and individual education consultancy seminars with applicants and acadamacıans. (Online) '
    },
    {
        'icon':'',
        'text':'Collection of applicant\'s academic background and university selection/ creation of a university list according to the student\'s preference.'
    },
    {
        'icon':'',
        'text':'Collection of all required documents from the applicant. '
    },
    {
        'icon':'',
        'text':'Translation and notarization of documents (if required). Guideline on certificate attestation by respective Education Board, Ministry of Education, and Ministry of Foreign Affairs in Bangladesh.'
    },
    {
        'icon':'',
        'text':'Sending all required documents to the university for application purposes and acquiring an acceptance letter/ offer letter.'
    },
    {
        'icon':'',
        'text':'Acquire a Turkish Student Certificate (Öğrenci Belgesi) after registration and send all original documents to the student via international cargo. (For Premium Service)'
    },
    {
        'icon':'',
        'text':'Assistance with visa application paperwork (Proper Guidance)'
    },
    {
        'icon':'',
        'text':'Assistance with Dormitory and Language Institute application and registration.',
    },
    {
        'icon':'',
        'text':'Receiving the student from the airport and arranging transportation to the hotel/ dormitory.',
    },
    {
        'icon':'',
        'text':'Applying for a Student Resident Permit.',
    },
]



def retrive_blog(slug):
    blog = Blog.objects.filter(slug=slug)
    if blog:
        return blog[0]
    else:
        return None

university_types=[
    {
        'title':'Public University',
        'body':'Turkish public universities meet European education standards, offer Erasmus exchanges, internships,government dormitories, campuses free of politics at very low cost.',
        'class': 'uil uil-book-open text-green fs-40',
        'color': 'green',
        'blog': retrive_blog('public-universities-turkey'),
    },
    {
        'title':'Privet University',
        'body':'Turkey has excellent private universities with top rankings, quality education, and opportunities to study in English, compensating for higher costs compared to public universities.',
        'class': 'uil uil-book text-red fs-40',
        'color': 'red',
        'blog': retrive_blog('private-universities-turkey'),
    },
    {
        'title':'Medical University',
        'body':'Turkey\'s healthcare system is one of the world\'s best, with improving quality reflected in medical colleges. The country offers unprecedented job opportunities for doctors.',
        'class': 'uil uil-book-medical text-white fs-40',
        'color': 'primary',
        'blog': retrive_blog('medical-universities-turkey'),
    },
    {
        'title':'Language Institute',
        'body':'Turkish language proficiency is recommended for students whose medium of instruction is Turkish. Learning Turkish is also beneficial for socializing and interacting with locals.',
        'class': 'uil uil-english-to-chinese text-violet fs-40',
        'color': 'violet',
        'blog': retrive_blog('language-schools-turkey'),
    }
]