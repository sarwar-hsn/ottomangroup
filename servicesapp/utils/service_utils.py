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
                description="All kinds of services related to buying and selling properties in Turkiye, assist with the process of getting citizenship and make sure the process is complete within the shortest time.",
                icon="building.png",
                color="bg-green",
                link="servicesapp:servicesapp_real_estate"
                ),
            Service(
                title="Citizenship & Residence Permit", 
                description="Citizenship of services related to buying and selling properties in Turkiye, assist with the process of getting citizenship and make sure the process is complete within the shortest time.",
                icon="passport.png",
                color="bg-yellow",
                link="servicesapp:servicesapp_citizenship"),
            Service(
                title="Export-Import", 
                description="All kinds of services related to buying and selling properties in Turkiye, assist with the process of getting citizenship and make sure the process is complete within the shortest time.",
                icon="export_import.png",
                color="bg-purple",
                link='servicesapp:servicesapp_export_import'),
            Service(
                title="Study in Turkiye", 
                description="All kinds of services related to buying and selling properties in Turkiye, assist with the process of getting citizenship and make sure the process is complete within the shortest time.",
                icon="study.png",
                color="bg-pale-blue",
                link='servicesapp:servicesapp_study'),
            Service(
                title="Hajj & Umrah", 
                description="All kinds of services related to buying and selling properties in Turkiye, assist with the process of getting citizenship and make sure the process is complete within the shortest time.",
                icon="hajj.png",
                color="bg-pink",
                link='servicesapp:servicesapp_hajj_umrah'),
            Service(
                title="Tourism-Health Tourism", 
                description="All kinds of services related to buying and selling properties in Turkiye, assist with the process of getting citizenship and make sure the process is complete within the shortest time.",
                icon="tourism.png",
                color="bg-orange",
                link='servicesapp:servicesapp_tourism'),
            Service(
                title="Service Solutions", 
                description="All kinds of services related to buying and selling properties in Turkiye, assist with the process of getting citizenship and make sure the process is complete within the shortest time.",
                icon="service.png",
                color="bg-red",
                link='servicesapp:servicesapp_service_solutions'),
        ]