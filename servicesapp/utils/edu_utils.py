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

services =[
    {
        'title':'Standard Services',
        'body':[
            'University Application',
            'Acquiring an acceptance letter',
            'Taking power of attorney on behalf of the student',
            'Certificate and mark sheet Translation',
            'Certificate and mark sheet notarization',
            'Acquiring the Turkish Student Certificate(Öğrenci Belgesi)',
            'Hotel Booking',
            'Health Insurance',
            'Assistance with visa procedure',
            'Turkish Residence Permit Application'
        ]
    },
    {
        'title':'Premium Services',
        'body':[
            'Live consultancy meeting via video conferencing',
            'University application',
            'Acquiring an acceptance letter',
            'Having power of attorney on behalf of the student',
            'Certificate and mark-sheet translation',
            'Certificate and mark sheet notarization',
            'Acquiring the Turkish Student Certificate (Öğrenci Belgesi)',
            'ending all original documents to students via International cargo',
            'Assistance with visa procedure',
            'Hotel booking/ student dormitory registration',
            'Air ticket reservation',
            'Airport pickup with a car (from Türkiye)',
            'One night stay in Istanbul (at a 4-star hotel) ',
            'Transportation to campus/city (BUS/AIR)',
            'Health insurance',
            'Turkish residence permit application',
            'Language course registration',
            'Proper academic guidelines throughout the duration of the study',
        ]
    },
    {
        'title':'Basic Services',
        'body':[
            'University application',
            'Acquiring an Acceptance Letter',
            'Assistance with visa procedure (proper guidance)',

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