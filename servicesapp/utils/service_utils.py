
class Service():
    def __init__(self,title,description,icon,color,link):
        self.title = title;
        self.description = description;
        self.icon = icon;
        self.color = color;
        self.link=link;


all_services = [
            Service(
                title="Real Estate & Consultancy", 
                description="All kinds of services related to buying and selling properties in Turkiye.",
                icon="building.png",
                color="bg-green",
                link="servicesapp:servicesapp_real_estate"
                ),
            Service(
                title="Citizenship & Residence Permit", 
                description="Services related to obtaining citizenship including paperwork and consultancy.",
                icon="passport.png",
                color="bg-yellow",
                link="servicesapp:servicesapp_citizenship"),
            Service(
                title="Export-Import", 
                description="Legal consultancy and advising related to export and import business in Turkiye.",
                icon="export_import.png",
                color="bg-purple",
                link='servicesapp:servicesapp_export_import'),
            Service(
                title="Study in Turkiye", 
                description="Assisting with the university selection, admission, and payment process in Turkish universities.",
                icon="study.png",
                color="bg-pale-blue",
                link='servicesapp:servicesapp_study'),
            Service(
                title="Hajj & Umrah", 
                description="Assisting with Hajj and Umrah processing, payments, and travels.",
                icon="hajj.png",
                color="bg-pink",
                link='servicesapp:servicesapp_hajj_umrah'),
            Service(
                title="Tourism-Health Tourism", 
                description="Arranging tours in different cities of Turkiye with accommodations and transportation services.",
                icon="tourism.png",
                color="bg-orange",
                link='servicesapp:servicesapp_tourism'),
            Service(
                title="Service Solutions", 
                description="Our expert team is ready to facilitate your work with sincere service.",
                icon="service.png",
                color="bg-red",
                link='servicesapp:servicesapp_service_solutions'),
        ]

